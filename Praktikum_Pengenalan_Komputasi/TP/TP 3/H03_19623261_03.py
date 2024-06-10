# NIM/NAMA: 19623261/Azfa Radhiyya Hakim
# Tanggal: 9 Oktober 2023
# Deskripsi: Menentukan stasiun sebagai tempat memulai perjalanan dan banyak_stasiunnya stasiun yang Tuan Leo kunjungi 

# Kamus:
# uang,n,i,j,stasiun_awal,sum,count,selanjutnya,m : int
# harga_stasiun,banyak_stasiun,sort : list
# cek: boolean

# Algoritma

# Input
uang = int(input("Masukkan uang yang dibawa Tuan leo: ")) # Inisialisasi
n = int(input("Masukkan banyak stasiun: ")) # Inisialisasi

harga_stasiun = [0 for i in range(n)] # Inisialisasi
banyak_stasiun = [0 for i in range(n)] # Inisialisasi


# Proses

# Pengisian list 'harga_stasiun
for i in range(n):
    harga_stasiun[i] = int(input(f"Masukkan harga stasiun ke-{i+1}: "))

# Menghitung banyaknya stasiun yang dapat dikunjungi jika stasiun awalnya adalah 'stasiun_awal'
for stasiun_awal in range(n):
    sum = 0
    count = 0
    selanjutnya = stasiun_awal
    while sum <=uang and selanjutnya < stasiun_awal+n+1 and count <= n:
        temp = selanjutnya % n
        sum += harga_stasiun[temp]
        count += 1
        selanjutnya += 1
    banyak_stasiun[stasiun_awal] = count-1  

# Membuat list baru untuk mengurutkan list 'banyak_stasiun' secara menurun
sort = list(banyak_stasiun)

# Mengurutkan list 'sort' secara menurun
for i in range(n):
    for j in range(n-1):
        if sort[j] < sort[j+1]:
            sort[j],sort[j+1] = sort[j+1],sort[j]

# Pengecekan indeks
i = 0
cek = True
while i < n and cek:
    if banyak_stasiun[i] == sort[0]:
        m = i
        cek = False
    i += 1

# Output
if sort[0] == 0:
    print("Tuan Leo kehabisan uang.")
else:
    print(f"Tuan Leo dapat mengunjungi {sort[0]} stasiun dimulai dari stasiun ke-{m+1}.")