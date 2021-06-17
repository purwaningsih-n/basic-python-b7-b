## Tugas minggu ke-2
## Program dapat menyimpan kontak (​nama dan ​nomor telepon), dan menampilkan kontak-kontak tersebut. 
## Terdapat 3 menu pilihan sbb: 
## 1. Daftar Kontak
## 2. Tambah Kontak
## 3. Keluar

## Inisialisasi data awal
def isi_data_awal():
    data_awal = [
        {'nama': "Ani", 'no_telp': "0111"},
        {'nama' : "Banyu", 'no_telp' : "0222"} 
    ]
    return data_awal

## Mencetak seluruh data
def cetak_data(data_cust):
    j = 1
    print("No ---  Nama pelanggan  ---   No telepon")
    for i in data_cust:
        print(j," --- ",i["nama"]," --- ",i["no_telp"])
        j += 1

## Menambahkan data baru berdasarkan input user dan memberikan pesan jika data berhasil ditambahkan
def tambah_data():
    nama_baru = str(input("Masukkan nama baru : "))
    notelp_baru = str(input("Masukkan no telp : "))
    data_cust.append({"nama":nama_baru, "no_telp":notelp_baru})
    print("Kontak berhasil ditambahkan")   

## Menampilkan pilihan menu, menerima input pilihan dari user. 
## Jika pilihan selain [1-2-3], program menampilkan pesan dan kembali ke menu
## Jika pilihan = 3, program selesai. Selain itu, nilai var pilihan akan dikembalikan     
def pilih_menu():
    print("Selamat datang!")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print()
    pilihan = int(input("Pilih menu: "))
    
    while (pilihan < 1) or (pilihan > 3):
        print("Menu tidak tersedia")
        pilihan = pilih_menu()

    if pilihan == 3:
        print("Program selesai, sampai jumpa!")
    else: return pilihan

## Menjalankan proses jika user memilih menu 1 atau 2 
def jalankan_menu(pilihan_user):
    if (pilihan_user == 1):
        print("Daftar kontak:")
        cetak_data(data_cust)
        print("=========================================================")
        pilihan_user = pilih_menu()
        jalankan_menu(pilihan_user)
    elif (pilihan_user == 2):
        print("Menambahkan data")
        tambah_data()
        print("=========================================================")
        pilihan_user = pilih_menu()
        jalankan_menu(pilihan_user)
    
##-------------------------------------------------------

## Program utama
data_cust = isi_data_awal()
pilihan_user = pilih_menu()
jalankan_menu(pilihan_user)
