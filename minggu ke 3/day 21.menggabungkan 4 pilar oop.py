class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.__gaji = gaji
        
    def lihat_gaji(self):
        print(f"nama: {self.nama}, gaji : Rp{self.__gaji:,}")
        
    def naik_gaji(self, jumlah):
        if jumlah > 0:
            self.__gaji = self.__gaji + jumlah
            print(f"nama: {self.nama}, gaji kamu naik: Rp{self.__gaji:,}")
        else:
            print("Jumlah kenaikan tidak valid!")
            
    def kerja(self):
        print(f"nama: " + self.nama , "sedang bekerja")
        
        
class Manager(Karyawan):
    def __init__(self, nama, gaji, divisi):
        super().__init__(nama , gaji)
        self.divisi = divisi
    
    def kerja(self):
        print(f"nama:" ,self.nama + " sedang memimpin divisi:" + self.divisi)
        
        
        
class Staff(Karyawan):  
    def kerja(self):
        print(f"nama: " + self.nama , "sedang mengerjakan tugas harian")
            


k1 = Karyawan("gilang" , 1000000)
k1.lihat_gaji()
k1.naik_gaji(500000)
k1.kerja()
print("===============================")
k2 = Karyawan("asep kopling" , 1000000)
k2.lihat_gaji()
k2.naik_gaji(200000)
k2.kerja()
print("===============================")
k3 = Karyawan("si imut" , 1000000)
k3.lihat_gaji()
k3.naik_gaji(-500)
k3.lihat_gaji()
k3.kerja()
print("===============================")
m1 = Manager("agus tampalban" , 1000000 , "backend")
m1.kerja()
m1.lihat_gaji()
m1.naik_gaji(2000000)
print("===============================")
m2 = Manager("rahmat karbu" , 1000000 , "frontend")
m2.kerja()
m2.lihat_gaji()
m2.naik_gaji(1000000)
print("===============================")
m3 = Manager("king nasir" , 1000000 , "frontend")
m3.kerja()
m3.lihat_gaji()
m3.naik_gaji(0)
print("===============================")
s1 = Staff("bambang member jmk" , 100000)
s1.kerja()
s2 = Staff("farhan kebab" , 100000)
s2.kerja()
s3 = Staff("rusdi simajuntak" , 100000)
s3.kerja()


total_orang = [k1,k2,
k3,
m1,
m2,
m3,
s1,
s2,
s3]

for t in total_orang:
    t.kerja()