## Program menentukan status kelulusan
## Input berupa nilai ujian teori dan praktek, nilai ujian dapat berupa bilangan desimal
## Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70
## Siswa dinyatakan mengulang jika nilai ujian kurang dari 70

## input nilai
n_teori = float(input("Masukkan nilai ujian teori: "))
n_praktek = float(input("Masukkan nilai ujian praktek: "))

## tentukan status kelulusan
if (n_teori >= 70):
    if (n_praktek >= 70): 
        print("Selamat, Anda lulus!")
    else:
        print("Anda harus mengulang ujian praktek")
elif (n_praktek >= 70):
        print("Anda harus mengulang ujian teori")
else: print("Anda harus mengulang ujian teori dan praktek")