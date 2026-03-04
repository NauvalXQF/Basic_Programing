#Nama File : add.py
#Nama : Muhammad Nauval Fadli

def Pangkat2 (x: int) -> int:
    return x * x

print(Pangkat2(7))

hasil = Pangkat2(10) #menggunakan variable, kemungkinan besar tidak boleh pada saat praktikum pertama

print(hasil)

def Pangkat3(x: int) -> int:
    return Pangkat2(x) * x

equal = Pangkat3(8) #using variable


print(equal)
print(Pangkat3(10))
