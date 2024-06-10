# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 5 Oktober 2023
# Deskripsi: Menentukan hasil penjumlahan bilangan yang habis dibagi oleh x dan y

# Kamus:
# a, b, x, y, sum: int

# Algoritma:

# Input:
a = int(input("Masukkan nilai A: ")) # Inisialisasi
b = int(input("Masukkan nilai B: ")) # Inisialisasi
x = int(input("Masukkan nilai x: ")) # Inisialisasi
y = int(input("Masukkan nilai y: ")) # Inisialisasi

# Proses:
sum = 0 # Inisialisasi

for i in range(a,b+1): # Untuk semua bilangan di dalam interval a dan b inklusif
    if i % x == 0 and i % y == 0: # Jika i habis dibagi x dan y
        sum += i # Variabel sum ditambahkan i
print(f"Jumlah bilangan yang habis dibagi oleh {x} dan {y} adalah {sum}")