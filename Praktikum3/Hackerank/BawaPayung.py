# Nama File: bawapayung.py
# Nama / NIM: Muhammad Nauval Fadli / 24060124120027
# Tanggal: 6 Maret 2026


# Fahri hendak pergi keluar kos dan harus menentukan apakah ia perlu membawa payung atau tidak. Ia mendapat informasi cuaca hari ini berupa suhu dan probabilitas hujan. Aturannya adalah: jika probabilitas hujan ≥ 50%, Fahri harus membawa payung; jika suhu > 35°C meskipun probabilitas hujan rendah, Fahri juga akan membawa payung untuk berteduh; jika tidak keduanya, Fahri tidak membawa payung. Diberikan sebuah fungsi BawaPayung(suhu, prob) dengan masukan berupa dua bilangan real yaitu suhu (0 ≤ T ≤ 100) dan probabilitas hujan (0 ≤ P ≤ 100), tentukan apakah Fahri perlu membawa payung atau tidak. Jika perlu, keluarkan "Bawa", jika tidak keluarkan "Tidak bawa".

def BawaPayung(suhu, prob):
    if prob >= 50 or suhu > 35:
        return "Bawa"
    else:
        return "Tidak bawa"
        

