class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def tambah_nilai(self, tambahan):
        self.nilai = self.nilai + tambahan

    def cek_status(self):
        if self.nilai >= 75:
            return "Lulus"
        else:
            return "Tidak lulus"

siswa1 = Siswa("Gilang", 70)
print(siswa1.nilai)

siswa1.tambah_nilai(10)
print(siswa1.nilai)
print(siswa1.cek_status())

class Produk:
    def __init__(self, nama, harga ,stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def kurangi_stok(self, jumlah):
        self.stok = self.stok - jumlah
    
    def ganti_harga(self, harga_baru):
        self.harga = harga_baru
        
        
    def info(self): 
        return "nama: " + self.nama + ", harga: " + str(self.harga) + ", stok: " + str(self.stok)

barang1 = Produk("sabun mandi" , 1000 , 100)
barang2 = Produk("sampo" ,2000 ,20)
print(barang1.info())    
print(barang1.info())
barang1.kurangi_stok(5)
barang1.ganti_harga(2000)
print(barang1.harga)
print(barang1.stok)
print(barang1.info())
print(barang2.info())


class Mobil:
    def __init__(self,merek , warna):
        self.merek = merek
        self.warna = warna
    
    def ganti_warna(self,baru):
        self.warna = baru
        



mobil1 = Mobil("Avanza", "Putih")
mobil2 = Mobil("Avanza", "Putih")
mobil1.ganti_warna("Hitam")
print(mobil1.warna)
print(mobil2.warna)


class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tambah_umur(self, tambahan):
        self.umur = self.umur + tambahan
kucing = Hewan("Miko", 2)
kucing.tambah_umur(3)
print(kucing.umur)