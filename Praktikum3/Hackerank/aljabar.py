# Nama File: aljabar.py
# Nama / NIM: Muhammad Nauval Fadli
# Tanggal: 6 maret 2026

# Diberikan sebuah fungsi Aljabar(a, b, c) dengan masukan berupa 3 buah koefisien bilangan bulat yaitu a, b, dan c yang membentuk persamaan kuadrat ax² + bx + c = 0. Tugas program adalah menghitung hasil pembagian antar akar-akar(x1, x2) persamaan kuadrat tersebut. Akar-akar yang sudah ditemukan harus dimutlakkan terlebih dahulu, lalu dibagi yang paling kecil dengan paling besar, sehingga rentang nilai keluaran selalu 0 ≤ output ≤ 1. Jika digit belakang terlalu panjang, maka dibulatkan ke 5 digit belakang saja menggunakan round(angka, x). Jika persamaan kuadrat bersifat imajiner, maka keluaran adalah -999. Program harus dibuat menggunakan Paradigma Fungsional, artinya tidak boleh ada memorisasi variabel di luar fungsi.

def max2(a: int, b: int):
    if a > b:
        return a
    else: 
        return b
    
def min2(a: int, b: int):
    if a > b:
        return b
    else: 
        return a  
    
def x2(x):
    return x * x
    
def Diskriminan(a, b, c):
    D = x2(b) - 4 * a * c
    
    return D

def Aljabar(a, b ,c):
    if Diskriminan(a, b, c) < 0:
        return -999
    else:
        x1 = (-b + (Diskriminan(a, b, c))**0.5) / (2 * a)
        x2 = (-b - (Diskriminan(a, b, c))**0.5) / (2 * a)
        
        mx1 = abs(x1)
        mx2 = abs(x2)
        
        mx11 = max2(mx1, mx2)
        mx22 = min2(mx1, mx2)
        
        hasil = mx22 / mx11
        
        Final = round(hasil, 5)
        
        return Final
            
print(Aljabar(2, -3, 22))
