warna = {"merah", "kuning" ,"hijau","kuning"}


warna.add("hitam")
warna.add("kuning")
warna.add("putih")
print(warna)

for w in warna:
    print(w)
    

hobi_saya = {
    "coding",
    "panjat tebing",
    "berenang ",
    "coli",
    
}

hobi_teman = {
    "coding",
    "lari",
    "berenang ",
    "sepeda",
}

hobi = hobi_saya & hobi_teman
print("hobi saya :",hobi_saya)
print("hobi temen saya :" ,hobi_teman)
print("jadi hobi kami:",hobi)

angka = {1, 1, 2, 2, 3}
print(angka)

buah = {"Apel", "Jeruk"}
buah.add("Apel")
print(len(buah))

angka_unik = {5, 5, 10, 10, 15}
print(angka_unik)