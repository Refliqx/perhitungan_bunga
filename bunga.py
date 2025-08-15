"""

Rumus Bunga Tunggal
m_akhir = m_awal + besar_bunga
besar_bunga = n * i * m_awal
m_akhir = m_awal * (1 + (n * i))

Rumus Bunga Majemuk
m_akhir = m_awal * (1 + i) ** n

"""

def hitung_periode_waktu():
    print("Ingin mencari periode dalam bentuk apa?")
    print("1. Bulan")
    print("2. Tahun")
    pilihan = input("Pilih (1/2): ")
    if pilihan == "1":
        return float(input("Masukkan periode dalam bulan: ")) / 12
    else:
        return float(input("Masukkan periode dalam tahun: "))

def hitung_bunga_tunggal():
    print("Mencari bagian apa?")
    print("1. Modal Akhir")
    print("2. Modal Awal")
    print("3. Persentase Bunga")
    print("4. Periode Waktu")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        m_awal = float(input("Modal awal: "))
        i = float(input("Persentase Bunga (misal 10 untuk 10%): ")) / 100
        n = hitung_periode_waktu()
        m_akhir = m_awal * (1 + i * n)
        return f"Modal akhir sekitar Rp{m_akhir:.2f}"

    elif pilihan == "2":
        m_akhir = float(input("Modal akhir: "))
        i = float(input("Persentase Bunga (misal 10 untuk 10%): ")) / 100
        n = hitung_periode_waktu()
        m_awal = m_akhir / (1 + i * n)
        return f"Modal awal sekitar Rp{m_awal:.2f}"

    elif pilihan == "3":
        m_akhir = float(input("Modal akhir: "))
        m_awal = float(input("Modal awal: "))
        n = hitung_periode_waktu()
        i = (m_akhir / m_awal - 1) / n
        return f"Persentase bunga sekitar {i * 100:.2f}%"

    elif pilihan == "4":
        m_akhir = float(input("Modal akhir: "))
        m_awal = float(input("Modal awal: "))
        i = float(input("Persentase Bunga (misal 10 untuk 10%): ")) / 100
        n = (m_akhir / m_awal - 1) / i
        return f"Periode waktu sekitar {n:.2f} tahun"

    else:
        return "Pilihan tidak valid."

def hitung_bunga_majemuk():
    print("Mencari bagian apa?")
    print("1. Modal Akhir")
    print("2. Modal Awal")
    print("3. Persentase Bunga")
    print("4. Periode Waktu")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        m_awal = float(input("Modal awal: "))
        i = float(input("Persentase Bunga (misal 10 untuk 10%): ")) / 100
        n = hitung_periode_waktu()
        m_akhir = m_awal * (1 + i) ** n
        return f"Modal akhir sekitar Rp{m_akhir:.2f}"

    elif pilihan == "2":
        m_akhir = float(input("Modal akhir: "))
        i = float(input("Persentase Bunga (misal 10 untuk 10%): ")) / 100
        n = hitung_periode_waktu()
        m_awal = m_akhir / ((1 + i) ** n)
        return f"Modal awal sekitar Rp{m_awal:.2f}"

    elif pilihan == "3":
        m_akhir = float(input("Modal akhir: "))
        m_awal = float(input("Modal awal: "))
        n = hitung_periode_waktu()
        i = (m_akhir / m_awal) ** (1 / n) - 1
        return f"Persentase bunga sekitar {i * 100:.2f}%"

    elif pilihan == "4":
        m_akhir = float(input("Modal akhir: "))
        m_awal = float(input("Modal awal: "))
        i = float(input("Persentase Bunga (misal 10 untuk 10%): ")) / 100
        import math
        n = math.log(m_akhir / m_awal) / math.log(1 + i)
        return f"Periode waktu sekitar {n:.2f} tahun"

    else:
        return "Pilihan tidak valid."

while True:
    print("Ingin menghitung apa?")
    print("1. Bunga Tunggal")
    print("2. Bunga Majemuk")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        hasil = hitung_bunga_tunggal()
    elif pilihan == "2":
        hasil = hitung_bunga_majemuk()
    elif pilihan == "3":
        exit()
    else:
        print("Silahkan masukkan input yang benar. Antara 1 sampai 3")