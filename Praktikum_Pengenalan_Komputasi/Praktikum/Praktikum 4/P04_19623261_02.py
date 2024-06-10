# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 2 November 2023
# Deskripsi: Menentukan apakah bom pada Kota Kompeng akan meledak

# Kamus:
# n,xbom,ybom,xpenawar,ypenawar: int
# kota : matriks
# cekada: boolean


# Algoritma:

# Input
n = int(input("Masukkan ukuran kota: "))
xbom = int(input("Koordinat x bom: "))
ybom = int(input("Koordinat y bom: "))
xpenawar = int(input("Koordinat x penawar: "))
ypenawar = int(input("Koordinat y penawar: "))

# Inisialisasi
kota = [["." for j in range(n)] for i in range(n)]

# Letak bom
kota[ybom-1][xbom-1] = "B"

# Letak penawar
for i in range(n):
    kota[i][xpenawar-1] = "X"
for j in range(n):
    kota[ypenawar-1][j] = "X"

# Cek apakah bom meledak atau tidak
cekada = False
for i in range(n):
    for j in range(n):
        print(kota[i][j], end=" ")
        if kota[i][j] == "B":
            cekada = True
    print()

if cekada:
    print("Bom akan meledak.")
else:
    print("Bom tidak akan meledak.")