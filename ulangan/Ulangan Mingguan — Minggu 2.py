try:
    angka = int(input("masukan angka:"))
    angka2 = int(input("masukan angka:"))
    print(angka / angka2)
except ValueError:
    print("Itu bukan angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")






file = open("catatan_ulangan.txt","w")
file.write("halo ini gilang")
file.write("\n""ini catatan satu")
file.write("\n")
file.write("ini catatan dua")
file.write("\n")
file.write("ini catatan tiga")
file.close()

file = open("catatan_ulangan.txt","r")
lihat = file.read()
print(lihat)
file.close()





mobil = {
    "merk" : "suzuki",
    "tahun" : 2026,
    "warna" : "merah"
}
print(mobil)
print(mobil["merk"])
print(mobil["tahun"])

belanja = ["meja" ,"maouse","monitor","keyboard"]
for b in belanja:
    print("barang :",b)
    
    
    
kalimat = "pagi pagi beli makan beli mimum pergi sekolah"

print(kalimat)
print(kalimat.upper())
print(kalimat.lower())
print(kalimat.title())