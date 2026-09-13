1.UPDATE tabel SET kolom = nilai WHERE syarat mengubah data yang sudah ada di baris yang cocok dengan syarat.
2.DELETE FROM tabel WHERE syarat menghapus baris yang cocok dengan syarat.
3.WHERE itu sangat penting di UPDATE/DELETE — tanpa itu, semua baris akan terkena aksi (diubah/dihapus semua).
4.DELETE ... WHERE yang tepat sasaran tidak memengaruhi baris lain yang tidak cocok dengan syaratnya.
5.koneksi.commit() tetap wajib dipanggil setelah UPDATE/DELETE, sama seperti INSERT.
6.Kebiasaan baik: cek dulu pakai SELECT dengan WHERE yang sama, sebelum benar-benar menjalankan UPDATE/DELETE.
7.Urutan UPDATE yang benar: UPDATE tabel SET kolom = nilai WHERE syarat.
8.Lupa WHERE pada UPDATE/DELETE adalah salah satu kesalahan paling berbahaya dalam SQL, bisa menyebabkan kehilangan data secara masal.
9.Urutan SET kolom = nilai tidak boleh dibalik jadi nilai = kolom.
10.UPDATE dan DELETE termasuk perintah SQL yang mengubah data secara permanen — perlu kehati-hatian ekstra dibanding SELECT yang cuma "membaca" tanpa mengubah apapun.