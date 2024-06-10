# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 21 September 2023
# Deskripsi: Program menentukan menu yang dapat ditukar dengan poin yang dimiliki

# Kamus:
# tanggal_awal, poin, ramen, gyoza, ocha : int
# Algoritma

# Input
tanggal_awal = int(input("Tanggal awal makan di resto: "))

# Proses
if 1 <= tanggal_awal <= 30: # Cek batas input tanggal
    poin = 31 - tanggal_awal # Penghitungan poin
    ramen = poin//10 # Menghitung banyak ramen yang didapat
    gyoza = (poin-10*ramen)//5 # Menghitung banyak gyoza yang didapat
    ocha = (poin - 10*ramen - 5*gyoza)//2 # Menghitung banyak ocha yang didapat
    
    # Cek kasus beserta outputnya
    if ramen == 0 and gyoza == 0 and ocha == 0:
        print("Poin tidak cukup untuk ditukarkan.")
    elif ramen == 0 and gyoza == 0:
        print(f"Nona Deb mendapatkan {ocha} ocha.")
    elif ramen == 0 and ocha == 0:
        print(f"Nona Deb mendapatkan {gyoza} gyoza.")
    elif gyoza == 0 and ocha == 0:
        print(f"Nona Deb mendapatkan {ramen} ramen.")
    elif ramen == 0:
        print(f"Nona Deb mendapatkan {gyoza} gyoza, {ocha} ocha.")
    elif gyoza == 0:
        print(f"Nona Deb mendapatkan {ramen} ramen, {ocha} ocha.")
    elif ocha == 0:
        print(f"Nona Deb mendapatkan {ramen} ramen, {gyoza} gyoza.")
    else:
        print(f"Nona Deb mendapatkan {ramen} ramen, {gyoza} gyoza, {ocha} ocha.")
else:
    print("Masukkan tanggal diantara 1-30 inklusif")