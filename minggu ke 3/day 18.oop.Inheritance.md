Ringkasan Hari 18

1.Inheritance memungkinkan class baru (turunan) mewarisi semua kemampuan dari class lain (induk).
2.class B(A): artinya class B mewarisi dari class A.
3.Class turunan otomatis punya semua data dan method milik class induknya, tanpa perlu menulis ulang.
4.Class turunan bisa punya method tambahan yang tidak dimiliki class induk.
5.super().__init__(...) dipakai untuk memanggil __init__ milik class induk, supaya data dari induk tetap terisi dengan benar.
6. class turunan punya __init__ sendiri tanpa super().__init__(...), data milik induk (misalnya self.nama) tidak akan terisi, dan akan error waktu dipakai.
7. turunan bisa menambahkan data baru (misalnya self.ras, self.divisi) setelah memanggil super().
8.Lupa menulis (NamaClassInduk) membuat class turunan berdiri sendiri, tidak mewarisi apapun.
9. parameter di super().__init__(...) harus sesuai dengan urutan parameter __init__ milik class induknya.
10.Inheritance berguna untuk menghindari penulisan kode yang berulang antar class-class yang punya kesamaan sifat.