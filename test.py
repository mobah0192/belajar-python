harga_barang = int(input("masukan harga barang:"))
jumlah_barang = int(input("masukan jumlah barang:"))

total = harga_barang * jumlah_barang


if total >= 100000:
    persentase = 10
    print("Mendapatkan diskon 10%") 
elif total >= 50000 and total < 100000:
    persentase = 5
    print("Mendapatkan diskon 5%")
elif total < 50000:
    persentase = 0
    print("Tidak mendapatkan diskon")

diskon = total * persentase / 100
Total_bayar = total - diskon
    
print("total harga:",total)
print("total diskon:",diskon)
print("total bayaran:",Total_bayar)