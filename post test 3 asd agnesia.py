class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.history = []

    def tambahAkhir(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
        self.history.append(('data masuk', value))

    def hapusDepan(self):
        if self.head is None:
            print("Linked list kosong")
        else:
            value = self.head.data
            self.head = self.head.next
            self.history.append(('data dihapus', value))

    def printList(self):
        if self.head is None:
            print("Antrian Kosong")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" --> ")
                n = n.next
        print('\n')

antrian = LinkedList()

while True:
    print("\nSelamat Datang di Perpustakaan")
    print("1. Tambah antrian")
    print("2. Tampilkan daftar antrian")
    print("3. Panggil antrian")
    print("4. Riwayat antrian")
    print("5. Exit")

    menu = input("\nMasukkan Pilihan Anda (1/2/3/4/5): ")

    if menu == "1":
        nama = input("Masukkan nama pendaftar : ")
        antrian.tambahAkhir(nama)
        print("Pendaftar dengan nama", nama, "berhasil ditambahkan pada antrian")
    
    elif menu == "2":
        antrian.printList()

    elif menu == "3":
        antrian.hapusDepan()
        antrian.printList()

    elif menu == "4":
        for event in antrian.history:
            print(event[0], ':', event[1])
    
    elif menu == "5":
        break
    
    else:
        print("Pilihan tidak tersedia. Coba Lagi.")