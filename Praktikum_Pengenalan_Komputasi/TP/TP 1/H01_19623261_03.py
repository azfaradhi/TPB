# NIM/NAMA: 19623261/Azfa Radhiyya Hakim
# Tanggal: 14 September 2023
# Deskripsi: MENENTUKAN JENIS KURSI DAN HARGA KURSI TUAN KIL

# KAMUS:

# nomor : int
# kursi : string

# ALGORITMA

# INPUT

nomor = int(input("Tentukan Nomor Kursi: "))
kursi = input("Tentukan Posisi Kursi: ")

# PROSES

if (1<= nomor <= 100) and ((kursi == "A") or (kursi == "B") or (kursi =="C") or (kursi =="D") or (kursi =="E") or (kursi =="F")):
    if (1 <= nomor <= 20) or (51 <= nomor <= 60):
        if kursi == "A" or kursi == "F":
            print("Tuan Kil memilih kursi Hot Seat dengan harga 1600000")
        elif kursi == "B" or kursi == "E":
            print("Tuan Kil memilih kursi Hot Seat dengan harga 1550000")
        elif kursi == "C" or kursi == "D":
            print("Tuan Kil memilih kursi Hot Seat dengan harga 1500000")

    elif (21 <= nomor <= 50) or (61 <= nomor <= 100):
        if kursi == "A" or kursi == "F":
            print("Tuan Kil memilih kursi Regular dengan harga 1000000")
        elif kursi == "B" or kursi == "E":
            print("Tuan Kil memilih kursi Regular dengan harga 950000")
        elif kursi == "C" or kursi == "D":
            print("Tuan Kil memilih kursi Regular dengan harga 900000")
else:
    print("Input yang diberikan tidak valid")