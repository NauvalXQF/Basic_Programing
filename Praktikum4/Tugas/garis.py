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
# A = makeTitik(2,7)
# B = makeTitik(10, 8)
# print(A)
# print(B)
# print(getAbsis(A))
# print(getAbsis(B))
# print(getOrdinat(A))
# print(getOrdinat(B))
# print(jarakTitik(A, B))
# print(kuadran(A))
# print(isEqualTitik(A, B))
# print(isOrigin(A))


type Garis = tuple[Titik, Titik]

# Konstruktor
def makeGaris(t1: Titik, t2: Titik) -> Garis:
    return (t1, t2)

# Selektor
def getTitikAwal(g: Garis) -> Titik:
    return g[0]

def getTitikAkhir(g: Garis) -> Titik:
    return g[1]

# Operator
def panjangGaris(g: Garis) -> float:
    t1 = getTitikAwal(g)
    t2 = getTitikAkhir(g)

    return jarakTitik(t1, t2)

def gradien(g: Garis) -> float:
    t1 = getTitikAwal(g)
    t2 = getTitikAkhir(g)

    p = getAbsis(t1)
    q = getOrdinat(t1)
    r = getAbsis(t2)
    s = getOrdinat(t2)

    m = (s - q) / (r - p)
    return m

# Predikat
def isSejajar(g1: Garis, g2: Garis) -> bool:
    return (gradien(g1) == (gradien(g2)))

# Aplikasi
A = makeGaris(makeTitik(2,4), makeTitik(8,3))
B = makeGaris(makeTitik(2,3), makeTitik(7,10))
print(panjangGaris(A))
print(gradien(A))
print(isSejajar(A, B))
    