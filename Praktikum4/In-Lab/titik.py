# Nama / NIM: Muhammad Nauval Fadli / 24060124120027
# Tanggal: 10 Maret 2026    

type Titik = tuple[float, float]

#konstruktor
def makeTitik(x: float, y: float) -> Titik:
    return (x, y)

#selektor
def getAbsis(t: Titik) -> float:
    return t[0] #mengambil x

def getOrdinat(t: Titik) -> float:
    return t[1] #mengambil y

#operator

def jarakTitik(t1: Titik, t2: Titik) -> float:
    return (((getAbsis(t1) - getAbsis(t2))**2) + (((getOrdinat(t1) - getOrdinat(t2)) ** 2))) ** 0.5


def kuadran(t: Titik) -> int:
    x = getAbsis(t)
    y = getOrdinat(t)

    if x > 0 and y > 0: #kuadran 1
        return 1
    elif x < 0 and y > 0: #kuadran 2
        return 2
    elif x < 0 and y < 0: #kuadran 3
        return 3
    elif x > 0 and y < 0: #kadran 4
        return 4
    else:
        return 0 #origin (0,0)
    
#predikat
def isEqualTitik(t1: Titik, t2: Titik) -> bool:
    return (getAbsis(t1) == getAbsis(t2)) and (getOrdinat(t1) == getOrdinat(t2))

def isOrigin(t: Titik) -> bool:
    return (getOrdinat(t) == 0) and (getAbsis(t) == 0)



#aplikasi
A = makeTitik(2,7)
B = makeTitik(10, 8)
print(A)
print(B)
print(getAbsis(A))
print(getAbsis(B))
print(getOrdinat(A))
print(getOrdinat(B))
print(jarakTitik(A, B))
print(kuadran(A))
print(isEqualTitik(A, B))
print(isOrigin(A))
