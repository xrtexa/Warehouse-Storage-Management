from data.item_data import Item

class InputOutput:
    def __init__(self):
        self.items = []

    def input_item(self):
        code = input("Masukkan kode barang: ")
        name = input("Masukkan nama barang: ")
        qty = int(input("Masukkan jumlah: "))
        item = Item(code, name, qty)
        self.items.append(item)
        print(f"Barang {name} ditambahkan.")

    def output_item(self):
        code = input("Masukkan kode barang yang keluar: ")
        for item in self.items:
            if item.code == code:
                qty = int(input("Jumlah keluar: "))
                if qty <= item.quantity:
                    item.quantity -= qty
                    print(f"{qty} unit {item.name} dikeluarkan.")
                else:
                    print("Stok tidak cukup.")
                break
        else:
            print("Barang tidak ditemukan.")
