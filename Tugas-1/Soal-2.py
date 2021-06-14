## Program menghitung luas lingkaran
## nilai r merupakan input dari user

r = int(input("masukkan panjang jari-jari lingkaran: "))
luas = 22/7 * r * r
format_luas = "{:.2f}".format(luas)
print("Luas lingkaran dengan jari-jari",r,"cm adalah",format_luas,"cm\u00b2")
