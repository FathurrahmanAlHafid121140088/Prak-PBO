class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk
        self.komponen = []

    def tambah_komponen(self, komponen):
        self.komponen.append(komponen)

    def lihat_komponen(self):
        print(
            f"Komputer {self.nama} dengan jenis {self.jenis} dan merk {self.merk}:")
        for komponen in self.komponen:
            komponen.info()


class Processor(Komputer):
    def __init__(self, nama, jenis, harga, merk, jumlah_core, kecepatan_processor):
        super().__init__(nama, jenis, harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

    def info(self):
        print(
            f"Processor dengan jumlah core {self.jumlah_core} dan kecepatan {self.kecepatan_processor} GHz")


class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity):
        super().__init__(nama, jenis, harga, merk)
        self.capacity = capacity

    def info(self):
        print(f"RAM dengan kapasitas {self.capacity} GB")


class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity, rpm):
        super().__init__(nama, jenis, harga, merk)
        self.capacity = capacity
        self.rpm = rpm

    def info(self):
        print(
            f"HDD dengan kapasitas {self.capacity} GB dan kecepatan putar {self.rpm} RPM")


class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity):
        super().__init__(nama, jenis, harga, merk)
        self.capacity = capacity

    def info(self):
        print(f"VGA dengan kapasitas {self.capacity} GB")


class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk, daya):
        super().__init__(nama, jenis, harga, merk)
        self.daya = daya

    def info(self):
        print(f"PSU dengan daya {self.daya} Watt")


komputer1 = [Processor('Intel Core i5', 'Processor', 2500000, 'Intel', 4, 3.4),
             RAM('Kingston DDR4', 'RAM', 1000000, 'Kingston', 8),
             HDD('Seagate Barracuda', 'HDD', 1200000, 'Seagate', 1000, 7200),
             VGA('MSI Nvidia GTX 1650', 'VGA', 2500000, 'MSI', 4),
             PSU('Corsair CX450', 'PSU', 800000, 'Corsair', 450)]

komputer2 = [Processor('AMD Ryzen 5', 'Processor', 3000000, 'AMD', 6, 3.6),
             RAM('Corsair DDR4', 'RAM', 1500000, 'Corsair', 16),
             HDD('Western Digital Caviar', 'HDD',
                 1600000, 'Western Digital', 2000, 5400),
             VGA('Asus Nvidia RTX 2060', 'VGA', 6000000, 'Asus', 8),
             PSU('Seasonic Focus GX-750', 'PSU', 2000000, 'Seasonic', 750)]

print('Komputer 1:')
for komponen in komputer1:
    print(komponen.jenis, komponen.nama, "produksi", komponen.merk)
print()

print('Komputer 2:')
for komponen in komputer2:
    print(komponen.jenis, komponen.nama, "produksi", komponen.merk)
print()
