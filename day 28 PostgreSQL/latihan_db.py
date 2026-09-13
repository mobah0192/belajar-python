import psycopg2

koneksi = psycopg2.connect(
    host="localhost",
    database="latihan_db",
    user="postgres",
    password="Katasandi@123"
)

cursor = koneksi.cursor()
print("koneksi berhasil")

cursor.execute("CREATE TABLE IF NOT EXISTS produk (id SERIAL PRIMARY KEY, nama TEXT, harga INTEGER, stok INTEGER)")

cursor.execute("INSERT INTO produk (nama, harga, stok) VALUES ('sabun mandi', 1500, 100)")
cursor.execute("INSERT INTO produk (nama, harga, stok) VALUES ('sampo', 1000, 50)")
cursor.execute("INSERT INTO produk (nama, harga, stok) VALUES ('odol',  2500, 0)")

koneksi.commit()

cursor.execute("SELECT * FROM produk")
hasil = cursor.fetchall()
for baris in hasil:
    print(baris)

koneksi.close()
