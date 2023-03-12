class AkunBank:
    list_nasabah = []

    def __init__(self, no_nasabah, nama_nasabah, jumlah_saldo):
        self.__no_nasabah = no_nasabah
        self.__nama_nasabah = nama_nasabah
        self.__jumlah_saldo = jumlah_saldo
        self.__class__.list_nasabah.append(self)

    def lihat_saldo(self):
        print("Jumlah saldo saat ini yaitu: Rp.", self.__jumlah_saldo)
        print()

    def tarik_tunai(self, jumlah_tarik):
        if jumlah_tarik <= self.__jumlah_saldo:
            self.__jumlah_saldo -= jumlah_tarik
            print("Penarikan tunai sebesar Rp. {} berhasil.".format(jumlah_tarik))
            print("Jumlah saldo anda sekarang adalah: Rp. {}".format(
                self.__jumlah_saldo))
            print()

        else:
            print("Jumlah saldo anda tidak cukup!")
            print()

    def transfer(self, no_tujuan, jumlah_transfer):
        for nasabah in self.__class__.list_nasabah:
            if nasabah.__no_nasabah == no_tujuan:
                if jumlah_transfer <= self.__jumlah_saldo:
                    self.__jumlah_saldo -= jumlah_transfer
                    nasabah.__jumlah_saldo += jumlah_transfer
                    print("Transfer sebesar Rp. {} ke nasabah {} berhasil.".format(
                        jumlah_transfer, nasabah.__nama_nasabah))
                    print("Jumlah saldo anda sekarang adalah: Rp. {}".format(
                        self.__jumlah_saldo))
                    print()
                else:
                    print("Maaf saldo anda tidak cukup!")
                    print()
                return
        print("No Nasabah Tujuan tidak ditemukan")
        print()

    def lihat_menu(self):
        print("Selamat datang di Bank Jago,", self.__nama_nasabah)
        print("1. Cek saldo")
        print("2. Tarik Tunai")
        print("3. Transfer")
        print("4. Keluar")


akun1 = AkunBank(1234, "MilkyWay", 5000000000)
akun2 = AkunBank(2345, "Ukraina", 7000000000)
akun3 = AkunBank(3456, "Elon Musk", 9000000000)

pil_akun = input(
    "Pilih akun yang tersedia ( 1 = Akun 1, 2 = Akun 2, 3 = Akun 3): ")

if pil_akun == "1":
    while True:

        akun1.lihat_menu()

        pilihan = input("Masukkan pilihan anda: ")

        if pilihan == "1":
            akun1.lihat_saldo()

        elif pilihan == "2":
            input_jumlah = input(
                "Masukkan jumlah nominal yang ingin ditarik: ")
            jumlah_tarik = int(input_jumlah)
            akun1.tarik_tunai(jumlah_tarik)

        elif pilihan == "3":
            input_transfer = input("Masukkan nominal yang ingin di transfer: ")
            jumlah_transfer = int(input_transfer)
            input_tujuan = input("Masukkan nomor rekening tujuan: ")
            no_tujuan = int(input_tujuan)
            akun1.transfer(no_tujuan, jumlah_transfer)

        elif pilihan == "4":
            print("Program telah berhenti")
            break

        else:
            print("Input tidak valid!")
elif pil_akun == "2":
    while True:

        akun2.lihat_menu()

        pilihan = input("Masukkan pilihan anda: ")

        if pilihan == "1":
            akun2.lihat_saldo()

        elif pilihan == "2":
            input_jumlah = input(
                "Masukkan jumlah nominal yang ingin ditarik: ")
            jumlah_tarik = int(input_jumlah)
            akun2.tarik_tunai(jumlah_tarik)

        elif pilihan == "3":
            input_transfer = input("Masukkan nominal yang ingin di transfer: ")
            jumlah_transfer = int(input_transfer)
            input_tujuan = input("Masukkan nomor rekening tujuan: ")
            no_tujuan = int(input_tujuan)
            akun2.transfer(no_tujuan, jumlah_transfer)

        elif pilihan == "4":
            print("Program telah berhenti")

        else:
            print("Input tidak valid!")


elif pil_akun == "3":
    while True:
        akun3.lihat_menu()

        pilihan = input("Masukkan pilihan anda: ")

        if pilihan == "1":
            akun3.lihat_saldo()
        elif pilihan == "2":
            input_jumlah = input(
                "Masukkan jumlah nominal yang ingin ditarik: ")
            jumlah_tarik = int(input_jumlah)
            akun3.tarik_tunai(jumlah_tarik)

        elif pilihan == "3":
            input_transfer = input(
                "Masukkan nominal yang ingin di transfer: ")
            jumlah_transfer = int(input_transfer)
            input_tujuan = input("Masukkan nomor rekening tujuan: ")
            no_tujuan = int(input_tujuan)
            akun3.transfer(no_tujuan, jumlah_transfer)

        elif pilihan == "4":
            print("Program telah berhenti")
            break

        else:
            print("Input tidak valid!")

else:
    print("Input tidak valid!")
