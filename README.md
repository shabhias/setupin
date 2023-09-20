## TUGAS 3

## Apa perbedaan antara form POST dan form GET dalam Django?
dalam penggunaannya, GET mengirimkan data formulir ke server melalui URL dan disimpan dalam URL, sedangkan POST mengirimkan data formulir ke server dan disimpan dalam body permintaan HTTP. Dari segi keamanan, POST lebih aman dibandingkan dengan GET karena data tersebut tidak terlihat di URL.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML: digunakan untuk menyimpan dan bertukar data antara sistem komputer. XML memiliki struktur yang fleksibel dan dapat dibaca oleh mesin dan manusia, biasanya digunakan untuk pertukaran data antar aplikasi. 
JSON: digunakan untuk pertukaran data yang ringan dan efisien antara sistem yang berbeda. dapat dipahami berbagai bahasa pemrograman. Lebih sederhana dibandingkan dengan XML
HTML: digunakan untuk membuat struktur dan tampilan halaman web. Tidak digunakan untuk pertukaran data antar aplikasi, melaikan untuk menyajikan data kepada user melalui halaman web

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
jSON sering digunakan dalam pertukaran data antara aplikasi web modern karena formatnya ringan dan mudah dibaca serta mudah dipahami berbagai bahasa pemrograman.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
### Membuat input form untuk menambahkan objek model pada app sebelumnya.
 - buat berkas forms.py untuk membuat struktur form dengan menggunakan model.py untuk model product. agar dapat input data produk baru
 - dalam berkas views.py ditambahkan fungsi create_product untuk pembuatan data produk baru berdasarkan input dari form
 - fungsi show main digunakan untuk menampilkan semua produk yang tersimpan di database. 
 - pada berkas urls.py diatur URL untuk mengakses fungsi create_product yang sudah dibuat sebelumnya
 - dibuat berkas create_product.html yang berisi form untuk menambahkan data produk baru. Form ini menggunakan metode POST. 
 - dalam berkas main.html ditambahkan kode untuk menampilkan data produk dalam bentuk tabel dan tombol "add new product" yang mengarahkan user ke halaman form 

### Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
 - lalu tambahkan lima fungsi views untuk melihat objek dalam berbagai format seperti HTML, XML, JSON, XML by ID, dan JSON by ID. fungsi tersebut memberikan fleksibilitas kepada pengguna aplikasi dalam mengakses dan memanfaatkan data.   
 - dengan menambahkan fungsi yang menerima parameter request dengan nama show_xml,show_JSON,show_xml_by_id, dan show_json_by_id ke dalam file views.py

### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
 - lalu membuat routing URL untuk masing-masing views yangg telah ditambahkan untuk menghubungkan permintaan HTTP dari user ke fungsi views. 
 - dengan mengimpor fungsi yang sudah di buat dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

























## TUGAS 2
## Step-by-Step

### 1. Membuat Sebuah Proyek Django Baru
Untuk membuat proyek Django baru, diperlukan sebuah direktori dan mengaktifkan virtual environment untuk mengisolasi package dari aplikasi sehingga tidak bertabrakan jika menjalankan program.

### 2. Membuat Aplikasi dengan Nama "main" pada Proyek
Untuk membuat aplikasi "main" pada proyek, jalankan perintah `python manage.py startapp main`. Perintah tersebut akan membentuk direktori baru dengan nama "main" yang berisi struktur awal aplikasi.

### 3. Melakukan Routing pada Proyek agar Dapat Menjalankan Aplikasi "main"
Untuk melakukan routing, dalam berkas urls.py proyek utama harus menambahkan routing khusus untuk aplikasi "main" path('main/', include('main.urls')). Ini akan mengarahkan URL tertentu ke views yang sesuai dalam aplikasi "main". Setelah itu konfigurasi 
routing aplikasi main pada berkas urls.py pada direktori main menambahkan path('', views.index, name='index') pada url patterns

### 4. Membuat Model pada Aplikasi "main" dengan Nama "item" dan Atribut Wajib
Pada langkah ini, kita memodifikasi berkas `models.py` untuk mendefinisikan model yang akan digunakan dalam aplikasi "main" berupa atribut "name," "amount," dan juga "description."

### 5. Membuat Sebuah Routing pada `urls.py` untuk Memetakan Fungsi yang Telah Dibuat pada `views.py`
Membuat berkas `urls.py` pada "main" dan juga pada direktori utama. Dengan ini, aplikasi "main" dapat terhubung pada URL proyek.

### 6. Membuat Deployment Adaptable
Membuat akun adaptable.io dan menghubungkannya ke dalam repository yang ada di GitHub. Proses deployment adaptable untuk membuat aplikasi yang stabil.

## Bagan 
[![Screenshot-2023-09-13-094510.png](https://i.postimg.cc/sDPfJ7Fk/Screenshot-2023-09-13-094510.png)](https://postimg.cc/2V6fkqSG)

## Mengapa Kita Menggunakan Virtual Environment?
Virtual environment memungkinkan pengguna untuk berinteraksi dengan komputasi lain dengan mengisolasi dependency proyek, sehingga proyek yang berbeda tidak saling mengganggu.

## Apakah Kita Tetap Dapat Membuat Aplikasi Web Berbasis Django Tanpa Menggunakan Virtual Environment?
Kita masih bisa membuat Django tanpa menggunakan virtual environment, tetapi akan terjadi konflik yang sulit apabila tidak memastikan bahwa dependensi proyek tidak saling bertabrakan dengan dependensi proyek lain di lingkungan Python.

## Apa itu MVC, MVT, MVVM, dan Perbedaan dari Ketiganya?
- **MVC (Model-View-Controller)**:
  - Model: data dan logika aplikasi
  - View: menampilkan informasi kepada pengguna
  - Controller: menerima input dari pengguna dan mengirimkannya ke Model atau View

- **MVT (Model-View-Template)**:
  - Model: data dan logika aplikasi
  - View: logika pengolahan dan mempersiapkan data untuk ditampilkan di Template
  - Template: menampilkan data yang diberikan oleh View dalam bentuk yang sesuai untuk pengguna.

- **MVVM (Model-View-ViewModel)**:
  - Model: data dan logika aplikasi
  - View: menampilkan informasi kepada pengguna
  - ViewModel: perantara antara Model dan View. ViewModel mengelola logika dan menyediakan data yang diperlukan oleh View.
- **perbedaan**:
	-MVC mengatur logika bisnis dan tampilan secara terpisah, sedangkan MVT dan MVVM mengatur logika bisnis dan tampilan secara terintegrasi.
	-MVT memisahkan logika pengolahan data dan tampilan menjadi View dan Template, sedangkan MVVM memisahkan logika bisnis dan tampilan menjadi View dan ViewModel.
	-MVC dan MVT lebih sering digunakan dalam pengembangan aplikasi web, sedangkan MVVM lebih umum digunakan dalam pengembangan aplikasi dengan antarmuka pengguna yang kompleks.
  
Perbedaan utama adalah dalam cara mereka mengatur logika aplikasi dan tampilan, serta bagaimana mereka berinteraksi dengan komponen lainnya.

