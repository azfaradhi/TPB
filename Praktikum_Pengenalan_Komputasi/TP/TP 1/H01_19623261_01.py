# NIM/NAMA: 19623261/Azfa Radhiyya Hakim
# Tanggal: 14 September 2023
# Deskripsi: PROGRAM MENENTUKAN APAKAH TUAN KIL LULUS ATAU TIDAK LULUS

# KAMUS:
# ujian_1, ujian_2, ujian_3, ujian_4, ratarata : int

# ALGORITMA:

# INPUT
ujian_1 = int(input("Masukkan nilai ujian 1: "))
ujian_2 = int(input("Masukkan nilai ujian 2: "))
ujian_3 = int(input("Masukkan nilai ujian 3: "))
ujian_4 = int(input("Masukkan nilai ujian 4: "))

# PROSES

# MENGHITUNG RATA-RATA 4 UJIAN
ratarata = (ujian_1 + ujian_2 + ujian_3 + ujian_4) / 4

# MENGECEK KELULUSAN TUAN KIL
if ujian_1 >= 50 and ujian_2 >= 50 and ujian_3 >= 50 and ujian_4>= 50:
    if ratarata >= 70:
        print("Tuan Kil lulus kelas Tuan Leo")
    else:
        print("Tuan Kil tidak lulus kelas Tuan Leo")
else:
    print("Tuan Kil tidak lulus kelas Tuan Leo")
