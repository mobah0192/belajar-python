import psycopg2

koneksi = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
     password="Katasandi@123"
)

cursor = koneksi.cursor()
print("koneksi berhasil")

cursor.execute("CREATE TABLE IF NOT EXISTS siswa (id SERIAL PRIMARY KEY, nama TEXT, nilai INTEGER)")

cursor.execute("INSERT INTO siswa (nama, nilai) VALUES ('Gilang', 90)")
cursor.execute("INSERT INTO siswa (nama, nilai) VALUES ('Budi', 60)")

koneksi.commit()

cursor.execute("SELECT * FROM siswa")
hasil = cursor.fetchall()
for baris in hasil:
    print(baris)

koneksi.close()
