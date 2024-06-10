# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 21 September 2023
# Deskripsi: Program menentukan pilihan transportasi yang tepat bedasarkan jam keberangkatan dan kepulangannya

# Kamus:
# jam_pergi, jam_pulang, harga: float
# pergi, pulang : string

# Algoritma

# Input
jam_pergi = float(input("Jam keberangkatan Nona Deb: "))
jam_pulang = float(input("Jam kepulangan Nona Deb: "))

harga = 0 # Harga awal

# Proses
if 0 <= jam_pergi <= 24 and 0 <= jam_pulang <= 24: # Jam pergi dan pulang harus berada diantara 0 dan 24 inklusif
    
# Penentuan pilihan yang tepat untuk pergi

    if 6 <= jam_pergi <= 8:
        pergi = "Bus Univertas"
    elif 8 < jam_pergi <15:
        harga += 5000
        pergi = "Bus Kota"
    elif 15 <= jam_pergi <= 17:
        pergi = "Bus Universitas"
    elif 17 < jam_pergi <= 18:
        harga += 5000
        pergi = "Bus Kota"
    elif 18 < jam_pergi <= 24:
        harga += 10000
        pergi = "Travel"

# Penentuan pilihan yang tepat untuk pulang

    if 6 <= jam_pulang <= 8:
        pulang = "Bus Univertas"
    elif 8 < jam_pulang <15:
        harga += 5000
        pulang = "Bus Kota"
    elif 15 <= jam_pulang <= 17:
        pulang = "Bus Universitas"
    elif 17 < jam_pulang <= 18:
        harga += 5000
        pulang = "Bus Kota"
    elif 18 < jam_pulang <= 24:
        harga += 10000
        pulang = "Travel"
    print(f"Nona Deb berangkat naik {pergi} dan pulang naik {pulang} dengan total biaya {harga}.")
else:
    print("Mohon masukan jam dalam batas 0-24")
