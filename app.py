import function 
daftar_kontak = []
daftar_kontak.append({
    "nama" : "yoga",
    "email" : "prayogaaditya069@gmail.com",
    "telepon" : "087897232423"
})
while True:
    print("#menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")

    menu = input("pilih menu : ")

    if menu == "0":
       break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
   
 
 
 
print("program berjalan lancar, sampai jumpa")
