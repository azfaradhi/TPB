# NIM       : 19623261
# Nama      : Azfa radhiyya Hakim
# Tanggal   : 23 Oktober 2023
# Deskripsi : Menentukan banyak Bakteri Pengkombacter

# Kamus:
# banyakbakteri : fungsi
# n,k : int
# bakteri : list

# Algoritma

# Fungsi
def banyakbakteri(n,k):
    # bakteri[0]: banyak bakteri yang bereproduksi, bakteri[1]: banyak bakteri yang tidak bereproduksi
    bakteri = [n,0]
    for i in range(k):
        bakteri[1] += bakteri[0]
        bakteri[0] *= 2
    return bakteri[0] + bakteri[1]

# Input
n = int(input("Masukkan nilai N: "))
k = int(input("Masukkan nilai K: "))

print(f'Terdapat {banyakbakteri(n,k)} Bakteri Pengkombacter.')