# NIM       : 19623261
# Nama      : Azfa radhiyya Hakim
# Tanggal   : 23 Oktober 2023
# Deskripsi : Menentukan jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil

# Kamus:
# kiriatas,kananatas,kiribawah,kananbawah : fungsi
# m,n,max : int
# matriks : list
# cek : boolean

# Algoritma

# Fungsi

# Jika bilangan ganjil berada pada kiri atas matriks 2x2
def kiriatas(matriks,i,j): 
    sum = 0
    if i < m-1 and j < n-1:
        sum = matriks[i][j] + matriks[i][j+1] + matriks[i+1][j] + matriks[i+1][j+1]
    return sum

# Jika bilangan ganjil berada pada kanan atas matriks 2x2
def kananatas(matriks,i,j):
    sum = 0
    if i < m-1 and j > 0:
        sum = matriks[i][j-1] + matriks[i][j] + matriks[i+1][j-1] + matriks[i+1][j]
    return sum

# Jika bilangan ganjil berada pada kiri bawah matriks 2x2
def kiribawah(matriks,i,j):
    sum = 0
    if i > 0 and j < n-1:
        sum = matriks[i-1][j] + matriks[i-1][j+1] + matriks[i][j] + matriks[i][j+1]
    return sum

# Jika bilangan ganjil berada pada kana bawah matriks 2x2
def kananbawah(matriks,i,j):
    sum = 0
    if i > 0 and j > 0:
        sum = matriks[i-1][j-1] + matriks[i-1][j] + matriks[i][j-1] + matriks[i][j]
    return sum

# Input
m = int(input("Masukkan nilai m: ")) # Inisialisasi baris
n = int(input("Masukkan nilai n: ")) # Inisialisasi kolom

# Inisialisasi Matriks
matriks = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        matriks[i][j] = int(input(f'Masukkan elemen matriks baris {i+1} kolom {j+1}: '))

# Inisialisasi variabel
max = 0
cek = False

# Cek elemen ganjil
for i in range(m): # baris
    for j in range(n): # kolom
        if matriks[i][j] % 2 == 1: # jika ganjil
            cek = True
            # Mencari nilai maksimal
            if kiriatas(matriks,i,j) > max:
                max = kiriatas(matriks,i,j)
            if kananatas(matriks,i,j) > max:
                max = kananatas(matriks,i,j)
            if kiribawah(matriks,i,j) > max:
                max = kiribawah(matriks,i,j)
            if kananbawah(matriks,i,j) > max:
                max = kananbawah(matriks,i,j)
if cek:
    print(f"Jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil adalah {max}")
else:
    print("Tidak ada submatriks 2x2 yang memenuhi syarat")