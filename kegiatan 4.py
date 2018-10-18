Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Vintan Kirana'
>>> NIM = 144
>>> Tinggi = 1.60
>>> Berat = 45
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type (Aku) #akan menampilkan tipe dari Aku
<type 'tuple'>
>>> Aku [0] #akan menampilkan data ke 0 dari Aku
2000
>>> a = NIM % 4 ; Aku [a]
2000
>>> #menampilkan data ke a dengan a adalah 0
>>> type(Aku[a])
<type 'int'>
>>> Aku[a:4]
(2000, 45, 1.6, 144)
>>> #menampilkan data Aku
>>> type(Aku[4])
<type 'str'>
>>> #menampilkan tipe dari data di atas adalah string
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> type(Data)
<type 'list'>
>>> #type dari data adalah list
>>> type(Data[4])
<type 'str'>
>>> #type dari data adalah string
>>> Data[4] [5]
'n'
>>> #akan menampilkan indeks ke 5 dari list ke 4
>>> Data [4] [a:6]
'Vintan'
>>> #akan menampilkan indeks ke 0 sampai dengan 5 dari list ke 4
>>> Data[0] = 'ok' ; Data
['ok', 45, 1.6, 144, 'Vintan Kirana']
>>> #data 0 diganti denagan ok karena list dapat diubah ubah
>>> Data[-a]
'ok'
>>> #menampilkan data dari 0
>>> range(a)
[]
>>> 
