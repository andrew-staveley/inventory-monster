from library.models.store_one import Store_One
from models.store_two import Store_Two
from models.store_three import Store_Three
from models.master import Master
from seed import seed_database
import platform
import os
import time

sweep_up_shop = 'cls' if platform.system() == 'Windows' else 'clear'

def exit_program():
    os.system(sweep_up_shop)
    print("Thank you for using Inventory Monster")
    time.sleep(2)
    os.system(sweep_up_shop)
    exit()

def add_master_list():
    pass

def remove_master_list():
    pass

def update_master_list():
    pass

def add_store_inv():
    pass

def remove_store_inv():
    pass

def update_store_inv():
    pass

def view_item_by_id():
    pass

def view_item_by_desc():
    pass

def view_item_by_name():
    pass

def view_all_items():
    pass

def view_stock_by_id():
    pass

def view_stock_by_sku():
    pass

def view_stock_by_desc():
    pass

def view_all_stock():
    pass

def total_inventory_worth():
    pass

def store_inventory_worth():
    pass

def password_correct(main):
    os.system(sweep_up_shop)
    print("Hello User, are you sure you want to reset the database?")
    print("Note: This will seed the database with sample data")
    print("Y / N")
    yn = input(">>> ")
    if yn == "Y" or "y":
        reset()
    elif yn == "N" or "n":
        main()
    else:
        print("Invalid Input")

def password_incorrect(main):
    os.system(sweep_up_shop)
    print("Password Incorrect")
    time.sleep(2)
    print("Loser")
    time.sleep(1)
    main()

def reset(main):
    os.system(sweep_up_shop)
    print("Working...")
    time.sleep(3)
    seed_database()
    main()