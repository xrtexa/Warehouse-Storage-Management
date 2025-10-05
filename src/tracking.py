class Tracking:
    def __init__(self, items):
        self.items = items

    def show_items(self):
        print("\n=== Daftar Barang ===")
        if not self.items:   #if statement digunakan untuk mengetahui apakah pada object "self" terdapat data atau tidak
            print("Belum ada barang.")
            return
        for item in self.items:  #for digunakan untuk menunjukkan data yang terdapat di dalam object "self"
            print(f"{item.code} | {item.name} | Stok: {item.quantity}")
