
import siswa_functions

while True:
    siswa_functions.tampilkan_menu()

    pilih = int(input("Masukkan pilihan: "))

    if pilih == 1:
        siswa_functions.tambah_siswa()

    elif pilih == 2:
        siswa_functions.lihat_siswa()

    elif pilih == 3:
        siswa_functions.simpan()
        
    elif pilih == 4:
        print("program selesai")
        break

    else:
        print("Pilihan tidak valid.")