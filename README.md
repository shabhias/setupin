
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

