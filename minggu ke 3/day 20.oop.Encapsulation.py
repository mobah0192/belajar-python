class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo

    def cek_saldo(self):
        print("Saldo:", self.__saldo)

    def setor(self, jumlah):
        self.__saldo = self.__saldo + jumlah
        print("Setor berhasil. Saldo sekarang:", self.__saldo)

    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup!")
        else:
            self.__saldo = self.__saldo - jumlah
            print("Tarik berhasil. Saldo sekarang:", self.__saldo)

rekening1 = Rekening("Gilang", 100000)
rekening1.cek_saldo()
rekening1.setor(50000)
rekening1.tarik(30000)

class Siswa:
    def __init__(self, nama, nilai):
        self.__nama = nama
        self.__nilai = nilai
        
    def lihat_nilai(self):
        print("nilai:", self.__nilai)
        
    def ubah_nilai(self, nilai_baru):
        if  nilai_baru  >= 0 and nilai_baru <= 100:
            self.__nilai = nilai_baru
            print("nilai berhasil di ubah , nilai sekarang :" , self.__nilai) 
        else:
            print("Nilai tidak valid!" )
            
siswa1 = Siswa("Gilang" , 80)
siswa1.lihat_nilai()
siswa1.ubah_nilai(90)


class Password:
    def __init__(self,password):
        self.__password = password
        
    def cek_password(self, coba):
            if coba == self.__password:
                print("password benar")
            else:
                print("password salah") 

Password1 = Password("katasandi123")        
Password1.cek_password("katasandi123")


class Rekening:
    def __init__(self, saldo):
        self.__saldo = saldo
    def cek_saldo(self):
        print(self.__saldo)

r = Rekening(50000)
r.cek_saldo()
    