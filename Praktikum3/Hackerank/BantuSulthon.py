# Nama File: determine.py
# Nama / NIM: Muhammad Nauval Fadli /24060124120027
# Tanggal: 6 Maret 2026


# Sulthon duduk terdiam di kelas setelah semua orang meninggalkan ruangan, matanya tertuju pada sebuah kertas ancaman di atas mejanya. Kertas tersebut memintanya untuk menentukan apakah bilangan N termasuk dalam pola bilangan ..., 3, 5, 7, 11, 13, 17, ... atau tidak. Diberikan sebuah fungsi Determine(n) dengan masukan berupa bilangan bulat n (n ≥ 0), tentukan apakah n termasuk dalam pola bilangan tersebut. Jika iya, keluarkan "Ya", jika tidak keluarkan "Tidak".

def Determine(n):
    if n >= 0:
        if n % 2 == 1:
            return "Ya"
        else:
            return "Tidak"
    else:
        return "Tidak"

#JANGAN DIUBAH!
print(eval(input()))