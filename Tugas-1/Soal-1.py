##Program menerima 3 input dari user kemudian menampilkan ke layar dengan format 
## "Nama saya [​Nama​], umur saya [​Umur​] tahun dan tinggi saya [​Tinggi​] cm."
##Input tersebut berupa:
##1. ​Nama​ bertipe data ​string
##2. ​Umur​ bertipe data ​integer
##3. ​Tinggi​ bertipe data ​float

nama = str(input("Masukkan nama Anda: "))
umur = int(input("Berapa umur Anda: "))
tinggi = float(input("Berapa tinggi Anda: "))

print("Nama saya "+nama+", umur saya",umur,"tahun dan tinggi saya",tinggi,"cm.")