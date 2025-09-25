# loop adlah cara untk menjalnkan kode yang sama berulang kali
# dengan perulangan kita bisa menghemat waktu dan  memabuat kode dengan lebih efisien

# For loop
# mencetak angka 0 sampai 4
# for i in range(5): # index dimulai dari 0
#     print(i)

# # mencetak angka 1 sampai 5
# for i in range(1, 6):
#     print(i)

# # mencetak "hallo" sebanyak 3 kali
# for i in range(3):
#     print('hello')

# # menghitung mundur
# print('hitung mundur mulai: ')
# for i in range(5, 0, -1):
#     print(i)

# # menggunakan For loop untuk mengiterasi setiap karakter dalam string
# nama = 'soppian'

# for huruf in  nama:
#     print("-", huruf)


# # while loop
# angka = 1
# while angka <= 5:
#     print(angka)
#     angka += 1 # angka awal ditambah 1

# # penggunaan while loop untuk validasi
# password = ''
# while password != 'admin123':
#     password = input('masukkan password anda: ')
#     if password != 'admin123':
#         print('password anda salah, coba lagi!')
# print('password anda benar!')

# mencetak angka ganjil saja
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# mencari huruf dalam kata
# kata = "informatika"
# huruf_dicari = 'i'

# for huruf in kata:
#     if huruf == huruf_dicari:
#         print("huruf ", huruf_dicari, 'ditemukan dalam kata!')
#         break
# else:
#     print('huruf', huruf_dicari, 'tidak ada dalam kata')

# memasukkan password sampai sisa percobaan habis
password_anda = 'admin123'
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("masukkan password anda!: ")
    percobaan += 1

    if password == password_anda:
        print('selamat anda berhasil login')
        break
    else:
        print('password yang anda masukkan salah, anda memiliki sisa percobaan: ', max_percobaan - percobaan, 'lagi!')
else:
    print('sisa percobaan anda habis!, tunggu selama 5 menit, silahkan coba lagi nanti ')