Ringkasan Hari 12

1.Dictionary menyimpan data sebagai pasangan key (label) dan value (isi), ditulis dengan { }.
2.Key dan value dipisahkan dengan titik dua :, contoh: "nama": "Gilang".
3. diakses menggunakan key, bukan nomor index seperti list, contoh: biodata["nama"].
4.Mengakses key yang tidak ada di dictionary akan menyebabkan error (KeyError).
5.data["key_baru"] = isi akan menambahkan key baru kalau belum ada, atau mengganti isinya kalau key itu sudah ada.
6. dan dictionary sama-sama pakai kurung kurawal { }, tapi set cuma berisi data tunggal, dictionary berisi pasangan key-value.
7.for key in dictionary: akan mengambil key-nya saja di setiap putaran, bukan value-nya langsung.
8.Untuk menampilkan value sekaligus, kita perlu dictionary[key] di dalam loop.
9.Setiap key dalam satu dictionary harus unik, tidak boleh ada dua key yang sama persis.
10.Dictionary cocok dipakai untuk data yang punya "label jelas", seperti biodata, data produk, dan sejenisnya — struktur ini akan sering banget kamu pakai nanti waktu belajar API dan backend.