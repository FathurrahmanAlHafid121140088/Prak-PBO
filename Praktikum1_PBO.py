n = int(input("Masukkan nilai n: ")) #Soal Perulangan

for i in range(n):
    for j in range(n):
        print(' *', end='')
    print()

#-----------------------------------------#

username_benar = "informatika" #Soal Mengecek Password
passw_benar = "12345678"

banyak_percobaan = 0
Cek_Login = False

while banyak_percobaan < 3:
    username = input("Masukkan username: ")
    passw = input("Masukkan Password: ")
    banyak_percobaan += 1

    if username == username_benar and passw == passw_benar:
        Cek_Login = True
        print("Anda telah berhasil login!!")
        break
    
    print("Username atau password salah!, coba lagi")
    print()

if not Cek_Login:
    print("Akun anda telah diblokir!")