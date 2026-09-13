import sqlite3

koneksi = sqlite3.connect("sekolah.db")
cursor = koneksi.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS siswa (id INTEGER PRIMARY KEY, nama TEXT, nilai INTEGER)")

cursor.execute("INSERT INTO siswa (nama, nilai) VALUES ('Gilang', 90)")
cursor.execute("INSERT INTO siswa (nama, nilai) VALUES ('Budi', 60)")

cursor.execute("DELETE FROM siswa WHERE nama = Budi")
koneksi.commit()
koneksi.close()