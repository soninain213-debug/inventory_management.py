import pickle
import os

# ---------- Product Class (Encapsulation) ----------
class Product:
    def __init__(self, pid, name, price, qty):
        self.pid = pid
        self.name = name
        self.price = price
        self.qty = qty

    def show(self):
        print(f"{self.pid}\t{self.name}\t{self.price}\t{self.qty}")

# ---------- Perishable Product (Inheritance + Polymorphism) ----------
class PerishableProduct(Product):
    def __init__(self, pid, name, price, qty, expiry):
        super().__init__(pid, name, price, qty)
        self.expiry = expiry

    def show(self):
        print(f"{self.pid}\t{self.name}\t{self.price}\t{self.qty}\t{self.expiry}")

# ---------- Inventory Class (Abstraction + File Handling) ----------
class Inventory:
    def __init__(self, fname="inventory.dat"):
        self.fname = fname
        self.products = self.load()

    def load(self):
        if os.path.exists(self.fname):
            with open(self.fname, "rb") as f:
                return pickle.load(f)
        return {}

    def save(self):
        with open(self.fname, "wb") as f:
            pickle.dump(self.products, f)

    def add(self, p):
        self.products[p.pid] = p
        self.save()
        print(" Product Added Successfully!")

    def update(self, pid):
        if pid in self.products:
            p = self.products[pid]
            p.name = input("New Name: ") or p.name
            p.price = float(input("New Price: ") or p.price)
            p.qty = int(input("New Quantity: ") or p.qty)
            self.save()
            print(" Product Updated Successfully!")
        else:
            print(" Product Not Found!")

    def delete(self, pid):
        if pid in self.products:
            del self.products[pid]
            self.save()
            print(" Product Deleted Successfully!")
        else:
            print(" Product Not Found!")

    def view(self):
        if not self.products:
            print("No Products Found!")
        else:
            print("\nID\tName\tPrice\tQty\tExpiry(Optional)")
            print("------------------------------------------")
            for p in self.products.values():
                p.show()

# ---------- Main Menu ----------
def main():
    inv = Inventory()

    while True:# create infinite loop.
        print("\n===== INVENTORY MENU =====")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Products")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()  # strip removes spaces

        if choice == '1':
            pid = input("Enter ID: ")
            name = input("Enter Name: ")
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))
            exp = input("Enter Expiry (optional): ")
            if exp:
                p = PerishableProduct(pid, name, price, qty, exp)
            else:
                p = Product(pid, name, price, qty)
            inv.add(p)

        elif choice == '2':
            pid = input("Enter Product ID to Update: ")
            inv.update(pid)

        elif choice == '3':
            pid = input("Enter Product ID to Delete: ")
            inv.delete(pid)

        elif choice == '4':
            inv.view()

        elif choice == '5':
            print("Exiting... Thank You!")
            break

        else:
            print(" Invalid Choice! Please enter 1, 2, 3, 4 or 5.")

if __name__ == "__main__":
    main()