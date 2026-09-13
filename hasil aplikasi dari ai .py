data_siswa = []


def tampilkan_menu():
    print("=== APLIKASI PENCATAT NILAI SISWA ===")
    print("1. Tambah siswa")
    print("2. Lihat semua siswa")
    print("3. Simpan ke file")
    print("4. Keluar")


def cek_status(nilai):
    if nilai >= 75:
        return "lulus"
    else:
        return "belum lulus"


def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    try:
        nilai = int(input("Masukkan nilai siswa: "))
        siswa = {"nama": nama, "nilai": nilai}
        data_siswa.append(siswa)
        print("Data berhasil ditambahkan!")
    except ValueError:
        print("Itu bukan angka!")


def lihat_siswa():
    for siswa in data_siswa:
        status = cek_status(siswa["nilai"])
        print(siswa["nama"], "-", siswa["nilai"], "-", status)


def simpan():
    file = open("catatan_siswa.txt", "w")
    for siswa in data_siswa:
        status = cek_status(siswa["nilai"])
        file.write(siswa["nama"] + " - " + str(siswa["nilai"]) + " - " + status + "\n")
    file.close()

    file = open("catatan_siswa.txt", "r")
    print(file.read())
    file.close()


def menu(pilih):
    if pilih == 1:
        tambah_siswa()
    elif pilih == 2:
        lihat_siswa()
    elif pilih == 3:
        simpan()
    elif pilih == 4:
        print("Program selesai")
    else:
        print("Menu tidak tersedia")


lanjut = True

while lanjut:
    try:
        tampilkan_menu()
        pilih = int(input("Masukkan pilihan: "))
        menu(pilih)
        if pilih == 4:
            lanjut = False
    except ValueError:
        print("Itu bukan angka!")