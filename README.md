# Cara Kerja Program
  Program yang dibuat merupakan sebuah implementasi dari single linked list yang menggambarkan proses antrian pembuatan kartu perpustakaan. Berikut ini adalah penjelasan dari setiap bagian program yang mendukung bagaimana program bekerja.
  
Pada program terdapat dua kelas yaitu:
 
1. Class Node: digunakan untuk membuat objek node, yang berisi data dan arahan ke node berikutnya.
2. Class LinkedList: digunakan untuk membuat objek linked list, yang berisi head node dan list history untuk menyimpan setiap data masuk dan data keluar pada linked list.

Pada program terdapat empat def atau fungsi yaitu sebagai berikut.
  
1. Fungsi init(): digunakan untuk mendefinisikan head node dan list history.
2. FungsitambahAkhir(): digunakan untuk menambahkan data baru pada akhir linked list, dengan memeriksa apakah linked list kosong atau tidak.
3. FungsihapusDepan(): digunakan untuk menghapus data pertama yang diinput pada linked list (yaitu yang berada paling depan pada antrian), jika linked list tidak kosong.
4. Fungsi printList(): digunakan untuk menampilkan isi linked list, dimulai dari head node.

Program juga dilengkapai dengan menu yang terdiri dari 5 pilihan, yaitu sebagai berikut.
1. Tambah antrian: meminta input nama pendaftar, dan menambahkan nama tersebut pada akhir linked list.
2. Tampilkan daftar antrian: menampilkan semua nama pendaftar dalam antrian, dimulai dari yang paling depan atau yang terlebih dahulu masuk.
3. Panggil antrian: menghapus nama pendaftar yang paling depan pada antrian.
4. Riwayat antrian: menampilkan riwayat setiap hal yang dilakukan pada antrian (misalnya, data masuk atau data dihapus).
5. Exit: keluar dari program.

  Dengan demikian, program tersebut mengimplementasikan struktur data linked list untuk membuat sistem antrian pada perpustakaan, dan dilengkapi dengan menu yang dapat menambah, menghapus, melihat daftar nama pendaftar dalam antrian, dan melihat riwayat pada antrian.

# Fungsionalitas Program
  Program ini merupakan sebuah implementasi dari struktur data linked list yang digunakan untuk membuat antrian pada perpustakaan. Fungsionalitas program adalah unutuk mengidentifikasi setiap data yang masuk dan data yang keluar pada antrian.

# Bagaimana Aplikasi Bekerja
Pada awal program, sebuah objek LinkedList dengan head kosong dan list riwayat kosong dibuat. Kemudian, program akan menampilkan pilihan menu, yaitu:

1.	Tambah antrian
2.	Tampilkan daftar antrian
3.	Panggil antrian
4.	Riwayat antrian
5.	Exit

  Jika pengguna memilih opsi "1", program akan meminta untuk memasukkan nama pendaftar. Nama pendaftar akan ditambahkan ke dalam linked list menggunakan fungsi tambahAkhir.
  
  Jika pengguna memilih opsi "2", program akan menampilkan semua nama pendaftar yang sedang menunggu di antrian. Hal ini Ini dilakukan dengan menggunakan fungsi printList.
  
  Jika pengguna memilih opsi "3", program akan menghapus data pertama dari linked list menggunakan fungsi hapusDepan. Kemudian program akan menampilkan daftar antrian yang terbaru dengan menggunakan fuingsi printList.
  
  Jika pengguna memilih opsi "4", program akan menampilkan riwayat semua peristiwa yang terjadi pada linked list. Ini mencakup setiap kali sebuah data ditambahkan ke dalam linked list atau dihapus dari linked list.
  
  Jika pengguna memilih opsi "5", program akan berhenti.
  
  Jika pengguna memilih opsi lain yang tidak valid, program akan menampilkan tulisan bahwa pilihan tidak tersedia dan meminta pengguna untuk memilih opsi yang valid.
 
# Output dan Penjelasan
![post test 3 1](https://user-images.githubusercontent.com/127474858/225945499-1d4d3578-5f9e-4708-bf0f-0c7347f13a79.jpeg)
![post test 3 2](https://user-images.githubusercontent.com/127474858/225945633-4c829d61-27e4-48b8-a524-7e2bb88839d7.jpeg)
![post test 3 3](https://user-images.githubusercontent.com/127474858/225945723-77346e14-d98e-4a81-a8a5-2c9e47f7a8f0.jpeg)

  Pada awalnya program akan menampilkan daftar menu yang tersedia. Kemudian, user memilih menu 1 yaitu untuk menambah data. Selanjunya, user memasukkan tiga data berupa nama pendaftar. Setelah itu, user memilih menu 2 dan program akan menampilkan daftar antrian yang telah masuk. Kemudian, user memilih menu 3 yaitu panggil antrian dan program akan memanggil antrian dimulai dari data yang paling depan atau yang paling awal dimasukkan. Hal ini berarti data yang dipanggil akan dihapus dari daftar antrian. Selanjutnya, user memilih menu 4 dan program akan menampilkan riwayat data masuk dan data yang dihapus pada antrian. Terakhir, user memilih menu 5 sehingga program berhenti

# Elemen Penting yang Digunakan
  Linked list digunakan untuk menyimpan data pengunjung dalam bentuk node-node yang terhubung secara berurutan. Setiap node terdiri dari sebuah data (nama pengunjung) dan sebuah pointer yang menunjuk ke node berikutnya.
  
  Kelas Node memiliki dua atribut, yaitu data dan next. Atribut data menyimpan data pendaftar  dalam bentuk string, sedangkan atribut next adalah pointer yang menunjuk ke node berikutnya.
  
  Kelas LinkedList digunakan untuk membuat linked list dan mengimplementasikan menu tambah elemen di akhir linked list (tambahAkhir()), hapus elemen di depan linked list (hapusDepan()), dan cetak linked list (printList()), dan menyimpan riwayat kejadian pada linked list dalam atribut history. Program berjalan secara terus menerus sampai pengguna memilih opsi keluar (Exit).
