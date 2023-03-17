# """"Data Laundry Menggunakan Single Linked List"""
# kelas Node
class Node:
    def __init__(self,id,nama,laundry):
        self.id = id
        self.nama = nama
        self.laundry = laundry
        self.next = None
# kelas Linked List
class LinkedList :
    def __init__(self):
        self.head = None
# Menampilkan Daftar Data-Data Laundry
    def display(self):
        ("\n")
        if self.head is None :
            print("Tidak ada data Laundry yang Baru")
        else:
            n= self.head
            while n is not None :
                print (f"| ID:{n.id} | {n.nama} | ({n.laundry} Kg) |")
                n= n.next
# Menambahkan Data Laundry Ke Daftar
    def add(self,id,nama,laundry):
        ("\n")
        data_baru= Node (id,nama,laundry)
        if self.head == None:
            self.head = data_baru
        else:
            data_baru.next = self.head
            self.head = data_baru
# Menambahkan Data Baru dengan memasukkan nilai id, nama, dan laundry dari pelanggan yang akan ditambahkan ke daftar
    def addnew(self):
        ("\n")
        id = input ("Masukkan Id Pelanggan: ")
        nama = input("Masukkan Nama Pelanggan: ")
        laundry = int (input("Masukkan Laundry/Kg Pelanggan: "))
        data_baru2 = Node(id,nama,laundry)
        if self.head is None:
            self.head = data_baru2
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = data_baru2
        print (" Data Berhasil Di Tambahkan!! ")
# Menghapus Data yang ada di Daftar laundry
    def delete (self):
        ("\n")
        Id = int (input("\n Masukkan Id Pelanggan : "))
        if self.head is None:
            print("Tidak Ada ID.")
        elif self.head.id == Id:
            self.head = self.head.next
            print(" Data Berhasil Dihapus! ")
        else:
            current = self.head
            while current.next is not None:
                if current.next.id == Id:
                    current.next = current.next.next
                    print(" Data berhasil dihapus! ")
                    return True
                current = current.next
            print(" Id Tidak Ditemukan.")

# Fungsi untuk Tampilan Awal  & Menu Login
def luser():
    while True:
        print("="*5,"Selamat Datang di dream Laundry ".center(40),"="*5)
        print("="*52,"\n")
        print(" 1. Layanan Laundry ")
        print(" 2. Keluar ")
        pilih = int(input("\nPilihan => "))
        if pilih == 1:
            os.system ('cls')
            print (" Login ".center(40))
            input ("Username : ")
            input ("Password : ")
            return True
        elif pilih == 2:
            print ("Terimakasih")
            break
        else:
            break
        
laundryimel=LinkedList ()
# Menambahkan data yang tersedia di laundry pada daftar
laundryimel.add(20,"imel", 7)
laundryimel.add(22,"nisa", 5)
laundryimel.add(29, "vhia", 3)

# Main Menu
if luser ():
    while True:
        os.system ('cls')
        print("* Dream Laundry *".center(40))
        print ()
        print(" Rincian Laundry Dream :")
        print("1. Lihat data laundry")
        print("2. Menambah data laundry")
        print("3. Hapus data laundry")
        print("4. Keluar")
        pilihan = int(input("Masukkan pilihan: "))
        print ()
        if pilihan == 1:
            print (" Data Laundry Yang Tersedia ".center(20))
            print ()
            laundryimel.display ()
            input ("=================================")
        elif pilihan == 2:
            print (" Tambah Data Baru ".center(20))
            print ()
            laundryimel.addnew()
            input ("=================================")
        elif pilihan == 3:
            print (" Hapus Data Laundry ".center(20))
            print ()
            laundryimel.display()
            laundryimel.delete()
            input ("=================================")
        elif pilihan == 4:
            break
        else:
            print("Pilihan Tidak Valid.")
            
# Penjelasan Cara Kerja Program dan Cara Aplikasi Bekerja
Program diatas adalah implementasi dari program single linked list. Program ini terdiri dari dua kelas, yaitu kelas Node dan kelas LinkedList. 
* Kelas Node digunakan untuk menginisialisasi tiga variabel yaitu id, nama, dan laundry. Variabel next berfungsi sebagai penunjuk ke node berikutnya yang akan ditambahkan. 
* Kelas LinkedList digunakan untuk memungkinkan kita untuk menuangkan Node ke dalam daftar terkait. 
Dalam inisialisasinya, kita membuat kepala node yaitu variabel self.head yang pada awalnya tidak memiliki node apa pun, sehingga nilainya adalah None. 
~Metode display akan menampilkan daftar node yang telah ditambahkan pada program. Jika tidak ada data pada program, pesan “Tidak ada data Laundry yang Baru” akan ditampilkan. 
~ Metode add digunakan untuk menambahkan node baru ke daftar. Jika daftar masih kosong, maka node baru akan menjadi node pertama melalui pembaruan variabel self.head. Jika daftar sudah berisi node, maka node baru akan ditambahkan di awal dan variabel self.head akan diperbarui. 
~ Metode addnew meminta pengguna untuk memasukkan nilai id, nama, dan laundry dari pelanggan yang akan ditambahkan ke daftar. Sama seperti metode add, metode addnew juga menambahkan node baru ke daftar laundry. 
~ Metode delete digunakan untuk menghapus node yang sudah ditambahkan ke dalam daftar laundry. Pengguna diminta untuk memasukkan nilai Id dari node yang akan dihapus. Metode ini akan menjelajahi daftar laundry dan mencari node dengan id yang sesuai. Jika node ditemukan, maka node tersebut akan dihapus dari daftar laundry, dan jika tidak ditemukan, maka pesan “Id tidak ditemukan” akan ditampilkan. 
* Fungsi luser () adalah fungsi login yang akan meminta pengguna untuk memasukkan username dan password untuk masuk ke program. Program dapat dijalankan jika fungsi login berhasil dilakukan. Pada perulangan utama, terdapat empat pilihan yang dapat dipilih oleh pengguna, yaitu melihat data laundry, menambahkan data laundry baru, menghapus data laundry, atau keluar dari program. 
Jika pengguna memilih opsi 1, maka daftar laundry akan ditampilkan. 
Jika pengguna memilih opsi 2, maka pengguna akan diminta untuk memasukkan detail pelanggan baru yang akan ditambahkan ke daftar laundry. 
Jika pengguna memilih opsi 3, maka pengguna akan diminta untuk memasukkan id dari node yang akan dihapus dari daftar laundry. 
Jika pengguna memilih opsi 4, program akan keluar dan program berakhir.

# OUTPUT Program
# Tampilan Awal
=====     Selamat Datang di dream Laundry      =====
==================================================== 

 1. Layanan Laundry 
 2. Keluar 

Pilihan => 1
# Menu Login
                 Login
Username : imel
Password : 123

# Tampilan Menu
* Dream Laundry *

 Rincian Laundry Dream :
1. Lihat data laundry
2. Menambah data laundry
3. Hapus data laundry
4. Keluar

# Menampilan Daftar Data Laundry
Masukkan pilihan: 1

 Daftar Data Laundry Yang Tersedia 

| ID:29 | vhia | (3 Kg) |
| ID:22 | nisa | (5 Kg) |
| ID:20 | imel | (7 Kg) |
| ID:18 | mila | (5 Kg) |
| ID:06 | chan | (8 Kg) |
=================================  

# Menambahkan Data 
  Tambah Data Baru     

Masukkan Id Pelanggan: 18
Masukkan Nama Pelanggan: mila
Masukkan Laundry/Kg Pelanggan: 5
 Data Berhasil Di Tambahkan!!    
=================================

# Menghapus Data
Masukkan pilihan: 3

 Hapus Data Laundry      

| ID:29 | vhia | (3 Kg) |
| ID:22 | nisa | (5 Kg) |
| ID:20 | imel | (7 Kg) |
| ID:18 | mila | (5 Kg) |
| ID:16 | chan | (8 Kg) |

 Masukkan Id Pelanggan : 16
 Data berhasil dihapus!
=================================
