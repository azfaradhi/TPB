# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 2 November 2023
# Deskripsi: Mengurutkan tinggi botol dengan bagian luar adalh botol dengan tinggi yang lebih kecil

# Kamus:
# a,b,k,x,y,p: int
# urutantinggi,tinggibotol: list

# Algoritma:

# Input:

a = int(input("Masukkan panjang meja: "))
b = int(input("Masukkan lebar meja: "))

# Inisialisasi
tinggibotol = [0 for i in range(a*b)]
for i in range(a*b):
    tinggibotol[i] = int(input(f"Masukkan tinggi botol ke-{i+1}: "))

# Mengurutkan tinggi botol
for i in range(a*b):
    for j in range(a*b-1):
        if tinggibotol[j] < tinggibotol[j+1]:
            tinggibotol[j],tinggibotol[j+1] = tinggibotol[j+1],tinggibotol[j]

urutantinggi = [[0 for i in range(a)] for i in range(b)]

# Proses pengurutan botol
k = 0
x = b//2
y = a//2
p = 1
while x >= 0 and y >= 0:
    if x == 0 and y == 0:
        for i in range(b-1,-1,-1):
            for j in range(a-1,-1,-1):
                if urutantinggi[i][j] == 0:
                    urutantinggi[i][j] = tinggibotol[k]
                    k += 1
        x -= 1
        y -= 1
    elif x == 0:
        for j in range(y,y+p):
            if urutantinggi[1][j] == 0:
                urutantinggi[1][j] = tinggibotol[k]
                k += 1
        p += 2
        y -= 1
    elif y == 0:
        for i in range(x,x+p):
            if urutantinggi[i][1] == 0:
                urutantinggi[i][1] = tinggibotol[k]
                k += 1
        p += 2
        x -= 1
    else:
        for i in range(x,x+p):
            for j in range(y,y+p):
                urutantinggi[i][j] = tinggibotol[k]
                k += 1
        p += 2
        x -= 1
        y -= 1

for i in range(b):
    for j in range(a):
        print(urutantinggi[i][j], end=" ")
    print()