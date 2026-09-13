siswa = {
    "nama" : "gilang",
    "kelas" : "a3 TI",
    "nilai" : "90",
        }
print(siswa)
print(siswa["nama"])
print(siswa["nilai"])


siswa["umur"] = 20
print(siswa)
siswa["sekolah"] = "smk 1"


produk = {
    "nama_produk" : "sabun",
    "harga" : 1000,
    "stok" : 1
}
if produk["stok"] > 0:
    print("produk tersedia")
else:
    print("produk habis")
    
data = {"nama": "Budi"}
print(data["nama"])
data["umur"] = 20
print(data)

data = {
    "kota" : "kanjut"
}
data["kota"] = "bandung"
print(data)

hewan = {
    "nama" : "kucing",
    "suara" : "meong",
    "nama2" : "anjing",
    "suara2" : "gukguk"
}
print(hewan)
for s in hewan:
    print(s,":", hewan[s])