nama = "ahmad soppian" #variabel yang menggunakan tipe data string
umur = 18 #variabel yang menggunakan tipe data int atau interger

# manipulasi string : manggabungkan 2 variabel berbeda bertipe data string
pesan = "Halo Nama saya adalah " + nama
# tapi tidak bisa di gabungkan dengan tipe data selain string contoh:
# pesan = "Halo nama saya adalah " + nama + "umur saya adalah" + umur
# akan mengakibatkan eror TypeError: can only concatenate str (not "int") to str
# tapi int bisa di conversi seperti ini 
pesan = "Halo nama saya adalah " + nama + "umur saya adalah" + str(umur)
# str() akan mengconversi tipe data jadi tipe data string
print(pesan)

# mengetahui jumlah panjang kata dari tipe data string menggunakan len()
print(len(nama))

# mengakses karakter yang ada dalam string / indexing
# setiap karakter yang ada didalam string dimulai dari index 0
# bisa dimulai dari depan menggunakan positif
print(nama[0]) # akan memunculkan a
print(nama[1]) # akan memunculkan h
print(nama[2]) # akan memunculkan m
# bisa dimulai dari belakang menggunakan negatif
print(nama[-1]) # akan memunculkan n
print(nama[-2]) # akan memunculkan a
print(nama[-3]) # akan memunculkan i

# string method
# tipe data string memiliki method atau fungsi yang menempel pada tipe data
Name = "Ahmad soppian"
# upper() untuk mengubah semua karakter string menjadi huruf besar semua 
Name_upper = Name.upper()
print(Name_upper) # AHMAD SOPPIAN

# lower() untuk mengubah semua karakter string menjadi huruf kecil semua 
Name_lower = Name.lower()
print(Name_lower) # ahmad soppian

# title() untuk mengubah setiap awal karakter di kata menjadi huruf besar 
Name_title = Name.title()
print(Name_title) # Ahmad Soppian

# capitalize untuk mengubah awal karakter menjadi huruf besar 
Name_capitalize  = Name.capitalize ()
print(Name_capitalize ) # Ahmad soppian

# strip() untuk menghilangkan karakter kosong (seperti spasi) di awal dan akhir
Name_strip  = Name.strip ()
print(Name_strip ) # Ahmad soppian

# replace(dari, menjadi) untuk mengganti bagian tertentu dalam string
Name_replace = Name.replace("soppian", "yannn")
print(Name_replace) # Ahmad yannn

# count(text) untuk menghitung berapa kali text muncul
Name_count = Name.count("p")
print(Name_count) # 2

# find(text) untuk mencari posisi text
Name_find = Name.find("ian")
print(Name_find) # 10
# len untuk menghitung banyaknya karakter
Name_len = Name.__len__()
print(Name_len)