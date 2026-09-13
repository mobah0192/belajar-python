Ringkasan Hari 19

1.Polymorphism artinya method dengan nama sama bisa punya perilaku berbeda di tiap class turunan.
2.Menulis ulang method milik class induk di class turunan disebut override.
3.Method yang di-override tidak menghapus versi aslinya di class induk — versi asli tetap ada, cuma "ditimpa" untuk object dari class turunan.
4.Kalau class turunan tidak override sebuah method, Python akan otomatis memakai versi milik class induk.
5.Menulis method dengan nama berbeda dari class induk itu bukan override, tapi method baru/terpisah.
6.Satu list bisa berisi campuran object dari class-class turunan yang berbeda.
7. bisa memanggil method yang sama lewat satu loop, walau isi list-nya berbeda jenis class — Python otomatis memilih versi yang sesuai untuk masing-masing object.
8.Manfaat utama polymorphism: menghindari perlu menulis kondisi (if/elif) berbeda-beda untuk tiap jenis object.
9.Override berguna kalau class turunan butuh perilaku khusus yang beda dari versi umum milik induknya.
10. sering dipakai bersama inheritance — keduanya saling melengkapi.