# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal: 5 Oktober 2023
# Deskripsi: Program membuat n bendera segitiga

# Kamus:
# n: int

# Algoritma:

# Input:
n = int(input("Masukkan nilai dari n: ")) # Inisialisasi

# Proses:
while n <=0:
    n = int(input("Masukkan nilai dari n: "))

for i in range (1,4*n+2): # Pengisian baris pertama
    print("*", end="")
print()
for i in range(1,4*n+2): # Pengisian baris kedua
    if i % 4 == 1: # Jika i dibagi 4 bersisa 1
        print(" ", end="")
    else: # Jika i dibagi 4 tidak bersisa 1
        print("*", end="")
print()
for i in range(1,4*n+2): # Pengisian baris ketiga
    if i % 4 == 3: # Jika i dibagi 4 bersisa 3
        print("*", end="")
    else: # Jika i dibagi 4 tidak bersisa 3
        print(" ", end="")