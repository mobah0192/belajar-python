Ringkasan Hari 

1.Method di dalam class bisa punya parameter tambahan selain self, ditulis setelah self.
2.Waktu memanggil method lewat object (obj.method(5)), kita tidak perlu menulis self manual — Python otomatis mengisinya.
3.self cuma ditulis manual waktu mendefinisikan method (def nama_method(self, parameter):).
4.Method bisa mengubah data yang menempel pada object-nya sendiri, dengan self.data = nilai_baru.
5.Setiap object dari class yang sama punya data yang terpisah/independen — mengubah data satu object tidak memengaruhi object lain.
6. nama data (attribute) dan nama method ditulis sama persis, data itu bisa "menimpa" method-nya — jadi method tidak berfungsi seperti yang diharapkan. Ini sama seperti 
larangan Hari 9 soal jangan pakai nama yang sama untuk hal berbeda.
7.Selalu pastikan method benar-benar mengubah data yang dimaksud (misalnya self.warna), bukan membuat data baru yang kebetulan mirip namanya.
8.Kesalahan seperti ini normal terjadi, bahkan pada programmer berpengalaman — yang penting adalah kemampuan menemukan dan memperbaikinya sendiri.
9.self.nilai = self.nilai + tambahan adalah pola umum untuk "mengubah nilai lama jadi nilai baru berdasarkan nilai sebelumnya".
10.OOP memungkinkan kita membungkus data dan kemampuan (method) dalam satu paket (object), dan setiap object bisa "berkembang"/berubah sendiri-sendiri lewat method-nya.