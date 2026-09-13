import sqlite3

koneksi = sqlite3.connect("siswa.db")
cursor = koneksi.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS nilai_ujian (id INTEGER PRIMARY KEY, nama TEXT, nilai INTEGER)")

cursor.execute("INSERT INTO nilai_ujian (nama, nilai) VALUES ('agus', 80)")
cursor.execute("INSERT INTO nilai_ujian (nama, nilai) VALUES ('toyep', 90)")
cursor.execute("INSERT INTO nilai_ujian (nama, nilai) VALUES ('bambang', 70)")
cursor.execute("INSERT INTO nilai_ujian (nama, nilai) VALUES ('siti',  60)")


cursor.execute("SELECT * FROM nilai_ujian")
hasil = cursor.fetchall()
for baris in hasil:
    print(baris)
    
cursor.execute("SELECT * FROM nilai_ujian ORDER BY nilai DESC LIMIT 4")
hasil = cursor.fetchall()
for baris in hasil:
    print(baris)



cursor.execute("SELECT AVG(nilai) FROM nilai_ujian")
print(cursor.fetchone())
    
koneksi.commit()
koneksi.close()