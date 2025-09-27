# function (fungsi) adalah blok kode yang dapat digunakan berulang kali
# function membantu kita menulis kode yang lebih terorganisir, mudah dibaca, dan mudah dipelihara

# menghitung luas persegi pangjang L = p * l
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print('luas persegi panjang adalah', luas)

hitung_luas_persegi_panjang(50, 100)

# menghitung luas lingkaran 
def hitung_luas_lingkaran(radius):
    pi = 3.141
    luas = pi * radius * radius
    return luas

luas1 = hitung_luas_lingkaran(10)

print('luas lingkaran adalah:', luas1)

# menghitung luas persegi
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas
luas_persegi = hitung_luas_persegi(25)

print('luas persegi adalah', luas_persegi)

# default parameter
def sapa(nama, sapaan='hello'):
    print(sapaan, nama)

sapa("ahmad")
sapa('ahmad', 'HI')

# keyword arguments (urutan bebas)
def identitas_mahasiswa(nama, nim, prodi):
    print('Nama:', nama)
    print('NIM:', nim)
    print('Prodi:', prodi)
    print("=======")

# tanpa menggunakan keyword arguments
identitas_mahasiswa('soppian', 19251391, 'sistem informasi')

# menggunakan keyword arguments
identitas_mahasiswa(nim=19251391, prodi='sistem informasi', nama='soppian')