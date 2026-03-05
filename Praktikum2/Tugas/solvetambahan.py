# ==========================================
# TUGAS OPSIONAL (Poin Tambahan)
# ==========================================

def max2(a: int, b: int) ->  int:
    if a > b:
        return a
    else: 
        return b
    
def min2(a: int, b: int) ->  int:
    if a > b:
        return b
    else: 
        return a

# 4. MEAN OLYMPIQUE
def mean_olympique(a: int, b: int, c: int, d: int) -> float:
    # """
    # Menerima empat parameter bilangan bulat dan mengeluarkan rata-rata 
    # dari bilangan terkecil kedua dan terbesar kedua[cite: 314, 315].
    # """
    # pass

    return ((a + b + c + d) - (max2(max2(a,b), max2(c,d))) - (min2 (min2(a,b), min2(c,d)))) / 2
print(mean_olympique(4,9,12,6))


# 5. HITUNG NILAI AKHIR
def hitung_nilai_akhir(partisipatif: float, tugas: float, proyek: float, uts: float, uas: float) -> float:
#     # """
#     # Menerima lima parameter nilai dan mengeluarkan nilai akhir dari rata-rata 
#     # semua nilai tersebut berdasarkan bobot: 
#     # Aktivitas Partisipatif (10%), Tugas (20%), Proyek (40%), UTS (15%), UAS (15%)[cite: 316, 317, 319, 320, 321, 322, 325, 326, 327, 328, 331].
#     # """
#     # pass
    p = 0.1 * partisipatif
    q = 0.2 * tugas
    r = 0.4 * proyek
    s = 0.15 * uts
    t = 0.15 * uas
    
    return (p + q + r + s + t)
print(hitung_nilai_akhir(100,90,80,98,75))