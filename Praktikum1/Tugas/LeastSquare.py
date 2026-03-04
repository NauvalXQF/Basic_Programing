#Nama File : add.py
#Nama : Muhammad Nauval Fadli

def akar2(x):
    return x ** 0.5
def Pangkat2 (x: int) -> int:
    return x * x

def LeastSquare(x2: int, y2: int, x1: int, y1: int) -> int:
    return (akar2(Pangkat2(x2-x1) + Pangkat2(y2-y1)))

x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))

Hitung = LeastSquare(x1, x2, y1, y2)
print(Hitung)