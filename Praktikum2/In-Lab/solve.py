# Nama: Muhammad Nauval Fadli
# NIM: 24060124120027
# Deskripsi: Tugas Ekspresi Fungsional Praktikum 2

# ==========================================
# TUGAS WAJIB
# ==========================================

# 1. APAKAH HURUF A?
def is_huruf_a(karakter: str) -> bool:
    # """
    # Menerima satu parameter karakter dan mengeluarkan nilai True (benar) 
    # jika karakter tersebut merupakan huruf 'A', dan False jika bukan[cite: 303, 304].
    # """
    # pass
    return karakter == 'A'
print(is_huruf_a('A'))
print(is_huruf_a('b'))


# 2. APAKAH POSITIF?
def is_positif(bilangan: int) -> bool:
    # """
    # Menerima satu parameter bilangan bulat dan mengeluarkan nilai True (benar) 
    # jika bilangan tersebut bernilai positif dan bukan nol[cite: 305, 306].
    # """
    # pass
    return bilangan > 0
print(is_positif(9))
print(is_positif(0))


# 3. MODIFIED LEAST SQUARE
def jarak_origin(x: float, y: float) -> float:
    # """
    # Menerima dua parameter bilangan riil x dan y, dan mengeluarkan 
    # jarak titik tersebut dari titik origin (0,0)[cite: 307, 308].
    # """
    # pass
    return ((x**2 + y**2))**0.5 #sebenrnya bisa buat fungsi tambhan untuk x^2 dan sqrt

print(jarak_origin(2.1, 3.0))


