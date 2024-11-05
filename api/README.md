## Implementasi API Javascript

<br>

### Inisialisasi Variabel Awal

```js
const api = 'https://teradl-api.dapuntaratya.com';
let mode = 1; // Mode Default = 1
```

<br>

### Melakukan requests ke endpoint `get_config` untuk mendapat status mode *(wajib)*

```js
async function getConfig() {

    const url = `${api}/get_config`;

    const headers = {'Content-Type':'application/json'};
    const data = {
        'method'  : 'GET',
        'mode'    : 'cors',
        'headers' : headers
    };

    const req = await fetch(url, data);
    const response = await req.json();
    return(response.mode);
}
```
- Ini bertujuan sebagai auto switch mode dari sisi client, karena apabila cookies admin invalid, maka otomatis switch ke mode 1 *(tanpa cookie)*
- Response
    - `{"mode":1}` jika cookie admin invalid
    - `{"mode":2}` jika cookie admin valid
- Jika anda tidak melakukannya *(membuat auto switcher)*, resiko error tanggung sendiri

<br>

### **Mode 1** : Dynamic Cookie

#### Pastikan mode terlebih dahulu, bebas *di-inisialisasi* dimana, apakah saat program *di-load*, atau setiap fetch url

```js
mode = await getConfig(); // Jika ingin auto switch
mode = 1 // Jika ingin manual
```

#### **Requests 1** : Mendapatkan Semua Daftar File

```js
const url = 'link terabox yg mau dicari';

const get_file_url = `${api}/generate_file`;
const headers = {'Content-Type':'application/json'};
const data = {
    'method'  : 'POST',
    'mode'    : 'cors',
    'headers' : headers,
    'body'    : JSON.stringify({'url':url, 'mode':mode})
};

const req = await fetch(get_file_url, data);
const response = await req.json();
```

- Response requests 1
    ```json
    {
        "status": "success",
        "js_token": "js token wes",
        "browser_id": "mbuh pokoke browser id",
        "cookie": "iki cookie ne",
        "sign": "ha iki sign e",
        "timestamp": "nek iki tondo wektu",
        "shareid": "nek jareku iki id file e",
        "uk": "iki id akunmu otomatis",
        "list": [ // Inilah daftar filenya
            {...data_lain, "fs_id":"17428684593055"},
            {...data_lain, "fs_id":"13423453893056"},
            {...data_lain, "fs_id":"19346834756567"},
        ]
    }
    ```
- Mode 1 hanya menghasilkan `fs_id` untuk tiap filenya, jadi untuk mendapatkan link downloadnya perlu mengirim payload lengkap pada requests 2

#### **Requests 2** : Mendapatkan URL *(Download & Mirror)* Dari Tiap File

```js
const param = {

    // Static, bisa dipake berulang asal filenya dalam response requests 1 yg sama
    'mode'      : mode,
    'uk'        : "uk dari response requests 1",
    'shareid'   : "shareid dari response requests 1",
    'timestamp' : "timestamp dari response requests 1",
    'sign'      : "sign dari response requests 1",
    'js_token'  : "js_token dari response requests 1",
    'cookie'    : "cookie dari response requests 1",

    // Dynamic, tiap file beda-beda
    'fs_id'     : "inituh unique id dari tiap file"
};

const get_link_url = `${api}/generate_link`;
const headers = {'Content-Type':'application/json'};
const data = {
    'method'  : 'POST',
    'mode'    : 'cors',
    'headers' : headers,
    'body'    : JSON.stringify(param)
};

const req = await fetch(get_link_url, data);
const response = await req.json();
```

- Response requests 2
    ```json
    {
        "status": "success",
        "download_link": {
            "url_1": "base url lemot banget tapi kedownload kok",
            "url_2": "mirror url buat streaming",
            "url_3": "mirror url cepet tapi sering error"
        }
    }
    ```

<br>

### **Mode 2** : Static Cookie

#### Pastikan mode terlebih dahulu, bebas *di-inisialisasi* dimana, apakah saat program *di-load*, atau setiap fetch url

```js
mode = await getConfig(); // Jika ingin auto switch
mode = 2 // Jika ingin manual
```

#### **Requests 1** : Mendapatkan Semua Daftar File

```js
const url = 'link terabox yg mau dicari';

const get_file_url = `${api}/generate_file`;
const headers = {'Content-Type':'application/json'};
const data = {
    'method'  : 'POST',
    'mode'    : 'cors',
    'headers' : headers,
    'body'    : JSON.stringify({'url':url, 'mode':mode})
};

const req = await fetch(get_file_url, data);
const response = await req.json();
```

- Response requests 1
    ```json
    {
        "status": "success",
        "js_token": "js token wes",
        "browser_id": "mbuh pokoke browser id",
        "cookie": "iki cookie ne",
        "sign": "ha iki sign e",
        "timestamp": "nek iki tondo wektu",
        "shareid": "nek jareku iki id file e",
        "uk": "iki id akunmu otomatis",
        "list": [ // Inilah daftar filenya
            {...data_lain, "fs_id":"17428684593055", "link": "https://dm-d.terabox.com/..."},
            {...data_lain, "fs_id":"13423453893056", "link": "https://dm-d.terabox.com/..."},
            {...data_lain, "fs_id":"19346834756567", "link": "https://dm-d.terabox.com/..."},
        ]
    }
    ```
- Mode 2 menghasilkan `link` untuk tiap filenya. ini merupakan base download link *(bisa langsung digunakan untuk download)*
- Jika ingin mendapat mirror link, lanjut ke requests 2 tapi hanya dengan mengirim `link` saja

#### **Requests 2** : Mendapatkan URL *(Download & Mirror)* Dari Tiap File

```js
const param = {

    // Static
    'mode' : mode,

    // Dynamic, tiap file beda-beda
    'url' : "pake link dari requests 1 tadi"
};

const get_link_url = `${api}/generate_link`;
const headers = {'Content-Type':'application/json'};
const data = {
    'method'  : 'POST',
    'mode'    : 'cors',
    'headers' : headers,
    'body'    : JSON.stringify(param)
};

const req = await fetch(get_link_url, data);
const response = await req.json();
```

- Response requests 2
    ```json
    {
        "status": "success",
        "download_link": {
            "url_1": "base url lemot banget tapi kedownload kok",
            "url_2": "mirror url buat streaming",
            "url_3": "mirror url cepet tapi sering error"
        }
    }
    ```