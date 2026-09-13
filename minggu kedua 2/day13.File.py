file = open("biodara.txt", "w")
file.write("Halo, ini catatan pertamaku")
file.write("\n" "nama saya gilang ,hobi saya coding ,saya dari kota lubuklinggau")
file.close()

file = open("biodara.txt", "a")
file.write("\nIni baris tambahan")
file.close

file = open("biodara.txt" , "r")
baca = file.read()
print(baca)
file.close()



file = open("jurnal.txt","a")
text = input("masukan catatan:",)
file.write(text)
file.write("\n")
file.close()
file = open("jurnal.txt","r")
baca = file.read()
print(baca)

file = open("catatan.txt", "w")
file.write("Selamat belajar")
file.close()



