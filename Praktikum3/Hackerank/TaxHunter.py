# Nama File: TaxCollector.py
# Nama / NIM: Muhammad Nauval Fadli
# Tanggal: 5 Maret 2026



# Rohsani adalah seorang pekerja biasa yang hari ini dilantik menjadi Direktur Keuangan di perkantorannya sebagai pemenang utama dalam giveaway yang diadakan di suatu instansi. Saat menikmati jabatan barunya, ia tersadar ada dokumen rincian gaji karyawan di atas mejanya. Merasa gajinya kurang untuk menghidupi biaya hidupnya yang baru, ia menerapkan kebijakan pajak baru untuk setiap karyawan perusahaan. Diberikan sebuah fungsi TaxCollector(G, J) dengan masukan berupa gaji per jam G (real, G ≥ 0) dan jumlah jam kerja J (integer, J ≥ 0), hitunglah gaji akhir karyawan setelah dipotong pajak. Aturan pajak yang berlaku adalah: 
# 1. jika gaji per jam kurang dari 50rb/jam maka dikenakan pajak 15%; 
# 2. jika gaji per jam antara 50rb/jam hingga 150rb/jam maka dikenakan pajak 10%; 
# 3. jika gaji per jam antara 150rb/jam hingga 500rb/jam maka dikenakan pajak 5%; 
# 4. dan jika gaji per jam lebih dari 500rb/jam maka tidak dikenakan pajak (0%). Keluaran berupa nilai real dari gaji akhir setelah dipotong pajak.


def TaxCollector(G, J):
    if G >= 0:
        if G < 50: 
            return (G - (G * 0.15)) * J
        elif G >= 50 and G <= 150:
            return (G - (G * 0.1)) * J
        elif G > 150 and G <= 500:
            return (G - (G * 0.05)) * J
        else:
            return G * J
        
            
        
