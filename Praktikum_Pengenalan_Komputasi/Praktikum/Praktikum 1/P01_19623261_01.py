# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 21 September 2023
# Deskripsi: Program menentukan nilai total hambatan yang disusun Tuan Kil

# Kamus:
# r1,r2,r3,rt : float

# Algoritma

# Input

r1 = float(input("Masukkan nilai resistor pertama: "))
r2 = float(input("Masukkan nilai resistor kedua: "))
r3 = float(input("Masukkan nilai resistor ketiga: "))

# Proses

if r1>0 and r2>0 and r3>0: # Cek kondisi apakah ketiga hambatan lebih besar dari 0.
    rt = 1/((1/r1)+(1/r2)+(1/r3)) # Menghitung total hambatan
    print(f"Total hambatan rangkaian adalah {rt} ohm")
else:
    print("Tidak dapat menghitung hambatan")