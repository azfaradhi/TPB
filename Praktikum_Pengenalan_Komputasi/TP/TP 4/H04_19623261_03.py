# NIM       : 19623261
# Nama      : Azfa radhiyya Hakim
# Tanggal   : 23 Oktober 2023
# Deskripsi : Menghitung banyak kapal musuh yang ada bedasarkan peta matriks

# Kamus:
# horizontal,vertika,sendiri : fungsi
# n,m,k,kapalmusuh : int
# peta,a : list
# cekindeks,cekada : boolean

# Algoritma

# Fungsi

# Mencari banyak kapal musuh berbentuk horizontal
def horizontal(peta,i,p,m):
    if p > 1 and p < n-1:
            cekada = 2
    cekada = 0
    cek = True
    count = 0
    while cek and p < m:
        if peta[i][p] == "1":
            p += 1
            count += 1
        elif peta[i][p] == "0":
            cek = False
    if count > 1:
        cekada = 1
    return [p, cekada]

# Mencari banyak kapal musuh berbentuk vertikal
def vertikal(peta,j,p,n):
    cekada = 0
    cek = True
    count = 0
    while cek and p < n:
        if peta[p][j] == "1":
            p += 1
            count += 1
        elif peta[p][j] == "0":
            cek = False
    if count > 1:
        cekada = 1
    return [p, cekada]

# Mencari banyak kapal musuh yang tidak horizontal maupun vertikal (sendiri)
def sendiri(peta,i,j,m,n):
    sendirian = False
    if peta[i][j] == '1':
        if i == 0:
            if j == 0:
                if peta[i][j+1] == "0" and peta[i+1][j] == '0':
                    sendirian = True
            elif j == m-1:
                if peta[i][j-1] == "0" and peta[i+1][j] == '0':
                    sendirian = True
            else:
                if peta[i][j-1] == "0" and peta[i][j+1] == "0" and peta[i+1][j] == "0":
                    sendirian = True
        elif i == n-1:
            if j == 0:
                if peta[i-1][j] == "0" and peta[i][j+1] == '0':
                    sendirian = True
            elif j == m-1:
                if peta[i][j-1] == "0" and peta[i-1][j] == '0':
                    sendirian = True
            else:
                if peta[i][j-1] == "0" and peta[i][j+1] == "0" and peta[i-1][j] == "0":
                    sendirian = True
        else:
            if j == 0:
                if peta[i-1][j] == "0" and peta[i+1][j] == "0" and peta[i][j+1] == "0":
                    sendirian = True
            elif j == m-1:
                if peta[i-1][j] == "0" and peta[i+1][j] == "0" and peta[i][j-1] == "0":
                    sendirian = True
            else:
                if peta[i][j-1] == "0" and peta[i][j+1] == "0" and peta[i-1][j] == "0" and peta[i+1][j] == "0":
                    sendirian = True
    return sendirian

# Input               
n = int(input("Masukkan nilai N: "))
m = int(input("Masukkan nilak M: "))

# Inisialisasi matriks
peta = ["" for i in range(n)]

for i in range(n):
    peta[i] = input()

# Cek apakah matriks yang diberikan sesuai
cekindeks = True
for i in range(n):
    if len(peta[i]) != m:
        cekindeks = False
if cekindeks == False: 
    # Jika tidak sesuai, maka program tidak dapat dijalankan
    print("Matriks yang diinput salah, silahkan coba lagi!")
else:
    # Inisialisasi banyak kapal musuh
    kapalmusuh = 0

    # Banyak kapal musuh secara horizontal:
    for i in range(n):
        k = 0
        while k < n-1:
            a = horizontal(peta,i,k,m)
            print(a)
            k = a[0]
            cekada = a[1]
            if cekada == 1:
                kapalmusuh+=1
            k += 1

    # Banyak kapal musuh secara vertikal:
    for j in range(m):
        k = 0
        while k < m-1:
            a = vertikal(peta,j,k,n)
            k = a[0]
            cekada = a[1]
            if cekada == 1:
                kapalmusuh+=1
            k += 1

    # Banyak kapal musuh yang sendiri:
    for i in range(n):
        for j in range(m):
            if sendiri(peta,i,j,m,n):
                kapalmusuh += 1

    if kapalmusuh == 0:
        # Jika tidak ada kapal musuh
        print("Tidak terdapat kapal musuh pada peta")
    else:
        print(f'Terdapat {kapalmusuh} kapal musuh pada peta')