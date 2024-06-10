# NIM/NAMA: 19623261/Azfa Radhiyya Hakim
# Tanggal: 9 Oktober 2023
# Deskripsi: Menentukan nomor-nomor perwakilan yang tidak mendatangi acara

# Kamus:
# n,m,i,j: int
# listn, list: list
# output: str

# Algoritma

# Input
n = int(input("Masukkan nilai N: ")) #Inisialisasi
m = int(input("Masukkan nilai M: ")) #Inisialisasi

listn = [i+1 for i in range(n)] # Inisialisasi
listm = [0 for j in range(m)] # Inisialisasi

# Proses

for j in range(m):
    listm[j] = int(input(f"Masukkan data ke {j+1}: ")) # Pengisian list 'listm'

output = "Nomor perwakilan yang tidak datang: " # Output yang akan di print

for i in range(n):
    for j in range(m):
        if listn[i] == listm[j]: # Jika data yang diberikan termasuk didalam list
            listn[i] = 0 # Data dalam list tersebut diubah menjadi 0
for i in range(n):
    if listn[i] != 0: # Jika data bukan sama dengan 0
        a = listn[i]
        output += str(a) + " " # Print data tersebut
print(output)
