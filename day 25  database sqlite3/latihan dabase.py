import sqlite3

koneksi = sqlite3.connect("toko.db")
cursor = koneksi.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS produk (id INTEGER PRIMARY KEY, nama TEXT, harga INTEGER, stok INTEGER)")

cursor.execute("INSERT INTO produk (nama, harga, stok) VALUES ('sabun mandi', 1500, 100)")
cursor.execute("INSERT INTO produk (nama, harga, stok) VALUES ('sampo', 1000, 50)")
cursor.execute("INSERT INTO produk (nama, harga, stok) VALUES ('odol',  2500, 0)")



cursor.execute("SELECT * FROM produk")
hasil = cursor.fetchall()

for baris in hasil:
    print(baris)


cursor.execute("SELECT * FROM produk WHERE stok > 0")
hasil = cursor.fetchall()
for baris in hasil:
    print(baris)

cursor.execute("SELECT * FROM produk ORDER BY harga")
hasil = cursor.fetchall()
for baris in hasil:
    print(baris)
    
cursor.execute("SELECT * FROM produk ORDER BY stok DESC LIMIT 1")
hasil = cursor.fetchall()
for baris in hasil:
    print(baris)
    
cursor.execute("SELECT COUNT(*) FROM produk")
print(cursor.fetchone())

cursor.execute("SELECT SUM(stok) FROM produk")
print(cursor.fetchone())

koneksi.commit()
koneksi.close()