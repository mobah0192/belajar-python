Ringkasan Hari 27
1.ORDER BY kolom mengurutkan hasil dari kecil ke besar (ascending) secara bawaan.
2. BY kolom DESC mengurutkan dari besar ke kecil (descending).
3.LIMIT n membatasi hasil hanya menampilkan n baris pertama.
4. BY dan LIMIT bisa digabung untuk mengambil data "teratas"/"terbawah" (misalnya produk termahal, siswa nilai tertinggi).
5.COUNT(*) menghitung jumlah baris di tabel.
6.SUM(kolom) menjumlahkan semua nilai di kolom tertentu.
7.(kolom) menghitung rata-rata nilai di kolom tertentu.
8.cursor.fetchone() dipakai untuk mengambil satu hasil saja — cocok untuk fungsi agregasi yang menghasilkan satu angka.
9.WHERE bisa digabung dengan fungsi agregasi, misalnya menghitung jumlah data yang memenuhi syarat tertentu.
10.Fungsi agregasi dihitung langsung oleh database, jadi Python cuma menerima hasil akhirnya, tidak perlu menghitung manual dengan loop.