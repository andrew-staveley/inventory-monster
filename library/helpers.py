from models.store_one import Store_One
from models.store_two import Store_Two
from models.store_three import Store_Three
from models.master import Master
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
    desc = input("Please Enter Item Desc: ")
    sku = input("Please Enter SKU: ")
    price = input("Please Enter Price in XXXX.xx Format: ")
    try:
        Master.create(desc, sku, price)
        os.system(sweep_up_shop)
        print(f"Success! Item {desc} Added")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
    except Exception as exc:
        os.system(sweep_up_shop)
        print("Error Creating Item")
        print("")
        print(exc)
        print("")
        print("Press Enter To Continue")
        print("")
        input("> ")

def remove_master_list():
    item_id = input("Enter the Item ID: ")
    if item_id := Master.find_by_id(item_id):
        item_id.delete()
        os.system(sweep_up_shop)
        print(f"Item {item_id} has been deleted successfully.")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
    else:
        os.system(sweep_up_shop)
        print(f"Error Removing Item {item_id}")
        print("")
        print("Item not found. Please double-check ID")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")


def update_master_list():
    item_id = input("Enter the Item ID: ")
    if item_id := Master.find_by_id(item_id):
        try:
            desc = input("Enter new item description: ")
            item_id.desc = desc
            sku = input("Enter new item SKU: ")
            item_id.sku = sku
            price = input("Enter new item price: ")
            item_id.price = price
            item_id.update()
            os.system(sweep_up_shop)
            print(f"Success in updating item {item_id}")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        except Exception as exc:
            os.system(sweep_up_shop)
            print(f"Error updating item {item_id}")
            print("")
            print(exc)
            print("")
            print("Press Enter to Continue")
            input("> ")
    else:
        os.system(sweep_up_shop)
        print(f"Error Updating {item_id}")
        print("")
        print("Item not found. Double-check item ID.")
        print("")
        print("Press Enter to Continue")
        print("> ")


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
