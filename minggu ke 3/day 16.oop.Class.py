class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def cek_status(self):
        if self.nilai >= 75:
            return "Lulus"
        else:
            return "Tidak lulus"
        
        
siswa1 = Siswa("gilang", 90)
siswa2 = Siswa("Budi", 60)

print(siswa1.nama)
print(siswa1.cek_status())
print(siswa2.nama)
print(siswa2.cek_status())
print("--------siswa")


print("--------mobil")
class mobil :
    def __init__(self , merek ,warna):
        self.merek = merek
        self.warna = warna
        

mobil1 = mobil("lambord", "merah")
mobil2 = mobil("feraro" , "putih")


print(mobil1.merek)
print(mobil1.warna)
print(mobil2.merek)
print(mobil2.warna)
print("--------mobil")

class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        
    def info(self):        
        return "nama: " + self.nama + ", harga: " + self.harga + ", stok: " + self.stok
    

barang1 = Produk("sabun mandi" , "1000" ,"10")
barang2 = Produk("sampo" , "1000" ,"20")


print("--------print")
print(barang1.info())


print(barang2.info())
print("--------print")


class Hewan:
    def __init__(self, nama):
        self.nama = nama

kucing = Hewan("Miko")
print(kucing.nama)

class Orang:
    def __init__(self, umur):
        self.umur = umur
        
        
manusia = Orang(20)
print(manusia.umur)


class Buku:
    def __init__(self,judul):
        self.judul = judul
        
buku1 = Buku("koala kumal")
print(buku1.judul)