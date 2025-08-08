""" 
Rumus Bunga Tunggal

m_akhir = m_awal + besar_bunga
besar_bunga = n * i * m_awal

m_akhir = m_awal * (1 + (n * i))

Rumus Bunga Majemuk
m_akhir = m_awal * (1 + i) ** n
"""

def hitung_bunga_tunggal():
    print("Mencari bagian apa?")
    print("1. Modal Akhir")
    print("2. Modal Awal")
    print("3. Persentase Bunga")
    print("4. Periode Waktu")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        m_awal = int(input("Modal awal: "))
        i = float(input("Persentase Bunga (50 untuk 50%): ")) / 100
        
        print("Periode dalam bentuk bulan/tahun?")
        print("1. Bulan")
        print("2. Tahun")
        usrinput = input("(Bulan/Tahun): ")
        if usrinput == "1":
            n = float(input("Periode Waktu (dalam bulan): ")) / 12
        else:
            n = float(input("Periode Waktu (dalam tahun): "))

        m_akhir = m_awal * (1 + (i * n))
        return f"Modal akhir sekitar Rp.{m_akhir:.2f}"
    elif pilihan == "2":
        m_akhir = int(input("Modal Akhir: "))
        i = float(input("Persentase Bunga (50 untuk 50%): ")) / 100
        
        print("Periode dalam bentuk bulan/tahun?")
        print("1. Bulan")
        print("2. Tahun")
        usrinput = input("(Bulan/Tahun): ")
        if usrinput == "1":
            n = float(input("Periode Waktu (dalam bulan): ")) / 12
        else:
            n = float(input("Periode Waktu (dalam tahun): "))

        m_awal = m_akhir / (1 + (i * n))
        return f"Modal awal sekitar Rp.{m_awal:.2f}"
    elif pilihan == "3":
        m_akhir = int(input("Modal Akhir: "))
        m_awal = int(input("Modal Awal: "))
        
        print("Periode dalam bentuk bulan/tahun?")
        print("1. Bulan")
        print("2. Tahun")
        usrinput = input("(Bulan/Tahun): ")
        if usrinput == "1":
            n = float(input("Periode Waktu (dalam bulan): ")) / 12
        else:
            n = float(input("Periode Waktu (dalam tahun): "))

        i = (m_akhir / m_awal - 1) / n
        return f"Persentase bunga sekitar {i:.2f}"
    elif pilihan == "4":
        m_akhir = int(input("Modal Akhir: "))
        m_awal = int(input("Modal Awal: "))
        i = float(input("Persentase Bunga (50 untuk 50%): "))

        n = (m_akhir / m_awal - 1) / i
        return f"Periode Waktu sekitar {n:.2f} tahun"
    
def hitung_bunga_majemuk():
    print("Mencari bagian apa?")
    print("1. Modal Akhir")
    print("2. Modal Awal")
    print("3. Persentase Bunga")
    print("4. Periode Waktu")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        m_awal = int(input("Modal Awal: "))
        i = float(input("Persentase Bunga: "))

        print("Periode dalam bentuk bulan/tahun?")
        print("1. Bulan")
        print("2. Tahun")
        usrinput = input("(Bulan/Tahun): ")
        if usrinput == "1":
            n = float(input("Periode Waktu (dalam bulan): ")) / 12
        else:
            n = float(input("Periode Waktu (dalam tahun): "))

        m_akhir = m_awal * (1 + i) ** n
        return m_akhir
    elif pilihan == "2":
        pass

hasil_bunga_tunggal = hitung_bunga_tunggal()
print(hasil_bunga_tunggal)