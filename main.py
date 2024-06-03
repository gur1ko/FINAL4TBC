from inventory import add_item, update_item, delete_item, show_inventory, load_inventory, save_inventory

# Main menu
def main_menu():
    while True:
        print('Inventory Management System')
        print('1. Add Item')
        print('2. Update Item')
        print('3. Delete Item')
        print('4. Show Inventory')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            show_inventory()
        elif choice == '5':
            break
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    load_inventory()
    main_menu()
    save_inventory()
