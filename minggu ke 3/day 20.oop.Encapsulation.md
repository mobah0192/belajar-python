Ringkasan Hari 20


1.Encapsulation melindungi data supaya tidak diubah sembarangan dari luar class.
2.Data privat ditandai dengan dua garis bawah di depan namanya (self.__nama_data).
3.Data privat tidak bisa diakses langsung dari luar class (object.__data akan error).
4.Cara yang benar mengakses/mengubah data privat adalah lewat method yang disediakan class-nya (misalnya cek_saldo(), setor()).
5.Satu garis bawah (_nama) itu cuma konvensi/kebiasaan, bukan benar-benar terkunci — masih bisa diakses dari luar tanpa error.
6.Method yang jadi "pintu resmi" untuk mengubah data privat bisa punya aturan/validasi (contoh: cek saldo cukup sebelum menarik uang).
7.Tidak semua data harus dibuat privat — keputusan ini tergantung konteks, biasanya untuk data yang butuh perlindungan/validasi.
8.Encapsulation mencegah data jadi "rusak" karena diubah sembarangan tanpa lewat proses yang benar.
9.Data biasa (tanpa __) tetap bisa diakses langsung dari luar seperti biasa.
10.Encapsulation adalah pilar OOP terakhir dari 4 pilar utama: Class/Object (dasar), Inheritance (pewarisan), Polymorphism (banyak bentuk), dan Encapsulation (perlindungan data).