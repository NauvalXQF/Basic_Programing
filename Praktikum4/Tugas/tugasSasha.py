nama = str(input("Masukkan Nama: "))
npwp = str(input("Masukkan Nomor NPWP: "))
jamKerja = float(input("Masukkan Jumlah Jam kerja: ")) #dalam satuan jam
tarifKerja = float(input("Masukkan Tarif per Jam: "))

jamKerjaNormal = 40.0 #jam

if (jamKerja <= jamKerjaNormal):
    jamNormal = jamKerja
    jamLembur = 0

else: 
    jamNormal = jamKerjaNormal
    jamLembur = jamKerja - jamKerjaNormal

# HITUNG UPAH
upahNormal = jamNormal * tarifKerja
upahLembur = jamLembur * (tarifKerja * 1.5)
totalUpah = upahNormal + upahLembur

# Aplikasi
print("\n -- RINCIAN GAJI PEGAWAI -- ")
print("Masukkan Nama Pegawai: " + nama)
print("Masukkan NPWP: " + npwp)
print("Total Jam Kerja Dalam Seminggu: " + str(jamKerja) + " jam")
print("Besar Upah per Jam: " + str(int(tarifKerja)))
print()
print("Rincian Jam Kerja Pegawai: " + str(jamNormal) + " jam normal + " + str(jamLembur) + " jam lembur")
print()
print("Upah Normal: Rp" + str(int(upahNormal)))
print("Upah Lembur: Rp" + str(int(upahLembur)))
print("--------------------------------")
print("Total Upah Mingguan: Rp" + str(int(totalUpah)))


