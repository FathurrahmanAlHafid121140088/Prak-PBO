from abc import ABC, abstractmethod


class AkunBank(ABC):
    @abstractmethod
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo

    def transfer_saldo(self):
        pass

    def lihat_suku_bunga(self):
        pass


class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)

    def transfer_saldo(self, transfer):
        self.usia_akun = 2023 - self.tahun_daftar
        if self.usia_akun >= 3 and transfer > 100000:
            print("Biaya administrasi gratis")

        elif self.usia_akun < 3 and transfer > 100000:
            print("Biaya Administrasi : Rp. 2.000")

        else:
            print("Bebas biaya administrasi")

    def lihat_suku_bunga(self):
        if self.usia_akun >= 3 and self.saldo >= 1000000000:
            print("Bunga bulanan adalah: Rp.", self.saldo * 0.01)

        elif self.usia_akun < 3 and self.saldo >= 1000000000:
            print("Bunga bulanan adalah: Rp.", self.saldo * 0.02)

        else:
            print("Bunga bulanan adalah: Rp.", self.saldo * 0.03)


class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)

    def transfer_saldo(self, transfer):
        self.usia_akun = 2023 - self.tahun_daftar
        if self.usia_akun >= 3 and transfer > 100000:
            print("Biaya administrasi sebesar Rp. 2000")

        elif self.usia_akun < 3 and transfer > 100000:
            print("Biaya Administrasi : Rp. 5.000")

        else:
            print("Bebas biaya administrasi")

    def lihat_suku_bunga(self):
        if self.usia_akun >= 3 and self.saldo >= 10000000:
            print("Bunga bulanan adalah: Rp.", self.saldo * 0.01)

        elif self.usia_akun < 3 and self.saldo >= 10000000:
            print("Bunga bulanan adalah: Rp.", self.saldo * 0.02)

        else:
            print("Bunga bulanan adalah: Rp.", self.saldo * 0.03)


akun1 = AkunGold("Rizki", 2022, 15000000000)
akun2 = AkunSilver("Nanda", 2021, 9000000)

akun1.transfer_saldo(500000)
akun2.transfer_saldo(100000)

akun1.lihat_suku_bunga()
akun2.lihat_suku_bunga()
