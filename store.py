import sys

class Product:
    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

class GroceryStore:
    def __init__(self):
        self.products = {}
        self.sales = []

    def add_product(self, product):
        self.products[product.pid] = product

    def update_stock(self, pid, quantity):
        if pid in self.products:
            self.products[pid].quantity += quantity
        else:
            print("Product ID does not exist.")

    def sell_product(self, pid, quantity):
        if pid in self.products:
            product = self.products[pid]
            if product.quantity >= quantity:
                product.quantity -= quantity
                sale = {'pid': pid, 'name': product.name, 'quantity': quantity, 'total': product.price * quantity}
                self.sales.append(sale)
                print(f"Sold {quantity} of {product.name}")
            else:
                print("Insufficient stock.")
        else:
            print("Product ID does not exist.")

    def show_inventory(self):
        print("\nInventory:")
        for p in self.products.values():
            print(f"ID: {p.pid}, Name: {p.name}, Price: {p.price}, Stock: {p.quantity}")

    def show_sales(self):
        print("\nSales Report:")
        for sale in self.sales:
            print(f"Product ID: {sale['pid']}, Name: {sale['name']}, Quantity: {sale['quantity']}, Total: {sale['total']}")

def main():
    store = GroceryStore()
    while True:
        print("\n1. Add Product\n2. Update Stock\n3. Sell Product\n4. Show Inventory\n5. Show Sales\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pid = input("Product ID: ")
            name = input("Product Name: ")
            price = float(input("Product Price: "))
            quantity = int(input("Product Quantity: "))
            store.add_product(Product(pid, name, price, quantity))
        elif choice == '2':
            pid = input("Product ID: ")
            quantity = int(input("Quantity to add: "))
            store.update_stock(pid, quantity)
        elif choice == '3':
            pid = input("Product ID: ")
            quantity = int(input("Quantity to sell: "))
            store.sell_product(pid, quantity)
        elif choice == '4':
            store.show_inventory()
        elif choice == '5':
            store.show_sales()
        elif choice == '6':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()