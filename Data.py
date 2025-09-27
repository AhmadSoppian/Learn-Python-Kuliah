# struktur data
# Data Structures adalah cara untuk menyimpan dan mengorganisir data dalam pemrograman

# List (Daftar)
buah = ["apel", 'mangga', 'jeruk'] # list digunakan untuk mentimpan lebih dari 1 nilai
print(buah)
buah[1] = 'alpukat' # mengubah nilai yang tersimpan dalam list sesuai index yang diminta
print(buah)
buah.append('durian') # menambahkan nilai ke dalam list dibagian akhir list
print(buah)
buah.insert(1, 'buah naga') # menambahkan nilai ke dalam list sesuai index yang diinginkan dan sesuai nilai yang diinginkan
print(buah)
buah.remove('jeruk') # menghapus nilai yang diinginkan di dalam list
print(buah)
buah.pop() # menghapus nilai terakhir dalam list
print(buah)
del buah[0] # menghapus nilai susai index yang diinginkan
print(buah)

# manipulasi list
# menggabungkan list
angka1 = [1,2,3,4,5]
angka2 = [6,7,8,9,10]
print(angka1)
print(angka2)
print(angka1 + angka2)

# perulangan pada list
box_buah = ['apel', 'mangga', 'jeruk', 'alpukat']
for buah in box_buah:
    print(buah)

for i in range(0, len(box_buah)):
    print(box_buah[2])

if "durian" in box_buah:
    print('buah ada didalam box')
else:
    print('tidak ada buah dalam box')


# Tuple 
# mirip dengan list, tetapi tidak bisa diubah setelah dibuat. tuple ditulis dengan kurung biasa().
tanggal_lahir = (22, 1, 2007)
print('tanggal lahir anda: ', tanggal_lahir)

# iterasi di tuple
for e in tanggal_lahir:
    print('e')
# iterasi di tuple dengan menggunakan index
for i in range(len(tanggal_lahir)):
    print(tanggal_lahir[i])


# Dictionary (kamus)
# menyimpan data dalam pasangan key-velue (kunci-nilai). Dictionary ditulis dengan kurung kueawal {}
mahasiswa = {
    'nama' : 'ahmad soppian',
    'nim' : 19251391,
    'prodi' : 'sitem informasi'
}
print(mahasiswa)

print(mahasiswa['nama']) # ahmad soppian
print(mahasiswa['nim']) # 19251391
print(mahasiswa['prodi']) # sistem informasi

# mengubah nilai
mahasiswa['prodi'] = 'teknologi informasi'
print(mahasiswa)

# menghapus key-value
del mahasiswa['prodi']
print(mahasiswa)

# mengiterasi keys
for key in mahasiswa:
    print(key, ':', mahasiswa[key])

# mengiterasi  key-value pairs
for key, value in mahasiswa.items():
    print(key, '=', value)


# Set (himpunan)
# adlah kumpulan data yang tidak berurutan dan tidak memiliki elemen duplikat
# Set ditulis dengan kurung kurawal{} atau fungsi set()

makanan = {'burger', 'pizza', 'nasi padang'}
print(makanan)

makanan.add('ayam')
print(makanan)
makanan.add('ayam')
print(makanan)

makanan.remove("pizza")
print(makanan)

# perulangan 

for x in makanan:
    print(makanan)