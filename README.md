## TeraDL - Terabox Video Downloader & Streaming

<div style="text-align:justify; line-height:1.3;"><b>TeraDL</b> adalah platform untuk streaming atau mengunduh file Terabox secara gratis dan cepat, yang diciptakan agar pengguna tidak perlu menginstall aplikasi Terabox terlebih dahulu, tapi hanya dengan memasukkan url, kemudian file siap diunduh</div>

### Informasi

<table style="border-collapse: collapse;">
    <tr>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">Version</td>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">1.4</td>
    </tr>
    <tr>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">Website</td>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;"><a href="https://teradl.dapuntaratya.com">TeraDL</a></td>
    </tr>
    <tr>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">API</td>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;"><a href="https://teradl-api.dapuntaratya.com">TeraDL API</a></td>
    </tr>
    <tr>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">Author</td>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;"><a href="https://www.facebook.com/Dapunta.Khurayra.X">Dapunta Khurayra X</a></td>
    </tr>
    <tr>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">Status</td>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">Open Source (Full)</td>
    </tr>
</table>

### Screenshot

<table style="border-collapse: collapse; width: 100%; max-width: 800px; table-layout: fixed;">
    <tr>
        <td style="border: 1px solid transparent; padding: 5px; text-align: center;">
            <img src="assets/screenshot1.png" alt="Image" style="width: 100%; height: auto;">
        </td>
        <td style="border: 1px solid transparent; padding: 5px; text-align: center;">
            <img src="assets/screenshot2.png" alt="Image" style="width: 100%; height: auto;">
        </td>
        <td style="border: 1px solid transparent; padding: 5px; text-align: center;">
            <img src="assets/screenshot3.png" alt="Image" style="width: 100%; height: auto;">
        </td>
    </tr>
</table>

### TechStack

<table style="border-collapse: collapse;">
    <tr>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">Backend</td>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">Python (Flask)</td>
    </tr>
    <tr>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">Frontend</td>
        <td style="border: 1px solid transparent; line-height:1.3; padding: 0px;">HTML, CSS (VanillaCSS), Javascript (VanillaJS)</td>
    </tr>
</table>

<br>

### Changelog

<br>

- **Apa Yang Baru Di Versi 1.4?**
    - Fitur streaming video secara langsung
    - Support download berbagai format file
        - Video : `.mp4`, `.mov`, `.mkv`, `.m4v`, `.asf`, `.avi`, `.wmv`, `.m2ts`, `.3g2`
        - Gambar : `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`
        - Lainnya : `.pdf`, `.docx`, `.zip`, `.rar`, `.7z`

    <br>

- **Apa Yang Baru Di Versi 1.3?**
    - Penambahan mode baru *(`get link` dengan `cookies` dari sisi server)* sehingga URL download lebih awet, meminimalisir error, dan proses download menjadi lebih cepat
        - **Mode 1** : Menggunakan cookies dynamic yang didapat dari scrap secara real time
        - **Mode 2** : Menggunakan cookies static dari admin (sesi login akun admin)
    - Auto switch mode jika `cookies` dari sisi server invalid

    <br>

- **Apa Yang Baru Di Versi 1.2?**

    - [TeraDL](https://teradl.dapuntaratya.com/) adalah project lanjutan dari [TeraStream](https://terastream.dapuntaratya.com/)
    - Perbaikan `get file` yang sebelumnya error
    - Perubahan logika pemrograman untuk `get file` dan `get link` sehingga proses loading lebih cepat
    - Perubahan tampilan menjadi lebih sederhana dan agar terkesan lebih menarik

<br>

### Cara Penggunaan API

- Javascript : [Javascript Implementation](https://github.com/Dapunta/TeraDL/tree/main/api)