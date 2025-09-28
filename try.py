# print('=== KALKULATOR SEDERHANA ===')

# try:
#     angka1 = int(input('masukkan angka pertama: '))
#     angka2 = int(input('masukkan angka kedua: '))
#     hasil = angka1 / angka2
#     print('Hasil', hasil)
# except ValueError:
#     print('mohon masukkan angka yang valid!')
# except ZeroDivisionError:
#     print('angka tidak bisa dibagi dengan 0')
# except:
#     print('terjadi kesalahan!')

try:
    angka = int(input('masukkan angka:'))
except ValueError:
    print('angka tidak valid')
else:
    print('angka yang anda masukkan: ', angka)
    if angka > 0:
        print('angka anda positif')
    elif angka < 0:
        print('angka anda negatid')
    else:
        print('angka anda nol!')
finally:
    print('program selesai!')