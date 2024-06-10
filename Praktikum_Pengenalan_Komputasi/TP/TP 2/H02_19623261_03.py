# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal: 28 September 2023
# Deskripsi: Program menentukan apakah dapat mencapai N dengan input A dan B dengan ketentuan yang berlaku

# Kamus:
# a, b, n, temp1, temp2 : int
# cek1, cek2 : boolean

# Algoritma

# Input
a = int(input("Masukkan nilai A: ")) # Inisialisasi
b = int(input("Masukkan nilai B: ")) # Inisialisasi
n = int(input("Masukkan nilai N: ")) # Inisialisasi

# Proses

# Proses 1 (dikali mulai dari a)

# Variabel sementara 
cek1 = False # Inisialisasi
temp1 = 1 # Inisialisasi

while temp1 <= n: # Ketika nilai temp1 masih dibawah n
    temp1 *= a # temp1 dikali dengan a
    if temp1 == n: # Jika nilai temp1 sama dengan n
        cek1 = True # Boolean cek berubah menjadi True
    else: # Jika nilai temp1 belum sama dengan n
        temp1 *= b # temp1 dikali dengan b
        if temp1 == n: # Jika nilai temp1 sama dengan n
            cek1 = True # Boolean cek1 berubah menjadi True

# Proses 2 (dikali dimulai dari b)

# Variabel sementara
cek2 = False # Inisialisasi
temp2 = 1 # Inisialisasi
while temp2 <= n: # Ketika nilai temp2 masih dibawah n
    temp2 *= b # temp2 dikali dengan a
    if temp2 == n: # Jika nilai temp2 sama dengan n
        cek2 = True # Boolean cek2 berubah menjadi True
    else:  # Jika nilai temp2 belum sama dengan n
        temp2 *= a # temp2 dikali dengan a
        if temp2 == n: # Jika nilai temp2 sama dengan n
            cek2 = True # Bollean cek2 berubah menjadi True

if cek1 or cek2: # Jika cek1 atau cek2 True
    print(f"Bilangan {n} dapat dicapai.")
else: # Jika cek1 dan cek2 False
    print(f"Bilangan {n} tidak dapat dicapai.")