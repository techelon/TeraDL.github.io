#--> Standard module & library
import json

#--> Flask
from flask import Flask, Response, request
from flask_cors import CORS
app = Flask(import_name=__name__)
CORS(app=app)

#--> Local module
from python.terabox import TeraboxFile, TeraboxLink

#--> Main
@app.route(rule='/')
def stream() -> Response:
    response: dict[str,str] = {
        'status'  : 'success',
        'service' : [
            {
                'method'   : 'POST',
                'endpoint' : 'generate_file',
                'url'      : '{}generate_file'.format(request.url_root),
                'params'   : ['url'],
                'response' : ['status', 'js_token', 'browser_id', 'cookie', 'sign', 'timestamp', 'shareid', 'uk', 'list']},
            {
                'method'   : 'POST',
                'endpoint' : 'generate_link',
                'url'      : '{}generate_link'.format(request.url_root),
                'params'   : ['js_token', 'cookie', 'sign', 'timestamp', 'shareid', 'uk', 'fs_id'],
                'response' : ['status', 'download_link']}],
        'message' : 'hayo mau ngapain?'}
    return Response(response=json.dumps(obj=response, sort_keys=False), mimetype='application/json')

#--> Get file
@app.route(rule='/generate_file', methods=['POST'])
def getFile() -> Response:
    
    try:

        data : dict = request.get_json()
        result = {'status':'failed', 'message':'invalid params'}

        if data.get('url'):
            TF = TeraboxFile()
            TF.search(data.get('url'))
            result = TF.result
    
    except: result = {'status':'failed', 'message':'wrong payload'}

    return Response(response=json.dumps(obj=result, sort_keys=False), mimetype='application/json')

#--> Get link
@app.route(rule='/generate_link', methods=['POST'])
def getLink() -> Response:
    
    try:

        data : dict = request.get_json()
        result = {'status':'failed', 'message':'invalid params'}

        required_keys = {'fs_id', 'uk', 'shareid', 'timestamp', 'sign', 'js_token', 'cookie'}
        if all(key in data for key in required_keys):
            TL = TeraboxLink(**{key: data[key] for key in required_keys})
            TL.generate()
            result = TL.result
    
    except: result = {'status':'failed', 'message':'wrong payload'}

    return Response(response=json.dumps(obj=result, sort_keys=False), mimetype='application/json')

#--> Initialization
if __name__ == '__main__':
    app.run(debug=True)
    
# https://1024terabox.com/s/1eBHBOzcEI-VpUGA_xIcGQg