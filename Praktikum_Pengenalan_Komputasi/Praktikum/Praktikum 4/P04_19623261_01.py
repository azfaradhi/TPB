# NIM: 19623261
# Nama: Azfa Radhiyya Hakim
# Tanggal 2 November 2023
# Deskripsi: Cek nilai diskriminan dan akar dari suatu persamaan kuadrat

# Kamus:
# a,b,c,d: input
# diskriminan: subprogram fungsi
# cekakr: subprogram prosedur
# Algoritma:

# Fungsi cek deskriminan
def diskriman(a,b,c):
    d = (b**2)-(4*a*c)
    return d

# Prosedur cek akar persamaan
def cekakar(d):
    if d > 0:
        return "Persamaan kuadrat memiliki akar berbeda"
    if d ==0 :
        return "Persamaan kuadrat memiliki akar kembar"
    if d < 0:
        return "Persamaan kuadrat tidak memilki akar real"

# Input
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

# Output
print(diskriman(a,b,c))
print(cekakar(diskriman(a,b,c)))