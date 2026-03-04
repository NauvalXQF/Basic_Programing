#Nama File : add.py
#Nama : Muhammad Nauval Fadli

#versi 1 lebih bagus untuk komputasi karena lebih cepat
def max2(a: int, b: int) ->  int:
    if a > b:
        return a
    else: 
        return b
    
#versi 2
def maks2(a: int, b: int) -> int:
    return ((a + b) + abs (a - b)) // 2
    
print(maks2(12,13))