# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 19 Oktober 2023
# Deskripsi: Mengubah pesan biasa menjadi sebuah pesan yang sudah dirahasiakan

# Kamus:
# kata, output: string
# panjang_kata: int
# kata2 = list
# selesai = boolean
# Algoritma:

# Input:
kata = input("Masukkan kata yang dirahasiakan: ") # Inisialisasi
panjang_kata = len(kata)
kata2 = [" " for i in range(panjang_kata)] # Inisialisasi

# Proses
for i in range(panjang_kata):
    if kata[i] == "*": # cek apakah string * atau ^
        selesai = False
        j = i-1
        mulai = 0
        # mencari titik mulai pergantian huruf
        while selesai == False and j >= 0:
            if kata[j] == "*" or kata[j] == "^":
                mulai = j+1
                selesai = True
            j -= 1
        # Proses pergantian huruf
        for k in range(mulai,i):
            kata2[k] = kata[mulai+i-k-1]
    if kata[i] == "^": # cek apakah string * atau ^
        selesai = False
        j = i-1
        mulai = 0
        # mencari titik mulai pergantian huruf
        while selesai == False and j >= 0:
            if kata[j] == "*" or kata[j] == "^":
                mulai = j+1
                selesai = True
            j -= 1
        # Proses pergantian huruf
        for k in range(mulai,i):
            if (i - mulai) % 2 == 1:
                if kata[k+1] != "^":
                    if k % 2 == 0:
                        kata2[k],kata2[k+1] = kata[k+1],kata[k]
                else:
                    kata2[k] = kata[k]
            else:
                if k % 2 == 0:
                    kata2[k],kata2[k+1] = kata[k+1],kata[k]

output = "" # Inisialisasi
for i in range(panjang_kata):
    output += kata2[i]
print(output)