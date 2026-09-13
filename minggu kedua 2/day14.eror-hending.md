Ringkasan Hari 14

1.try/except adalah "jaring pengaman" — menangkap error supaya program tidak langsung mati (crash).
2.Kode yang berpotensi error ditaruh di dalam try:.
3. terjadi error, Python "lompat" ke bagian except: yang cocok, bukan menghentikan program total.
4.except: polos (tanpa nama error) akan menangkap semua jenis error, apapun itu.
5.except NamaError: (misalnya ValueError, ZeroDivisionError, FileNotFoundError) menangkap jenis error tertentu saja, lebih spesifik dan informatif.
6.Kalau tidak ada error di try, bagian except tidak akan dijalankan — dilewati sepenuhnya.
7.try/except bisa punya beberapa except berbeda untuk menangani beberapa jenis error yang berbeda dalam satu blok kode.
8.try/except cuma menangkap error supaya program tetap jalan — bukan alat untuk memperbaiki kesalahan logika program.
9.ValueError sering muncul waktu int(...) gagal mengubah teks jadi angka.
10.ZeroDivisionError muncul waktu ada pembagian dengan angka 0; FileNotFoundError muncul waktu file yang dibuka tidak ditemukan.