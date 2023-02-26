def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("===================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")
def new_kontak():
    nama = input("Nama : "),
    email = input("Email : "),
    telepon = input("Telepon: ")
    kontak = {
        'nama' : nama,
        'email' : email,
        'telepon' : telepon
     }
    return kontak
