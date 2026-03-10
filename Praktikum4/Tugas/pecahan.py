# Nama / NIM: Muhammad Nauval Fadli / 24060124120027
# Tanggal: 10 Maret 2026    

type Pecahan = tuple[int, int]


#konstruktor
def makePecahan(pembilang: int, penyebut: int) -> Pecahan:
    return (pembilang, penyebut)

#selektor
def getPembilang(p: Pecahan) -> int:
    return p[0]

def getPenyebut(p: Pecahan) -> int:
    return p[1]

#Operator
def addPecahan(p1: Pecahan, p2: Pecahan) -> Pecahan:
    a = getPembilang(p1)
    b = getPenyebut(p1)
    c = getPembilang(p2)
    d = getPenyebut(p2)

    return makePecahan(((a * d) + (c * b)), (b * d))

def mulPecahan(p1: Pecahan, p2: Pecahan) -> Pecahan:
    a = getPembilang(p1)
    b = getPenyebut(p1)
    c = getPembilang(p2)
    d = getPenyebut(p2)

    return makePecahan((a * c), (b * d))

def isEqualPecahan(p1: Pecahan, p2: Pecahan) -> bool:
    a = getPembilang(p1)
    b = getPenyebut(p1)
    c = getPembilang(p2)
    d = getPenyebut(p2)

    return ((a * d) == (b * c))


p1 = makePecahan(1, 2)
p2 = makePecahan(2, 4)
print(addPecahan(p1, p2))
print(mulPecahan(p1, p2))
print(isEqualPecahan(p1, p2))
