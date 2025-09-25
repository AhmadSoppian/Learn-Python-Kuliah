# 1. Operator Aritmatika
x = 5
y = 2
# + → untuk penjumlahan
print(x + y) # output 7

# - → untuk pengurangan
print(x - y) # output 3

# * → untuk perkalian
print(x * y) # output 10

# / → untuk pembagian (hasil pecahan)
print(x / y) # output 0.5

# // → untuk pembagian bulat
print(x // y) # output 2 

# % → untuk mencari sisa bagi
print(x % y) # output 1

# ** → untuk perpangkatan
print(x ** y) # output 25

# Operator Perbandingan
x = 5
y = 5
# == → untuk membandingkan sama dengan
print(x == y) # output True

# != → untuk membandingkan tidak sama dengan
print(x != y) # output False 

# > → untuk membandingkan lebih besar dari
print(x > y) # output False

# < → untuk membandingkan lebih kecil dari
print(x < y) # output False

# >= → untuk membandingkan lebih besar atau sama dengan
print(x >= y) # output True

# <= → untuk membandingkan lebih kecil atau sama dengan
print(x <= y) # output True

# Operator Logika
a = True
b = False
# and → untuk logika DAN
print(a and b)   # False (karena salah satu False)

# or → untuk logika ATAU
print(a or b)    # True (karena salah satu True)

# not → untuk logika TIDAK
print(not a)     # False (kebalikan dari True)

# 4. Operator Penugasan


# = → untuk memberikan nilai
# x = 10

# += → untuk menambahkan dan menyimpan ke variabel
x = 10
x += 5   # sama dengan x = x + 5
print(x) # 15

# -= → untuk mengurangi dan menyimpan ke variabel
x = 10
x -= 5   # sama dengan x = x - 5
print(x) # 5

# *= → untuk mengalikan dan menyimpan ke variabel
x = 10
x *= 2   # sama dengan x = x * 2
print(x) # 20

# /= → untuk membagi dan menyimpan ke variabel
x = 10
x /= 5   # sama dengan x = x dibagi 5
print(x) # 2
# //= → untuk pembagian bulat dan menyimpan ke variabel
x = 10
x //= 3  # sama dengan x = x // 3
print(x) # 3

# %= → untuk sisa bagi dan menyimpan ke variabel
x = 10
x %= 3
print(x) # 10
# **= → untuk perpangkatan dan menyimpan ke variabel
x = 10
x **= 2
print(x) # 10

# operator memiliki urutan prioritas (precendence). Operator dengan prioritas lebih tinggi akan dieksekusi terlebih dahulu 
# urutan prioritas (dari tinggi ke rendah)
# - ** (pangkat)
# - *.//./.% (perkalian dan pembagian)
# - +.- (penjumlahan, pengurangan)
# - ==. !=. <. >. <=. >= (perbandingan)
# - not (logika not)
# - and (logika and)
# - or (logika or)