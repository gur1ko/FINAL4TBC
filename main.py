from inventory import Inventory
from auth import Auth

def main_menu():
    auth = Auth()
    
    while True:
        print('Welcome to the Coin Collection Management System')
        print('1. Log in')
        print('2. Register')
        print('3. Info')
        print('4. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            if auth.login():
                user_menu(auth)
        elif choice == '2':
            auth.register()
        elif choice == '3':
            print('This is a Coin Collection Management System. Please register or log in to continue.')
        elif choice == '4':
            return
        else:
            print('Invalid choice, please try again.')

def user_menu(auth):
    user_email = auth.get_current_user_email()
    inventory_collection = auth.get_user_inventory(user_email)
    inventory = Inventory()
    inventory.collection = inventory_collection

    while True:
        print('Inventory Management System')
        print('1. Add Item')
        print('2. Update Item')
        print('3. Delete Item')
        print('4. Show Inventory')
        print('5. Export Inventory to Excel')
        print('6. Log out')
        choice = input('Enter your choice: ')
        if choice == '1':
            inventory.add_item()
        elif choice == '2':
            inventory.edit_item()
        elif choice == '3':
            inventory.remove_item()
        elif choice == '4':
            inventory.display_collection()
        elif choice == '5':
            inventory.export_to_excel()
        elif choice == '6':
            print('Logging out...')
            auth.update_user_inventory(user_email, inventory.collection)
            auth.save_user_inventories()
            auth.logout()
            break
        else:
            print('Invalid choice, please try again.')

if _name_ == '_main_':
    main_menu()