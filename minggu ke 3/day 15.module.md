Ringkasan Hari 15

1.Module adalah cara memecah kode jadi beberapa file .py terpisah, supaya program besar tetap rapi.
2. nama_file (tanpa .py) dipakai untuk mengambil isi dari file lain.
3.Memanggil function dari module yang di-import penuh harus pakai format nama_module.nama_function(...).
4.from nama_module import nama_function memungkinkan kita memanggil function itu langsung, tanpa perlu menulis nama module-nya lagi.
5.Python juga punya banyak module bawaan siap pakai, contoh random untuk menghasilkan angka acak.
6.random.randint(1, 10) — kedua angka (awal dan akhir) ikut dihitung, beda dengan range().
7.while kondisi: mengulang selama kondisi masih benar — dipakai kalau jumlah pengulangan tidak diketahui pasti di awal.
8.break menghentikan loop secara paksa, walau syaratnya masih benar.
9.continue melompati sisa kode di satu putaran, langsung lanjut ke putaran berikutnya, tanpa keluar dari loop.
10.Kode yang tidak pernah dipanggil/dipakai (dead code) tidak menyebabkan error, tapi sebaiknya dibersihkan supaya program tetap rapi dan mudah dibaca.