Ringkasan Hari 

1.Database = lemari arsip, tabel = laci di dalamnya, kolom = label laci, baris = satu data di dalam laci.
2.sqlite3.connect("nama.db") membuka/membuat koneksi ke database SQLite.
3.cursor.execute("...") menjalankan perintah SQL yang ditulis dalam bentuk teks.
4.CREATE TABLE IF NOT EXISTS nama_tabel (...) membuat tabel baru (kalau belum ada).
5. INTO tabel (kolom) VALUES (nilai) menambahkan data baru ke tabel.
6.SELECT * FROM tabel mengambil semua data dari tabel.
7.WHERE syarat menyaring data sesuai syarat tertentu, mirip if di Python.
8.cursor.fetchall() mengambil seluruh hasil SELECT, berbentuk list berisi tuple.
9.koneksi.commit() wajib dipanggil supaya perubahan data (INSERT, UPDATE, DELETE) tersimpan permanen.
10. di dalam perintah SQL harus dibungkus tanda kutip satu ('teks').