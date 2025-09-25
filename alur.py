# kontrol alur program adlah cara untuk mengatur jalannya program berdasarkan kondisi tertentu
# dengan kontrol alur,, program bisa mengambil keputusan dan melakukan tindakan yang berbeda tergantung pada situasi 

angka = int(input('masukkan angka: '))

if angka > 0:
    print('angka positif')

if angka < 0: 
    print('angka negatif')

if angka == 0:
    print('angka nol')

nilai = int(input('masukkan nilai anda: '))

if nilai >= 90:
    print('Grade A')
elif nilai >= 80:
    print('Grade B')
elif nilai >= 70:
    print('Grade C')
else:
    print('Grade D')

umur = int(input('masukkan umur kamu: '))
punya_sim = input('Punya SIM? (ya/tidak): ')

if umur >= 17 and punya_sim == 'ya':
    print('Boleh mengendarai motor')
else:
    print('tidak boleh mengendarai motor')

username = input('Username:')
password = input('Password: ')

if username == "admin123":

    if password == 'admin':
        print('anda login sebagai admin')
        print('selamat datang dihalaman admin')
    else:
        print('password salah')   
else:
    print('username tidak ditemukan')

# Match-case adalah alternatif elif
hari = input('masukkan nama hari: ').lower()

match hari:
    case 'senin' | 'selasa' | 'rabu' | 'kamis' | 'jumat':
        print('hari ini hari kerja')
    case 'sabtu' | 'minggu':
        print('hari ini hari libur')
    case _:
        print('hari tidak valid')

# ternary operator 

angka = int(input('masukkan angka: '))

# #  dengan if-else biasa 
# if angka > 0:
#     print('angka positif')
# else:
#     print('angka negatif')

# dengan ternary op
hasil = "positif" if angka >= 0 else "negatif"
print('angka tersebut:', hasil)