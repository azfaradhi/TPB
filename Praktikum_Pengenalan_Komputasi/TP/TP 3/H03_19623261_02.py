# NIM/NAMA: 19623261/Azfa Radhiyya Hakim
# Tanggal: 9 Oktober 2023
# Deskripsi: Menentukan nilai terbesar ke N dari data yang dimasukkan

# Kamus:
# data, n, i, j: int
# bilangan: list

# Algoritma

# Input
data = int(input("Masukkan banyak data: ")) # Inisialisasi
n = int(input("Masukkan nilai N: ")) # Inisialisasi

bilangan = [0 for i in range(data)] # Inisialisasi

# Proses
for i in range(data):
    bilangan[i] = float(input(f"Masukkan data ke-{i+1}: ")) # Pengisian list 'bilangan'

for i in range(data):
    for j in range(data):
        if bilangan[j] < bilangan[j+1]: # Proses mengurutkan bilangan dari terbesar ke terkecil
            bilangan[j],bilangan[j+1] = bilangan[j+1],bilangan[j]

print(f"Nilai terbesar ke-{n} adalah {bilangan[n-1]}")
