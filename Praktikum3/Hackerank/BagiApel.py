# Nama File: bagiapel.py
# Nama / NIM: Muhammad Nauval Fadli
# Tanggal: 6 Maret 2026


# Kokoro adalah elf berambut putih yang baik hati. Di suatu hari, dia mendapatkan n buah apel untuk dibagikan kepada temannya, Pecorine. Namun, Kokoro adalah elf yang tidak suka dengan bilangan ganjil, sehingga dia ingin membagi buah apel untuk dirinya sendiri dan Pecorine dalam jumlah genap. Diberikan sebuah fungsi bagiApel(n) dengan masukan berupa sebuah bilangan bulat n, tentukan apakah n buah apel dapat dibagi menjadi 2 bagian dimana keduanya bernilai genap. Jika bisa, keluarkan "Bisa", jika tidak keluarkan "Tidak".

def bagiApel(n):
    if (n >= 4) and (n % 2 == 0):
        return "Bisa"
    else: 
        return "Tidak"


