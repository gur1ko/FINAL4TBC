import hashlib
import json
import os
import re  # Import regular expression module
from inventory import Inventory

class Auth:
    def __init__(self, user_db_file='users.json'):
        self.user_db_file = user_db_file
        self.users = self.load_users()
        self.user_inventories = self.load_user_inventories()
        self.current_user_email = None

    def load_users(self):
        if os.path.exists(self.user_db_file):
            with open(self.user_db_file, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_users(self):
        with open(self.user_db_file, 'w') as file:
            json.dump(self.users, file)

    def load_user_inventories(self):
        if os.path.exists('user_inventories.json'):
            with open('user_inventories.json', 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_user_inventories(self):
        with open('user_inventories.json', 'w') as file:
            json.dump(self.user_inventories, file)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def is_valid_gmail(self, email):
        return email.endswith('@gmail.com')

    def is_valid_password(self, password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True

    def register(self):
        email = input('Enter your email (@gmail.com): ')
        if not self.is_valid_gmail(email):
            print('Invalid email. Please use an email ending with @gmail.com.')
            return False
        if email in self.users:
            print('Email already registered.')
            return False

        while True:
            password = input('Enter a password (at least: 8 symbols, one number, one symbol, one big letter): ')
            if self.is_valid_password(password):
                break
            else:
                print('Password does not meet the criteria. Please try again.')

        self.users[email] = self.hash_password(password)
        self.user_inventories[email] = []
        self.save_users()
        self.save_user_inventories()
        print('Registration successful.')
        return True

    def login(self):
        email = input('Enter your email (@gmail.com): ')
        if not self.is_valid_gmail(email):
            print('Invalid email. Please use an email ending with @gmail.com.')
            return False
        password = input('Enter your password: ')
        if email in self.users and self.users[email] == self.hash_password(password):
            print('Login successful.')
            self.current_user_email = email
            return True
        else:
            print('Invalid email or password.')
            return False

    def logout(self):
        self.current_user_email = None

    def get_current_user_email(self):
        return self.current_user_email

    def get_user_inventory(self, user_email):
        if user_email in self.user_inventories:
            return self.user_inventories[user_email]
        else:
            inventory = Inventory()
            self.user_inventories[user_email] = inventory.collection
            return inventory.collection

    def update_user_inventory(self, user_email, inventory):
        self.user_inventories[user_email] = inventory
