# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 19 Oktober 2023
# Deskripsi: Menentukan batas pandang belakang Tuan Leo

# Kamus:
# n: int
# tinggi_petak, batas_pandang : list
# output : str
# cek : boolean
# Algoritma:

# Input:
n = int(input("Masukkan nilai N: ")) # Inisialisasi
tinggi_petak = [0 for i in range(n)] # Inisialisasi
for i in range(n):
    tinggi_petak[i] = int(input(f"Tinggi petak ke-{i+1}: ")) # Inisialisasi

# Proses
batas_pandang = [0 for i in range(n)] # Inisialisasi

# Menghitung batas pandang dibelakang tinggi petak ke i+1
for i in range(n):
    if i == 0:
        batas_pandang[i] = 0
    else:
        count = 0
        j = i-1
        cek = True
        while cek and j >= 0:
            if tinggi_petak[j] <= tinggi_petak[i]:
                count += 1
                j -= 1
            else:
                cek = False
        batas_pandang[i] = count

output = "Batas pandang belakang bernilai " # Inisialisasi
for i in range(n):
    if i == n-1:
        output += str(batas_pandang[i])  
    else:
        output += str(batas_pandang[i])
        output += "-"
print(output)