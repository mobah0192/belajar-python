import sqlite3

koneksi = sqlite3.connect("sekolah.db")
cursor = koneksi.cursor()

cursor.execute("SELECT * FROM siswa")
hasil = cursor.fetchall()

for baris in hasil:
    print(baris)



cursor.execute("SELECT * FROM siswa WHERE nilai >= 75")
hasil = cursor.fetchall()
for baris in hasil:
    print(baris)
    
koneksi.close()