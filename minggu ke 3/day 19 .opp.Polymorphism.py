class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bunyi(self):
        print(self.nama + " mengeluarkan suara")

class Kucing(Hewan):
    def bunyi(self):
        print(self.nama + " berkata: Meong!")

class Anjing(Hewan):
    def bunyi(self):
        print(self.nama + " berkata: Guk guk!")

class Ayam(Hewan):
    def bunyi(self):
        print(self.nama + " berkata:kukuruyuk")
        
class sapi(Hewan):
    def bunyi(self):
        print(self.nama + " berkata:moooo")

kucing1 = Kucing("Miko")
anjing1 = Anjing("Rex")
ayam1 = Ayam("jeck")
sapi1 = sapi("agus")
kucing1.bunyi()
anjing1.bunyi()
ayam1.bunyi()
sapi1.bunyi()

print("----------------------")
daftar_hewan = [Kucing("Miko"), Anjing("Rex"), Ayam("jeck")]

for hewan in daftar_hewan:
    hewan.bunyi()
    
    
    
    
class Bentuk:
    def luas(self):
        print("Belum ada rumus luas")


class Persegi(Bentuk):
    def __init__(self, sisi):
        super().__init__()
        self.sisi = sisi

    def luas(self):
        hasil = self.sisi * self.sisi
        print("Luas persegi:", hasil)


class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        super().__init__()
        self.jari_jari = jari_jari

    def luas(self):
        hasil = 3.14 * self.jari_jari * self.jari_jari
        print("Luas lingkaran:", hasil)


Persegi1 = Persegi(100)
Lingkaran1 = Lingkaran(20)

Persegi1.luas()
Lingkaran1.luas()

hasil_gabungan = [Persegi(100),Lingkaran(20)]
for bentuk in hasil_gabungan:
    bentuk.luas()

class Hewan:
    def bunyi(self):
        print("Suara umum")

class Ayam(Hewan):
    def bunyi(self):
        print("Kukuruyuk")

a = Ayam()
a.bunyi()


