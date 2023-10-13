


<summary>TUGAS 6 </summary>

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Syncronus programming mengerjakan tugas secara berurutan. Setiap tugas harus selesai sebelum tugas berikutnya dapat dimulai. Dengan demikian, program menunggu setiap tugas selesai sebelum melanjutkan ke tugas berikutnya. Synchronous programming sering disebut "blocking" karena menghentikan eksekusi kode lebih lanjut sampai tugas saat ini selesai.

- Asynchronous Programming mengerjakan tugas secara independen satu sama lain. Program dapat melanjutkan tugasnya ain sambil menunggu tugas asynchronous selesai, ini memungkinkan beberapa tugas dieksekusi secara bersamaan, meningkatkan efisiensi dan responsivitas program. Asynchronous programming sering disebut "non-blocking" karena tidak menghentikan eksekusi kode lebih lanjut.


Dalam pemrograman berbasis platform, asynchronous programming sangat penting karena banyak operasi yang membutuhkan waktu lama, seperti operasi I/O atau akses ke database. Dengan menggunakan asynchronous programming, program dapat menjalankan tugas-tugas ini secara efisien tanpa menghentikan eksekusi kode lainnya. Hal ini dapat meningkatkan responsivitas program dan kinerja secara keseluruhan.

## Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada penggantian tabel data menggunakan AJAX

Paradigma event-driven programming adalah pendekatan pemrograman di mana alur eksekusi program ditentukan oleh kejadian atau peristiwa yang terjadi. Dalam paradigma ini, program akan merespons kejadian atau peristiwa yang terjadi dengan menjalankan kode yang terkait.

Contoh penerapan paradigma event-driven programming pada penggantian tabel data menggunakan AJAX adalah sebagai berikut:

Misalkan kita memiliki sebuah halaman web yang menampilkan tabel data. Ketika pengguna melakukan interaksi tertentu, seperti mengklik tombol "Refresh", kita ingin menggantikan isi tabel dengan data baru tanpa harus memuat ulang seluruh halaman.

Dalam penerapan ini, kita dapat menggunakan AJAX (Asynchronous JavaScript and XML) untuk mengambil data baru dari server secara asynchronous. Ketika pengguna mengklik tombol "Refresh", kita akan mengirim permintaan ke server untuk mendapatkan data baru. Setelah menerima data dari server, kita akan menggunakan JavaScript untuk menggantikan isi tabel dengan data baru tersebut.


## Jelaskan penerapan asynchronous programming pada AJAX.



## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

> FETCH API:
bawaan pada JavaScript yang menyediakan antarmuka untuk melakukan permintaan HTTP secara asynchronous.

kelebihan:
- Memiliki ukuran yang lebih kecil. Memiliki fitur-fitur seperti Promise dan Async/await yang memudahkan pengelolaan permintaan dan tanggapan secara asynchronus. Selain itu, fetch API juga dapat mengatur metode HTTP lebih mudah. 


kekurangan:
- Fetch API tidak didukung oleh semua browser lama.

> JQUERY

kelebihan:
- jQuery dirancang untuk mendukung berbagai browser. 

kekurangan:
- Library jQuery memiliki ukuran yang lebih besar dibandingkan dengan Fetch API. 


kesimpulan:
Pilihan antara FETCH API dan JQuery tergantung pada kebutuhan dan preferensi user. Fetch API dapat digunakan apabila 



## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. pengimplementasian cards dengan mengimplementasikan AJAX GET pada <script>
2. menambahkan <button type="button" class="button is-success" id="addItemButton">
    Add New Item by AJAX
    </button>
3. menambahkan function addProduct()

      function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(() => {
            refreshProducts();
            document.getElementById("form").reset(); 
            document.getElementById("exampleModal").classList.remove("is-active");
        });
        return false;
    }

4. Membuat Fungsi View Baru untuk Nenambahkan Item Baru ke dalam Basis Data
      @csrf_exempt
      def add_product_ajax(request):
          if request.method == 'POST':
              form = ProductForm(request.POST)

          if form.is_valid():
              product = form.save(commit=False)
              product.user = request.user
              product.save()
              return HttpResponse("Created", status=201)
          else:
              # Handle form validation errors and return as JSON
              errors = form.errors.as_json()
              return HttpResponseBadRequest(errors, content_type='application/json')
          return HttpResponseNotFound()

5. Membuat Path /create-ajax/ yang Mengarah ke Fungsi View add_item_ajax(request) dan Menghubungkan Form yang telah dibuat di dalam Modal ke Path /create-ajax/
    path('create-ajax/', add_product_ajax, name='add_product_ajax')


Bonus:  menambahkan function delete item dengan menggunakan AJAX DELETE


<summary> TUGAS 5 </summary>

## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

Manfaat selector dalam CSS adalah untuk memberikan gaya umum untuk semua elemen, seperti mengatur padding ataupun margin. selector juga menambahkan keunikan dalam sebuah web yang membuat pembaca merasakan. Waktu yang tepat untuk menggunakannya adalah 


## Jelaskan HTML5 Tag yang kamu ketahui.

<header>: Digunakan untuk mengelompokkan elemen-elemen header pada halaman web, seperti judul, logo, dan menu navigasi.
<nav>: Digunakan untuk mengelompokkan elemen-elemen navigasi pada halaman web, seperti menu atau daftar tautan.
<section>: Digunakan untuk mengelompokkan elemen-elemen yang terkait secara tematik pada halaman web, seperti bagian-bagian dari artikel atau konten.
<article>: Digunakan untuk mengelompokkan konten yang berdiri sendiri dan dapat berdiri sendiri secara independen, seperti artikel berita atau posting blog.
<aside>: Digunakan untuk mengelompokkan konten yang berhubungan dengan konten utama pada halaman web, seperti sidebar atau kotak info tambahan.
<footer>: Digunakan untuk mengelompokkan elemen-elemen footer pada halaman web, seperti informasi kontak, tautan ke halaman lain, atau hak cipta.

## Jelaskan perbedaan antara margin dan padding.

Perbedaan utama antara margin dan padding adalah bahwa margin mempengaruhi jarak antara elemen dengan elemen lain di sekitarnya, sementara padding mempengaruhi jarak antara konten elemen dengan batas elemen. Margin tidak memiliki warna latar belakang dan tidak mempengaruhi warna latar belakang elemen lain, sedangkan padding dapat memiliki unsur warna yang sesuai dengan warna latar belakang elemen.

##  Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

DESIGN:
-BootStrap: tampilan yang cukup terstruktur dan konsisten. 
-TailWind: memberikan kebebasan kreatif yang lebih besar dan memungkinkan penggunaan class yang sangat spesifik.

FLEKSIBILITASl
- BottStrap:Meskipun Bootstrap menyediakan beberapa opsi customisasi, fleksibilitasnya terbatas dibandingkan dengan Tailwind CSS. Anda mungkin perlu menambahkan atau mengganti beberapa kelas CSS secara manual untuk mendapatkan tampilan yang sesuai dengan kebutuhan Anda.
- TailWind: Fleksibilitas Tailwind CSS terletak pada kemampuannya untuk memberikan kontrol yang lebih besar dalam styling elemen.

UKURAN FILE
-BootStrap: Bootstrap adalah kerangka kerja yang lebih besar dalam hal ukuran file karena menyediakan banyak fitur dan komponen yang siap pakai. Ini mungkin berdampak pada kecepatan pengunduhan dan performa halaman web.
- TailWind: dirancang untuk lebih ringan dalam hal ukuran file. Namun, ketika kita menggunakan banyak class utilitas dalam kode, ukuran file CSS dapat meningkat.

referensi: https://codepolitan.com/blog/perbedaan-bootstrap-dan-tailwind


<summary>TUGAS 4 </summary>

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
- usercreation form adalah form yang disediakan django untuk pembuatan user dengan fitur keamanan seperti username dan password dalam aplikasi web
- kelebihannya adalah mudah digunakan dan memiliki fitur keamanan yang sudah disediakan oleh jango
- kekurangannya adalah tampilan kurang menarik dan fitur-fiturnya terbatas

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Auntentikasi proses mengidentifikasi user
- ototritas proses memberikan hak akses kepada user yang terlah terauntetikasi
- keduanya sangat penting untuk melindungi hak akses dan data 


## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
 - cookies digunakan pada situs web untuk menyimpan informasi user termasuk pengelolaan data user.
- a. user mengakses web django, kemudian server Django akan membuat ID unik untuk user dan menyimpannya ke cookies yang sudah dikirim ke user. 
  b. kemudian, ketika user menggunakan aplikasi web lagi, ID akan dikirim kembali ke server Django melalui cookies. Fungsi ID untuk mengidentifikasi user yang sesuai dan menyimpan atau mengambil data yang relevan
  c. Django menyimpan data di server, dalam database atau cache dan menghubungkannya dengan ID yang dikirim melalui cookies
  d. risiko potensial yang harus diwaspadai adalah, kerentanan terhadap Cross-Site Scripting(XSS) jika data yang disimpan tidak dilakukan secara benar. 

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
- informasi pribadi user dapat di salah gunakan
- serangan XSS, menyisipkan skrip berbahaya ke dalam halaman web yang dapat dieksekusi oleh user. Hal ini dapat mengakibatkan pencurian data pribadi atau pengalihan ke situs web berbahaya.
- serangan CSRF, yang dapat merubah pengaturan akun

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
   - untuk membuat registrasi form, import UserCreationForm yang memudahkan kita untuk membuat registrasi form tanpa menulis kode dari awal. Kemudian membuat fungsi regitrasi harus memvalidasi input dan menyimpan data form tersebut. Kemudian membuat html dari form yang sudah dibuat
   - untuk membuat login, import metode yang diperlukan untuk autentikasi login. Kemudian buatlah template untuk login berupa HTML. Dengan menambahkan path URL ini ke dalam urlpatterns di file urls.py pada subdirektori main, maka pola URL telah terhubung dengan fungsi login_user
   - untuk membuat log out, membuat fungsi log untuk menghapus sesi pengguna yang masuk. Kemudian mengarahkan pengguna ke halaman login dalam aplikasi Django dan kemudian hubungan fungsi tersebut dengan URL. 

### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
   - Untuk membuat dua akun pengguna dengan tiga dummy data menggunakan model yang telah dibuat sebelumnya pada aplikasi di lokal, perlu impor model User dan Item ke dalam file yang akan digunakan. Kemudian 


### Menghubungkan model Item dengan User.
   - untuk menghubungkan product dengan user, kita harus import user ke dalam file models.py agar dapat mengidentifikasinya.Kemudian pastikan model Item memiliki field ForeignKey yang mengacu pada model User. Kemudian menambahkan Item.objects.filter(owner=user) untuk mendapatkan semua item yang dimiliki oleh seorang pengguna tertentu, di mana user adalah instance dari model User.


### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
   - import datetimen. Kemudian pada fungsi login_user, kita akan menambahkan fungsi untuk menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. `response.setcookie('last_login', str(datetime.datetime.now())) berfungsi untuk membuat _cookie last_login dan menambahkannya ke dalam response. Kemudian tambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context untuk  menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web. Kemudian jangan lupa untuk menghapus menghapus cookie last_login saat pengguna melakukan logout.


<summary>TUGAS 2  </summary>
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

