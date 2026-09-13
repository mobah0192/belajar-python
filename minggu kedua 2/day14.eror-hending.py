try:
    angka = int(input("Angka: "))
except:
    print("Terjadi kesalahan")

try:
    angka = int(input("Angka: "))
except ValueError:
    print("Terjadi kesalahan")

try:
    angka = int(input("masukan angka:"))
    print(100 / angka)
except ValueError:
    print("Itu bukan angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")
    
    
try:
    file = open("data.txt","r")
    baca = file.read()
    print(baca)
except FileNotFoundError:
    print("File tidak ditemukan, silakan buat dulu filenya.")
    
try:
    print(10 / 0)
except ZeroDivisionError:
    print("mana bisa di bagi 0")

    
try:
    file = open("rahasia.txt","r")
    baca = file.read()
    print(baca)
except FileNotFoundError:
    print("File tidak ditemukan")
    
try:
    angka = int(input("Angka: "))
except:
    print("Terjadi kesalahan")