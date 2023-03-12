class Mobil:
    # atribut/fungsi kelas
    jumlah_mobil = 0  # Digunakan untuk menghitung jumlah mobil

    def __init__(self, merk, tahun, warna):  # Menginisialisasi atribut pada objek
        # atribut private
        self.__merk = merk
        self.__tahun = tahun
        # atribut protected
        self._warna = warna
        Mobil.jumlah_mobil += 1

    # method public
    def info_mobil(self):  # Menampilkan informasi dari mobil
        print("Merk:", self.__merk)
        print("Tahun:", self.__tahun)
        print("Warna:", self._warna)

    # method protected
    def _ubah_warna(self, warna_baru):  # Mengubah warna dari mobil
        self._warna = warna_baru

    # method private
    def __ubah_tahun(self, tahun_baru):  # Mengubah Tahun Mobil
        self.__tahun = tahun_baru


mobil1 = Mobil("Toyota", 2021, "hitam")  # Inisaslisasi objek dengan atributnya
mobil2 = Mobil("Honda", 2022, "merah")

# akses atribut public
print(mobil1._warna)  # Warna mobl adalah hitam

# akses atribut protected
mobil1._ubah_warna("biru")  # Mengubah warna mobil dari hitam menjadi biru
print(mobil1._warna)

# akses atribut private (Coba akses atribut privat)
# print(mobil1.__merk) # akan menghasilkan AttributeError
# mobil1.__ubah_tahun(2023) # akan menghasilkan AttributeError

# akses atribut/fungsi kelas
print("Jumlah mobil:", Mobil.jumlah_mobil)  # Mengakses jumlah dari mobil
