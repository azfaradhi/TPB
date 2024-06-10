# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 19 Oktober 2023
# Deskripsi: Menentukan apakah mobil tuan kil ditemukan atau tidak

# Kamus:
# plat : string
# jumlah_digit, banyak_digit : int
# cek1, cek2, cek3 : boolean
# Algoritma:

# Input:

plat = input("Masukkan nomor plat mobil: ") # Inisialisasi
jumlah_digit = int(input("Masukkan jumlah digit: ")) # Inisialisasi
banyak_digit = int(input("Masukkan banyak digit: ")) # Inisialisasi

# Proses

# cek plat huruf pertama
cek1 = False
if plat[0] == "D":
    cek1 = True

# cek banyak digit
cek2 = False
for i in range(1,banyak_digit+1):
    if int(plat[i]) == True:
        cek2 = True

# cek jumlah digit
cek3 = False
if cek2 == True:
    sum = 0
    for i in range(1, banyak_digit+1):
        sum += int(plat[i])
    if sum == jumlah_digit:
        cek3 = True

if cek1 and cek2 and cek3:
    print("Mobil Tuan Kil ditemukan!")
else:
    print("Bukan mobil Tuan Kil!")