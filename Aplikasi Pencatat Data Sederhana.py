def tampilan_menu():
    print("=== APLIKASI PENCATAT NILAI SISWA ===")
    print("1. Tambah siswa")
    print("2. Lihat semua siswa")
    print("3. Simpan ke file")
    print("4. Keluar")
    
def menu(pilih):
    if pilih == 1:
        print("Kamu memilih menu Tambah Siswa")
        tambah_siswa()
    elif pilih == 2:
        print("Kamu memilih menu Lihat Semua Siswa")
        lihat_siswa()
    elif pilih == 3:
        print("Kamu memilih menu Simpan ke File")
        simpan()
    elif pilih == 4:
        print("Program selesai")
    else:
        print("Menu tidak tersedia")
        

data_siswa = []

def tambah_siswa():
    nama = input("masukan nama siswa:")
    try :
        nilai = int(input("masukan nilai siswa:"))
        siswa = { "nama" : nama ,"nilai" : nilai }
        data_siswa.append(siswa)
        print("Data berhasil ditambahkan!")
    except ValueError:
        print("Itu bukan angka!")
            
        
        
def lihat_siswa():
    for siswa in data_siswa:
        nilai_siswa = siswa["nilai"]
        if nilai_siswa >= 75:
            print(siswa["nama"],"-", siswa["nilai"],"lulus")
        else:
            print(siswa["nama"],"-", siswa["nilai"],"belum lulus")

def simpan():
    file = open("catatan_siswa.txt","w")
    for n in data_siswa:
        nama_siswa = n["nama"]
        nilai_siswa = n["nilai"]
        file.write(str(nama_siswa))
        file.write(" - ")
        file.write(str(nilai_siswa))
        nilai_siswa = n["nilai"]
        file.write(" - ")
        if nilai_siswa >= 75:
            file.write("lulus")
        else:
            file.write("belum lulus")
            
        file.write("\n")
    file.close()
    
    
    file = open("catatan_siswa.txt","r")
    lihat = file.read()
    print(lihat)
    file.close()
    
lanjut = True

while lanjut == True:
    try :
        tampilan_menu()
        pilih = int(input("masukan pilihan:"))
        menu(pilih)
    
        if pilih == 4:
            lanjut = False
    except ValueError:
        print("Itu bukan angka!")
        