import json
import os

# File name
INVENTORY_FILE = 'inventory.txt'

# Inventory data structure
inventory = []

# Load data from file
def load_inventory():
    global inventory
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as file:
            inventory = json.load(file)

# Save data to file
def save_inventory():
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file)

# Add item
def add_item():
    id = input('Enter item ID: ')
    name = input('Enter item name: ')
    quantity = int(input('Enter item quantity: '))
    price = float(input('Enter item price: '))
    wall = input('Enter wall number (1, 2, or 3): ')
    if wall not in ['1', '2', '3']:
        print('Invalid wall number!')
        return
    inventory.append({'id': id, 'name': name, 'quantity': quantity, 'price': price, 'wall': wall})
    save_inventory()
    print('Item added successfully!')

# Update item
def update_item():
    id = input('Enter item ID to update: ')
    for item in inventory:
        if item['id'] == id:
            item['name'] = input('Enter new name: ')
            item['quantity'] = int(input('Enter new quantity: '))
            item['price'] = float(input('Enter new price: '))
            item['wall'] = input('Enter new wall number (1, 2, or 3): ')
            if item['wall'] not in ['1', '2', '3']:
                print('Invalid wall number!')
                return
            save_inventory()
            print('Item updated successfully!')
            return
    print('Item not found!')

# Delete item
def delete_item():
    id = input('Enter item ID to delete: ')
    for item in inventory:
        if item['id'] == id:
            inventory.remove(item)
            save_inventory()
            print('Item deleted successfully!')
            return
    print('Item not found!')

# Show inventory
def show_inventory():
    if not inventory:
        print('Inventory is empty.')
    for item in inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Wall: {item['wall']}")
