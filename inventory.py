import pandas as pd
import json
import os
from datetime import datetime
import statistics

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
            condition = input("Enter condition (bad/poor/fair/good/very good/excellent): ").lower()
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
                    condition = input("Enter condition (bad/poor/fair/good/very good/excellent): ").lower()
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
            print(f"Your Inventory ({len(self.collection)} items):")
            for item in self.collection:
                print(f"{item['Index']}: {item}")
        else:
            print("Your inventory is empty.")

    def export_to_excel(self):
        if self.collection:
            df = pd.DataFrame(self.collection)
            df.to_excel('collection.xlsx', index=False)
            print("Collection exported to collection.xlsx successfully.")
        else:
            print("Collection is empty. Nothing to export.")

    def search_inventory(self):
        if not self.collection:
            print("Your inventory is empty.")
            return

        search_options = {
            '1': 'Index',
            '2': 'Type',
            '3': 'Country',
            '4': 'Denomination',
            '5': 'Currency',
            '6': 'Year',
            '7': 'Condition',
            '8': 'Material',
            '9': 'Date of Acquisition',
            '10': 'Purchase Price',
            '11': 'Estimated Value'
        }

        print("Search by:")
        for option, field in search_options.items():
            print(f"{option}. {field}")

        choice = input("Enter your choice: ")

        if choice in search_options:
            search_field = search_options[choice]
            search_value = input(f"Enter the {search_field.lower()} to search for: ")

            matched_items = [item for item in self.collection if str(item[search_field]).lower() == search_value.lower()]

            if matched_items:
                print(f"Items matching {search_field}: {search_value}")
                for item in matched_items:
                    print(f"{item['Index']}: {item}")
            else:
                print(f"No items found with {search_field}: {search_value}")
        else:
            print("Invalid choice. Please try again.")

    def calculate_statistics(self):
        if not self.collection:
            print("Your inventory is empty. No statistics to calculate.")
            return

        print("Inventory Statistics:")
        # Calculate mode for categorical fields
        print("\nMode:")
        types = [item['Type'] for item in self.collection]
        print(f"Type: {statistics.mode(types)}")

        countries = [item['Country'] for item in self.collection]
        print(f"Country: {statistics.mode(countries)}")

        denominations = [item['Denomination'] for item in self.collection]
        print(f"Denomination: {statistics.mode(denominations)}")

        currencies = [item['Currency'] for item in self.collection]
        print(f"Currency: {statistics.mode(currencies)}")

        years = [item['Year'] for item in self.collection]
        print(f"Year: {statistics.mode(years)}")

        conditions = [item['Condition'] for item in self.collection]
        print(f"Condition: {statistics.mode(conditions)}")

        materials = [item['Material'] for item in self.collection]
        print(f"Material: {statistics.mode(materials)}")

        # Calculate mean for numerical fields
        print("\nMean:")
        purchase_prices = [item['Purchase Price'] for item in self.collection]
        print(f"Purchase Price: {statistics.mean(purchase_prices):.2f} GEL")

        estimated_values = [item['Estimated Value'] for item in self.collection]
        print(f"Estimated Value: {statistics.mean(estimated_values):.2f} GEL")

        # Calculate total valuation and total purchase price
        total_valuation = sum(item['Estimated Value'] for item in self.collection)
        total_purchase_price = sum(item['Purchase Price'] for item in self.collection)
        print(f"\nTotal Valuation of the Collection: {total_valuation:.2f} GEL")
        print(f"Total Purchase Price of the Collection: {total_purchase_price:.2f} GEL")
