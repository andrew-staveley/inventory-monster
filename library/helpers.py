from models.inventory import Inventory
from models.master import Master
from models.store import Store
from cli import menu
from seed import seed_database
import platform
import os
import time

def sweep_up_shop():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def exit_program():
    os.system(sweep_up_shop)
    print("Thank you for using Inventory Monster")
    time.sleep(2)
    os.system(sweep_up_shop)
    exit()

def full_master_list():
    pass

def update_master_list():
    pass

def add_master_list():
    pass

def remove_master_list():
    pass

def find_item_by_name():
    pass

def find_item_by_id():
    pass

def find_item_by_sku():
    pass

def list_stores():
    pass

def add_store():
    pass

def remove_store():
    pass

def update_store():
    pass

def add_stock():
    pass

def remove_stock():
    pass

def update_stock():
    pass

def list_items_store():
    pass

def find_store_by_id():
    pass

def find_store_by_name():
    pass

def check_store_stock_by_id():
    pass

def check_store_stock_by_name():
    pass

def total_inventory_worth():
    pass

def store_total_inventory_worth():
    pass

def total_inventory_worth_per_item():
    pass

def store_total_inventory_worth_per_item():
    pass

def password_correct():
    os.system(sweep_up_shop)
    print("Hello User, are you sure you want to reset the database?")
    print("Note: This will seed the database with sample data")
    print("Y / N")
    yn = input(">>> ")
    if yn == "Y" or "y":
        reset()
    elif yn == "N" or "n":
        menu()
    else:
        print("Invalid Input")

def password_incorrect():
    os.system(sweep_up_shop)
    print("Password Incorrect")
    time.sleep(2)
    print("Loser")
    time.sleep(1)
    menu()

def reset():
    os.system(sweep_up_shop)
    print("Working...")
    time.sleep(3)
    seed_database()
    menu()