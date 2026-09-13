Mode	    Arti	Efek
"w"	        write	Menulis baru, menghapus isi lama kalau file sudah ada
"a"	        append	Menambahkan tulisan baru, tidak menghapus isi lama
"r"	        read	Membaca isi file (tidak bisa menulis)


Ringkasan Hari 13
1.File dipakai untuk menyimpan data secara permanen, supaya tidak hilang setelah program ditutup.
2.open("nama_file.txt", "mode") dipakai untuk membuka/membuat file.
3.Mode "w" (write) menulis baru, menghapus isi lama kalau file sudah ada isinya.
4.Mode "a" (append) menambahkan tulisan baru tanpa menghapus isi lama.
5.Mode "r" (read) dipakai untuk membaca isi file, tidak bisa menulis.
6..write(...) menulis teks ke file, .read() membaca seluruh isi file.
7..close() wajib dipanggil setelah selesai memakai file — dan harus pakai tanda kurung (), kalau tidak, method-nya tidak benar-benar terpanggil.
8.with open(...) as file: adalah cara yang lebih aman, karena otomatis menutup file tanpa perlu .close() manual.
9.Membaca file yang belum pernah dibuat akan menyebabkan error FileNotFoundError.
10."\n" dipakai untuk membuat baris baru di dalam teks yang ditulis ke file.