class Tracking:
    def __init__(self, items):
        self.items = items

    def show_items(self):
        print("\n=== Daftar Barang ===")
        if not self.items:
            print("Belum ada barang.")
            return
        for item in self.items:
            print(f"{item.code} | {item.name} | Stok: {item.quantity}")
