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
            print('I know one good man who collects coins and banknotes, but whenever I meet him, he always complains about organizing his vast collection. That little story was my inspiration for this console application, and here it is. This application helps coin collectors manage their collections with ease. It provides features for user registration, login, and various inventory management functionalities. Features User Registration and Login: Register with a valid Gmail address and a strong password. Log in to access your personal collection. Log out to secure your session. App Information: Get details about the application and its functionalities. Inventory Management: Add Item: Add new coins or banknotes to your collection with detailed information such as type, country, denomination, currency, year, condition, material, acquisition date, purchase price, and estimated value. Update Item: Edit existing items in your collection. Delete Item: Remove items from your collection. Show Inventory: Display your entire collection with all the details. Export Inventory to Excel: Export your collection to an Excel file for easy sharing and backup. Log in: Enter your registered Gmail address and password to log in. Register: Create a new account with your Gmail address and a strong password. Info: Learn about the application. Exit: Exit the application. User Menu (after logging in): Add Item: Add a new coin or banknote to your collection. Update Item: Edit an existing item in your collection. Delete Item: Remove an item from your collection. Show Inventory: Display all items in your collection. Export Inventory to Excel: Save your collection as an Excel file. Log out: Log out of your account.')
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
        print('5. Search in Inventory')
        print('6. Export Inventory to Excel')
        print('7. Calculate Inventory Statistics')
        print('8. Log out')
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
            inventory.search_inventory()
        elif choice == '6':
            inventory.export_to_excel()
        elif choice == '7':
            inventory.calculate_statistics()
        elif choice == '8':
            print('Logging out...')
            auth.update_user_inventory(user_email, inventory.collection)
            auth.save_user_inventories()
            auth.logout()
            break
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    main_menu()