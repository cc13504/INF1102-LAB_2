import os

#Global Contants
MAX_CAPACITY = 500
TAX_RATE = 0.1  # 10% tax rate
INVENTORY_FILE = "inventory.txt"

inventory = {}

#local variables
user_input = 0
current_total = 0
error_count = 0
tax_result = 0


#class Product
class Product:
    def __init__(self,product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def add_stock (self,quantity):
        new_stock = self.__stock + quantity
        if new_stock < 0:
            print(f"Invalid! Stock should not fall below 0. Current stock is {self._stock}.")
            return 
        else:
            self.__stock = new_stock

    def product_information(self):
        return  {"product_id" : self.__product_id,
                "product_name" : self.__name,
                "product_price": self.__price,
                "product_stock" : self.__stock
        }


class Inventory:

    def __init__(self):
        self.inventory = {}

    def add_product(self):

        name = input("Enter the name of the new product:\n")

        if not name:
         print("Error: Product name cannot be empty.")
         return
    
        if name in inventory:
         print("Error: Product already exists.")
         return

        qty_in = input("Enter initial quantity: ").strip()

        if qty_in.isdigit():
            inventory[name] = int(qty_in)
            print("Success: Product added.")
        else:
         print("Invalid quantity.")

    def display_information(self):
        inventory = {Product.product_information}
        return inventory

    def display_all_products(inventory):
        print("\n--- Current Inventory List ---")
        if not inventory:
            print("The inventory is currently empty.")
        else:
            print("Product | Quantity")
            for name, qty in inventory.items():
                print(name + " | " + str(qty))


class File_Handling:
    def __init__(self):
            pass
    
    def load_inventory():
        try:
         with open(INVENTORY_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, qty = parts[0], parts[1]
                    if qty.isdigit():
                        inventory[name] = int(qty)
        except (FileNotFoundError, ValueError):
         pass

        return inventory

    
    def save_inventory_to_file(inventory):
        with open(INVENTORY_FILE, "w") as file:
            for name, qty in inventory.items():
                file.write(name + "," + str(qty) + "\n")






def update_stock(self, new_quantity):
    name = input("Enter the product name to update: \n")
    if name not in inventory:
        print("Error: Product not found.")
        return

    print("Current quantity: " + str(inventory[name]))
    change_in = input("Enter amount to add (use negative to remove): ").strip()
    
    is_negative = change_in.startswith("-")
    clean_val = change_in[1:] if is_negative else change_in

    if clean_val.isdigit():
        amount = int(clean_val)
        if is_negative:
            amount = -amount
        
        inventory[name] += amount
        if inventory[name] < 0:
            inventory[name] = 0
            
        print("Success: Stock updated.")
    else:
        print("Invalid input.")

def search_product(inventory):
    name = input("Enter the product name to search for: ").strip()
    if name in inventory:
        print("Result: " + name + " | Quantity: " + str(inventory[name]))
    else:
        print("Product not found.")
        

#main function
def main():
    
    current_total = load_inventory()
    
    while True:
        print("\nINVENTORY MANAGEMENT SYSTEM")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            display_all_products(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory_to_file(inventory)
            print("Inventory saved!")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")

    

if __name__ == "__main__":
    main()









