d = {
    "nama" : "Laut Biru",
    "umur" : 6,
    "tinggi" : 100.55
    #key      #value
}
print(d["umur"])
print(d)
d["nama"]="Bening"
print(d)

#for x in d:
    #print(d)

d = []

for i in range(1):
    nama = input("Masukkan Nama anda : ")
    umur = int(input("Masukkan Umur anda : "))
    tinggi = float(input("Masukkan Tinggi anda : "))
    data = {
        "nama" : nama,
        "umur" : umur,
        "tinggi" : tinggi
    }
    d.append(data)
for i in d:
    print("Nama Pelanggan : ",i["nama"])
    print("Umur Pelanggan : ",i["umur"])
    print("Tinggi Pelanggan : ",i["tinggi"])    
