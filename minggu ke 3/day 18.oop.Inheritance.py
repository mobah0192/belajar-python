class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama + " sedang makan")

class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama)
        self.ras = ras

    def menggonggong(self):
        print(self.nama + " menggonggong: Guk guk!")

anjing1 = Anjing("Rex", "Herder")
anjing1.makan()
anjing1.menggonggong()
print(anjing1.ras)



class Kendaraan:
    def __init__(self, merek):
        self.merek = merek

    def jalan(self):
        print(self.merek + " :sedang berjalan")

class Motor(Kendaraan):
    def __init__(self, merek):
        super().__init__(merek)

    def klakson(self):
        print(self.merek + " suara :tin tin")        
        

Kendaraan1 = Motor("supra")
Kendaraan1.jalan()
Kendaraan1.klakson()
print(Kendaraan1.merek)
        
        
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        

class Manager(Karyawan):
    def __init__(self, nama, gaji,divisi):
        super().__init__(nama, gaji)
        self.divisi = divisi
    
    def bonus(self,tambah):
        self.gaji = self.gaji  + tambah 
        
    def info(self):
        return f"nama: {self.nama}, gaji: Rp{self.gaji:,}, divisi: {self.divisi}"
    

Karyawan1 = Manager("gilang" , 3000000 , "backend")
Karyawan2 = Manager("bambang" , 3000000 , "forntend")
print(Karyawan1.info())
Karyawan1.bonus(1000000)
print(Karyawan1.info())
print(Karyawan2.info())


