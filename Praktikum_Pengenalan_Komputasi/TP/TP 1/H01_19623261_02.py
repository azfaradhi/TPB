# NIM/NAMA: 19623261/Azfa Radhiyya Hakim
# Tanggal: 14 September 2023
# Deskripsi: MENENTUKAN APAKAH GARIS TERSEBUT HORIZONTAL, VERTIKAL, ATAU BERGRADIEN

# KAMUS:
# x1 : float
# x2 : float
# x3 : float
# x4 : float
# m : float

# ALGORITMA

# INPUT
x1 = float(input("Masukkan nilai x1: "))
y1 = float(input("Masukkan nilai y1: "))
x2 = float(input("Masukkan nilai x2: "))
y2 = float(input("Masukkan nilai y2: "))

# PROSES

if x1 == x2:
    print("Garis tersebut merupakan garis vertikal")
else:
    m = (y2-y1)/(x2-x1)
    if m == 0:
        print("Garis tersebut merupakan garis horizontal")
    else:
        print("Garis tersebut memiliki gradien " + str(m))