# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 28 September 2023
# Deskripsi: Program menentukan apakah N merupakan perpangkatan dari k

# Kamus:
# n,k : int
# temp : int
# cek : boolean

# Algoritma

# Input
n = int(input("Masukkan bilangan N: ")) # Inisialisasi
k = int(input("Masukkan nilai k: ")) # Inisialisasi
# Variabel sementara
cek = False #Inisialisasi
temp = n #Inisialisasi

# Proses
while temp >= 1:
    if temp == 1: # Cek apakah nilai dari temp adalah 1
        cek = True # Jika iya, maka cek berubah menjadi True
    temp /= k # temp dibagi dengan k

if cek == True: # Jika boolean cek adalah True
    print(f"{n} merupakan perpangkatan {k}")
else: # Jika boolean cek adalah False
    print(f"{n} bukan merupakan perpangkatan {k}")