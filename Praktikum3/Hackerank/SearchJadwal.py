# Nama File: SearchJadwal.py
# Nama / NIM: Muhammad Nauval Fadli / 24060124120027
# Tanggal: 6 Maret 2026


# Sebagai mahasiswa Informatika sejati, Baygon ingin tahu mata kuliah apa yang sedang dijadwalkan pada hari tertentu di jam tertentu. Jadwal kuliah yang sudah ditentukan oleh departemen Baygon berkuliah adalah sebagai berikut:

# Senin 	13–15 	→ Dasar Pemrograman
# Selasa 	13–15 	→ Aljabar Linier
# Rabu 	    07–10 	→ Dasar Sistem
# Rabu 	1   5–16 	→ Bahasa Inggris I
# Kamis 	07–09 	→ Pancasila
# Kamis 	13–15 	→ Matematika I
# Jumat 	07–09 	→ Bahasa Indonesia
# Jumat 	13–16 	→ Struktur Diskrit
# Jika ada, keluarkan string Nama Matkul (sesuai dengan diatas), jika tidak ada maka keluarkan "Tidak ada". Apabila ada lebih dari satu dalam interval yang diberikan, pisahkan mata kuliah dengan &. Misal, "Bahasa Indonesia & Struktur Diskrit"

# Input Format

# SearchJadwal(hari, awal, akhir)
# Constraints

# hari	: "sen"|"sel"|"rab"|"kam"|"jum"|"sab"|"min"
# awal	: integer
# akhir	: integer
# dimana , dan tidak ada kondisi multi-hari.

# Output Format

# [Mata Kuliah] | "Tidak ada"
# Sample Input 0

# SearchJadwal("sen", 12, 14)
# Sample Output 0

# Dasar Pemrograman
# Explanation 0

# Di interval 12-14, Baygon ada mata kuliah Dasar Pemrograman pada pukul 13-15.

# Sample Input 1

# SearchJadwal("jum", 8, 16)
# Sample Output 1

# Bahasa Indonesia & Struktur Diskrit
# Explanation 1

# Baygon memiliki jadwal Bahasa Indonesia dan Struktur Diskrit pada rentang jam 8 sampai 16.

def SearchJadwal(hari, awal, akhir):
    if hari == "sen":
    
        if awal < 15 and akhir > 13:
            return "Dasar Pemrograman"
        else:
            return "Tidak ada"
            
    elif hari == "sel":
     
        if awal < 15 and akhir > 13:
            return "Aljabar Linier"
        else:
            return "Tidak ada"
            
    elif hari == "rab":
        
        ds = awal < 10 and akhir > 7
        bing = awal < 16 and akhir > 15
        
        if ds and bing:
            return "Dasar Sistem & Bahasa Inggris I"
        elif ds:
            return "Dasar Sistem"
        elif bing:
            return "Bahasa Inggris I"
        else:
            return "Tidak ada"
            
    elif hari == "kam":
        
        pancasila = awal < 9 and akhir > 7
        mtk = awal < 15 and akhir > 13
        
        if pancasila and mtk:
            return "Pancasila & Matematika I"
        elif pancasila:
            return "Pancasila"
        elif mtk:
            return "Matematika I"
        else:
            return "Tidak ada"
            
    elif hari == "jum":
        
        bindo = awal < 9 and akhir > 7
        strukdat = awal < 16 and akhir > 13
        
        if bindo and strukdat:
            return "Bahasa Indonesia & Struktur Diskrit"
        elif bindo:
            return "Bahasa Indonesia"
        elif strukdat:
            return "Struktur Diskrit"
        else:
            return "Tidak ada"
            
    else: 
        return "Tidak ada"


