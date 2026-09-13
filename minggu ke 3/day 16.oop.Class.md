Ringkasan Hari 16


1.Class adalah "cetakan" untuk membuat object — menggabungkan data dan kemampuan (function) jadi satu paket.
2.Object adalah "barang jadi" hasil dari class — satu class bisa menghasilkan banyak object berbeda.
3.__init__ adalah function spesial yang otomatis dijalankan setiap kali object baru dibuat.
4.self wajib jadi parameter pertama di setiap function dalam class — merujuk ke object itu sendiri.
5.self.nama_data = nilai dipakai untuk menyimpan data supaya "menempel" pada object, bisa diakses lagi nanti.
6.Nama class biasanya ditulis dengan huruf besar di awal kata (contoh: Siswa, Mobil, Buku).
7.Object dibuat dengan cara nama_object = NamaClass(argumen) — ini otomatis memanggil __init__.
8.Data milik object diakses dengan titik: object.nama_data (mirip dictionary, tapi beda cara penulisan).
9.Function dalam class dipanggil dengan object.nama_function() — dan self di dalamnya otomatis merujuk ke object yang memanggil.
10.Lupa menulis self di function dalam class akan menyebabkan error waktu function itu dipanggil.