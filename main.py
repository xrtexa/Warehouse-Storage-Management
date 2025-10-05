from src import InputOutput
from src.tracking import Tracking

def main():
    io = InputOutput()
    while True:
        print("=== Warehouse Storage Management ===")
        print("1. Input barang")
        print("2. Output barang")
        print("3. Lihat stok")
        print("4. Keluar")
        print("Choose option")

        choice = (input(""))

        if choice == "1":
            io.input_item()
        elif choice == "2":
            io.output_item()
        elif choice == "3":
            tracker = Tracking(io.items)
            tracker.show_items()
        elif choice == "4":
            print("Keluar dari program.")
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
