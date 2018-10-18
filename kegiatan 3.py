Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Vintan Kirana'
>>> NIM = 'L200180144'
>>> X = '1' + NIM [7:] #didalam string, digabungkan angka 1 dengan slicing yang dimulai dari angka/huruf ke tujuh dari variabel NIM sampai selesai
>>> print (X) #menampilkan variabel X
1144
>>> a = int(X) #konversi string ke integer (bilangan bulat)
>>> print (a) #menampilkan variabel a
1144
>>> b = len(Nama) #konversi string dalam variabel Nama kedalam angka
>>> print (b) #menampilkan variabel b
13
>>> type (a) #menampilkan tipe data dari variabel a
<type 'int'>
>>> #python menampilkantipe dari variabel a yang merupakan integer
>>> type (b) #menampilkan tipe data dari variabel b
<type 'int'>
>>> #python menampilkan tipe dari variabel b yang merupakan integer
>>> a / b # operasi pembagian antara variabel a dengan variabel b
88
>>> #python menampilkan hasil bagi dari variabel a dengan variabel b
>>> a // b #operasi pembagian dari variabel a dan variabel b pembulatan ke bawah
88
>>> #python menampilkan hasil dari a // b yang merupakan pembagian dengan pembulatan ke bawah
>>> 10 * (a - 999)
1450
>>> #python menampilkan hasil dari 10 dikali dengan hasil pengurangan a dengan 999
>>> b ** 2 #menampilkan hasil operasi bilangan b dipangkatkan 2
169
>>> #python menampilkan hasil dari variabel b pangkat 2
>>> a % b #operasi yang menghasilkan sisa bagi
0
>>> #python menghasilkan hasil sisa variabel a dibagi variabel b
>>> c = 12.5
>>> type (c) #menampilkan tipe data dari variabel c
<type 'float'>
>>> #python menampilkan tipe data dari variabel c yang berupa float
>>> a / c #operasi pembagian antara variabel a dengan variabel c
91.52
>>> #python menampilkan hasil bagi antara variabel a dengan variabel c
>>> a // c #operasi pembagian antara variabel a dengan variabel c dengan pembulatan ke bawah
91.0
>>> #python menampilkan hasil bagi antara variabel a dengan variabel c lalu dibulatkan ke bawah
>>> a % c #operasi menghasilkan sisa bagi
6.5
>>> #python menampilkan hasil sisa bagi variabel a dibagi dengan variabel c
>>> c > b #menyatakan bahwa variabel c lebih besar daripada variabel b
False
>>> #hasilnya adalah false, karena variabel c tidak lebih besar dari variabel b
>>> type (c > b) #menampilkan tipe data
<type 'bool'>
>>> #type data dari (c > b) adalah bool
>>> a > b and b > c #menyatakan bahwa variabel b lebih besar daripada variabel c dan lebih kecil daripada variabel a
True
>>> #hasilnya adalah true
>>> a > 1100 or b < 10 #menyatakan bahwa variabel a lebih besar dari 1100 atau b lebih kecil dari 10
True
>>> #hasilnya adalah true
