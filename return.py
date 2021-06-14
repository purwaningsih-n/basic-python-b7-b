def function(p,l):
    Luas = p*l
    text = "Luas persegi panjang  adalah {} ".format(Luas)
    return text
print(function(20,10))   

def function_luas(p,l):
    Luas = p*l 
    #text = "Luas persegi panjang adalah {}".format(Luas)
    #return(text)
    return Luas

##input
p = int(input("panjang: "))
l = int(input("lebar: "))

##memanggil fungsi dan menampilkan hasil (Luas)
print(function_luas(p,l))

hasil = function_luas(p,l)
print(hasil)
