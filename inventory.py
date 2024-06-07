import pandas as pd
from datetime import datetime

class Inventory:
    def __init__(self):
        self.collection = []
        self.index_counter = 0

    def generate_index(self):
        self.index_counter += 1
        return f"G{self.index_counter:03d}"

    def add_item(self):
        item = {}
        item_index = self.generate_index()
        item['Index'] = item_index
        
        while True:
            item_type = input("Enter type (coin/banknote): ").lower()
            if item_type in ['coin', 'banknote']:
                item['Type'] = item_type
                break
            else:
                print("Invalid type. Please enter 'coin' or 'banknote'.")

        item['Country'] = input("Enter country: ")
        item['Denomination'] = input("Enter denomination: ")
        item['Currency'] = input("Enter currency (GEL, USD...): ").upper()
        
        while True:
            year = input("Enter year: ")
            if year.isdigit() and int(year) <= datetime.now().year:
                item['Year'] = int(year)
                break
            else:
                print("Invalid year. Please enter a valid year.")

        while True:
            condition = input("Enter condition(bad/ poor/ fair/ good/ very good/ excellent): ").lower()
            if condition in ['bad', 'poor', 'fair', 'good', 'very good', 'excellent']:
                item['Condition'] = condition
                break
            else:
                print("Invalid condition. Please enter one of: bad, poor, fair, good, very good, excellent.")

        item['Material'] = input("Enter material: ")
        
        while True:
            acquisition_date = input("Enter date of acquisition (dd/mm/yy): ")
            try:
                datetime.strptime(acquisition_date, '%d/%m/%y')
                item['Date of Acquisition'] = acquisition_date
                break
            except ValueError:
                print("Invalid date format. Please enter date in dd/mm/yy format.")

        while True:
            purchase_price = input("Enter purchase price (in GEL): ")
            if purchase_price.replace('.', '', 1).isdigit():
                item['Purchase Price'] = float(purchase_price)
                break
            else:
                print("Invalid purchase price. Please enter a valid number.")

        while True:
            estimated_value = input("Enter estimated value (in GEL): ")
            if estimated_value.replace('.', '', 1).isdigit():
                item['Estimated Value'] = float(estimated_value)
                break
            else:
                print("Invalid estimated value. Please enter a valid number.")

        self.collection.append(item)
        print(f"Item {item_index} added successfully.")

    def edit_item(self):
        index = input("Enter the index of the item to edit (e.g., G001): ").upper()
        for item in self.collection:
            if item['Index'] == index:
                print(f"Editing item: {item}")
                # Implement editing logic here
                print(f"Item {index} updated successfully.")
                return
        print("Wrong index. Please try again.")

    def remove_item(self):
        index = input("Enter the index of the item to remove (e.g., G001): ").upper()
        for item in self.collection:
            if item['Index'] == index:
                self.collection.remove(item)
                print(f"Item {index} removed successfully.")
                return
        print("Wrong index. Please try again.")

    def display_collection(self):
        if self.collection:
            for item in self.collection:
                print(f"{item['Index']}: {item}")
        else:
            print("Collection is empty.")

    def export_to_excel(self):
        if self.collection:
            df = pd.DataFrame(self.collection)
            df.to_excel('collection1.xlsx', index=False)
            print("Collection exported to collection.xlsx successfully.")
        else:
            print("Collection is empty. Nothing to export.")