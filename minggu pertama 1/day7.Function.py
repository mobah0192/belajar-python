def cek_ganjil_genap(angka):
    angka = 5 % 5
    return "Genap"



for i in range(10, 0, -1):
    print(i)

def cek_lulus(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak lulus"

nilai = int(input("Masukkan nilai: "))
status = cek_lulus(nilai)
print(status)


def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari

hasil = luas_lingkaran( 4 * 8)
print(hasil)
    



def sapa(nama):
    print("selamat datang," + nama)
sapa("gilang")

def x(a,b):
    print(a * b)
    return
x = 6 * 7
print(x)

def cek_lulus(nilai):
    if nilai >= 80:
        print("lulus")
        return
    else:
        print("belum lulus")
        return
        
nilai = int(input("masukan nilai:"))
cek_lulus(nilai)
        
def cek_lulus(nilai):
    if nilai >= 80:
        print("selamat kamu lulus")
    else:
        print("maaf kamu tidak lulus")
        return
nilai = int(input("masukan nilai:"))
cek_lulus(nilai)    
    
    
def s(n):
    for i in range(11):
        print("halo," , n , "selamat datang ")
        
n = input("nama kamu :")
s(n)
        
        
