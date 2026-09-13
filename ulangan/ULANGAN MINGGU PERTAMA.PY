def hitung(angka1,angka2):
    hasil = angka1 + angka2
    return hasil
a = int(input("masukan angka:"))
b = int(input("masukan angka:"))

hasil_akhir = hitung(a,b)
print("hasil:",hasil_akhir)
    


def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

angka = int(input("masukan angka:"))
print(cek_ganjil_genap(angka))


umur= int(input("masukan umur:"))
if umur >= 18:
    print("selamat kamu sudah dewasa")
else:
    print("maaf kamu belum cukup umur ")

a = 20
b = 10
hasil_tambah = a  + b 
hasil_kurang = a - b
hasil_kali = a * b
hasil_bagi = a / b
print(hasil_tambah)
print(hasil_kurang)
print(hasil_kali)
print(hasil_bagi)



nama = input("siapa nama kamu:")
kota = input("dari mana kota mu:")

print("hallo",nama ,"selamat datang" ,"oh kamu dari kota", kota)

def kali(a, b):
    return a * b

hasil = kali(4, 3)
print(hasil)


for i in range(3):
    print(i * 2 )
    
a = 5
b = "5"
print(a + a)

nama = "Budi"
print(nama)

print("5 + 5")

umur = input("masukan umur :")
print(umur)

print(10 + 10)

nilai = 70
if nilai >= 80:
	print("selamat kamu lulus")
else:
	print("maad kamu belum lulus")


for i in range(1,11):
	print(i)


def sapa(nama):
	print("halo" , nama)
sapa("budi")

