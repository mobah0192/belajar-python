Method	                    Artinya
assertEqual(a, b)	    Pastikan a sama dengan b
assertNotEqual(a, b)	Pastikan a tidak sama dengan b
assertTrue(x)	        Pastikan x bernilai benar (True)
assertFalse(x)	        Pastikan x bernilai salah (False)


Ringkasan Hari 

1.Testing otomatis mengecek apakah kode berjalan benar, tanpa perlu dicek manual satu-satu.
2.Module unittest adalah tool bawaan Python untuk testing.
3.Class testing harus mewarisi unittest.TestCase.
4.Nama function test harus diawali test_, supaya dikenali sebagai test yang harus dijalankan.
5.self.assertEqual(a, b) memastikan a sama dengan b — kalau cocok, test lolos; kalau tidak, test gagal.
6.Ada juga assertNotEqual, assertTrue, assertFalse untuk jenis pemeriksaan lain.
7.unittest.main() diperlukan untuk benar-benar menjalankan semua test yang ada di file itu.
8.Testing cuma mendeteksi kalau ada yang salah — tidak memperbaiki kode secara otomatis.
9.Manfaat utama testing: mendeteksi kalau perubahan kode di kemudian hari merusak sesuatu yang sebelumnya sudah benar.
10.Test yang lolos ditampilkan sebagai OK, yang gagal ditampilkan sebagai FAIL beserta detail perbedaan nilai yang diharapkan vs yang sebenarnya terjadi.