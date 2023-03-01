class Mahasiswa:
    def __init__(self, Nama, NIM, Kelas_PBO, Jumlah_SKS):
        self.nama = Nama
        self.NIM = NIM
        self.Kelas_PBO = Kelas_PBO
        self.Jumlah_SKS = Jumlah_SKS

    def cetakdata(self):
        print("Data mahasiswa: ")
        print()
        print("Nama:", self.nama)
        print()
        print("NIM:", self.NIM)
        print()
        print("Kelas PBO:", self.Kelas_PBO)
        print()
        print("Jumlah SKS yang diambil:", self.Jumlah_SKS)


Data_Mahasiswa = Mahasiswa("MilkyWay", 121140088, "RB", 24)

Data_Mahasiswa.cetakdata()

# Buat akun github, buat repository Prak-PBO,folder tugas1, isi = NIM_nama_tugas1.py
