# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal:8 September 2023
# Deskripsi: Program membuat segitiga sama kaki dengan tinggi H

# Kamus:
# n,m : int

# Algoritma

# Input
n = int(input("Masukkan nilai H: ")) # Inisialisasi
# Variabel sementara
m = 1

# Proses
for i in range((n+1)//2): # Pendefinisian baris
    for j in range(i+1): # Pendefinisian kolom
        print(m, end = " ") # Print output berupa variabel m
        m += 1
    print()

for i in range((n+1)//2, n): # Pendefinisian baris
    for j in range(n-i): # Pendefinisian kolom
        print(m, end = " ") # Print output berupa variabel m
        m += 1
    print()