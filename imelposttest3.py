import os
os.system

""""Data Laundry Menggunakan Single Linked List"""

class Node:
    def __init__(self,id,nama,laundry):
        self.id = id
        self.nama = nama
        self.laundry = laundry
        self.next = None

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
# Menambahkan Data Laundry ke Daftar
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
        id = int(input ("Masukkan Id Pelanggan: "))
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
# Menghapus Data yang ada di daftar laundry
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
# Menambahkan data yang tersedia di laundry
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
            print (" Daftar Data Laundry Yang Tersedia ".center(20))
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