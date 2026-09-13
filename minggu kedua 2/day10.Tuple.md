Ringkasan Hari 10

1.Tuple adalah "keranjang" yang mirip list, tapi isinya tidak bisa diubah setelah dibuat.
2.Tuple ditulis dengan tanda kurung biasa ( ), beda dengan list yang pakai kurung siku [ ].
3.Cara mengambil isi tuple sama seperti list — pakai index yang dimulai dari 0.
4.Mencoba mengubah isi tuple (tuple[0] = "baru") akan menyebabkan error: TypeError: 'tuple' object does not support item assignment.
5.Tuple tidak punya method seperti .append() atau .remove(), karena memang tidak dirancang untuk berubah.
6. "tidak bisa diubah" ini disebut immutable.
7.Tuple cocok dipakai untuk data yang memang seharusnya tetap, misalnya koordinat, tanggal lahir, atau kombinasi warna dasar.
8.Tuple juga bisa dipakai dengan for item in tuple:, sama seperti list.
9.Index yang dimulai dari 0 berlaku konsisten di string, list, tuple, dan range.
10.Pilih list kalau datamu perlu diubah-ubah, pilih tuple kalau datamu memang seharusnya tetap/dikunci.