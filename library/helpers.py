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


def add_store_inv(store):
    if store == "1":
        item_id = input("Please enter the ID of an item from master: ")
        stock = input("Please enter the stock amount: ")
        try:
            os.system(sweep_up_shop)
            store_item = Store_One.create(int(item_id), int(stock))
            print(f"Success! Item {store_item} has been added.")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        except Exception as exc:
            os.system(sweep_up_shop)
            print("Error adding stock.")
            print("")
            print(exc)
            print("")
            print("Press Enter to Continue")
            input("> ")
    elif store == "2":
        item_id = input("Please enter the ID of an item from master: ")
        stock = input("Please enter the stock amount: ")
        try:
            os.system(sweep_up_shop)
            store_item = Store_Two.create(int(item_id), int(stock))
            print(f"Success! Item {store_item} has been added.")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        except Exception as exc:
            os.system(sweep_up_shop)
            print("Error adding stock.")
            print("")
            print(exc)
            print("")
            print("Press Enter to Continue")
            input("> ")
    elif store == "3":
        item_id = input("Please enter the ID of an item from master: ")
        stock = input("Please enter the stock amount: ")
        try:
            os.system(sweep_up_shop)
            store_item = Store_Three.create(int(item_id), int(stock))
            print(f"Success! Item {store_item} has been added.")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        except Exception as exc:
            os.system(sweep_up_shop)
            print("Error adding stock.")
            print("")
            print(exc)
            print("")
            print("Press Enter to Continue")
            input("> ")
    else:
        os.system(sweep_up_shop)
        print("Error")
        print("")
        print("Store does not exist. Double check store")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")

def remove_store_inv(store):
    if store == "1":
        item_id = input("Please Enter Item ID: ")
        if store := Store_One.find_by_id(item_id):
            store.delete()
            os.system(sweep_up_shop)
            print("Item has been removed from the master list.")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            os.system(sweep_up_shop)
            print("Error Deleting Item")
            print("")
            print("Item not Found.")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    elif store == "2":
        item_id = input("Please Enter Item ID: ")
        if store := Store_Two.find_by_id(item_id):
            store.delete()
            os.system(sweep_up_shop)
            print("Item has been removed from the master list.")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            os.system(sweep_up_shop)
            print("Error Deleting Item")
            print("")
            print("Item not Found.")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    elif store == "3":
        item_id = input("Please Enter Item ID: ")
        if store := Store_Three.find_by_id(item_id):
            store.delete()
            os.system(sweep_up_shop)
            print("Item has been removed from the master list.")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            os.system(sweep_up_shop)
            print("Error Deleting Item")
            print("")
            print("Item not Found.")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    else:
        os.system(sweep_up_shop)
        print("Error")
        print("")
        print("Store does not exist. Double check store")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")

def update_store_inv(store):
    if store == "1":
        item_id = input("Please Enter Item ID: ")
        if store := Store_One.find_by_id(item_id):
            try:
                stock = input("Enter Stock: ")
                store.stock = stock
                os.system(sweep_up_shop)
                store.update()
                print("Success. Item Updated")
                print("")
                print("Press Enter to Continue")
                print("")
                input("> ")
            except Exception as exc:
                print("Error Updating Item")
                print("")
                print(exc)
                print("")
                print("Press Enter to Continue")
                print("")
                input("> ")
    elif store == "2":
        item_id = input("Please Enter Item ID: ")
        if store := Store_Two.find_by_id(item_id):
            try:
                stock = input("Enter Stock: ")
                store.stock = stock
                os.system(sweep_up_shop)
                store.update()
                print("Success. Item Updated")
                print("")
                print("Press Enter to Continue")
                print("")
                input("> ")
            except Exception as exc:
                print("Error Updating Item")
                print("")
                print(exc)
                print("")
                print("Press Enter to Continue")
                print("")
                input("> ")
    elif store == "3":
        item_id = input("Please Enter Item ID: ")
        if store := Store_Three.find_by_id(item_id):
            try:
                stock = input("Enter Stock: ")
                store.stock = stock
                os.system(sweep_up_shop)
                store.update()
                print("Success. Item Updated")
                print("")
                print("Press Enter to Continue")
                print("")
                input("> ")
            except Exception as exc:
                print("Error Updating Item")
                print("")
                print(exc)
                print("")
                print("Press Enter to Continue")
                print("")
                input("> ")
    else:
        os.system(sweep_up_shop)
        print("Error")
        print("")
        print("Store does not exist. Double check store")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")

def view_item_by_id():
    id_ = input("Enter the item's id: ")
    item = Master.find_by_id(id_)
    os.system(sweep_up_shop)
    print(item) if item else print(f'Item {id_} not found')
    print("")
    print("Press Enter to Continue")
    print("")
    input("> ")

def view_item_by_desc():
    desc = input("Enter the item's description: ")
    item = Master.find_by_desc(desc)
    os.system(sweep_up_shop)
    print(item) if item else print(f"Item {desc} not found")
    print("")
    print("Press Enter to Continue")
    print("")
    input("> ")

def view_item_by_sku():
    sku = input("Enter the item's SKU: ")
    sku_num = int(sku)
    item = Master.find_by_sku(sku_num)
    os.system(sweep_up_shop)
    print(item) if item else print(f"Item {sku} not found")
    print("")
    print("Press Enter to Continue")
    print("")
    input("> ")

def view_all_items():
    items = Master.get_all()
    for item in items:
        print(item)
    print("")
    print("Press Enter to Continue")
    print("")
    input("> ")

def view_stock_by_id(store):
    if store == "1":
        id_ = input("Please enter item ID: ")
        item = Store_One.find_by_id(id_)
        os.system(sweep_up_shop)
        if item:
            print(f"Qty In Stock: {item.stock}")
            print(Master.find_by_id(item.item_id))
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            print("Item Not Found")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    elif store == "2":
        id_ = input("Please enter item ID: ")
        item = Store_Two.find_by_id(id_)
        os.system(sweep_up_shop)
        if item:
            print(f"Qty In Stock: {item.stock}")
            print(Master.find_by_id(item.item_id))
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            print("Item Not Found")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    elif store == "3":
        id_ = input("Please enter item ID: ")
        item = Store_Three.find_by_id(id_)
        os.system(sweep_up_shop)
        if item:
            print(f"Qty In Stock: {item.stock}")
            print(Master.find_by_id(item.item_id))
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            print("Item Not Found")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    else: 
        os.system(sweep_up_shop)
        print("Error")
        print("")
        print("Store does not exist. Double check store")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")

def view_stock_by_sku(store):
    if store == "1":
        sku_ = input("Enter item SKU here: ")
        sku_num = int(sku_)
        item = Store_One.find_by_sku(sku_num)
        os.system(sweep_up_shop)
        if item:
            store_item = Store_One.find_by_id(item)
            print(f"Qty In Stock: {store_item.stock}")
            print(Master.find_by_sku(sku_num))
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            print("Item Not Found")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    elif store == "2":
        sku_ = input("Enter item SKU here: ")
        sku_num = int(sku_)
        item = Store_Two.find_by_sku(sku_num)
        os.system(sweep_up_shop)
        if item:
            store_item = Store_Two.find_by_id(item)
            print(f"Qty In Stock: {store_item.stock}")
            print(Master.find_by_sku(sku_num))
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            print("Item Not Found")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    elif store == "3":
        sku_ = input("Enter item SKU here: ")
        sku_num = int(sku_)
        item = Store_Three.find_by_sku(sku_num)
        os.system(sweep_up_shop)
        if item:
            store_item = Store_Three.find_by_id(item)
            print(f"Qty In Stock: {store_item.stock}")
            print(Master.find_by_sku(sku_num))
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            print("Item Not Found")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    else: 
        os.system(sweep_up_shop)
        print("Error")
        print("")
        print("Store does not exist. Double check store")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")

def view_stock_by_desc(store):
    if store == "1":
        description = input("Enter Item Description: ")
        item = Store_One.find_by_desc(description)
        os.system(sweep_up_shop)
        if item:
            store_item = Store_One.find_by_id(item)
            print(f"Qty In Stock: {store_item.stock}")
            print(Master.find_by_id(store_item.item_id))
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            print("Item Not Found")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    elif store == "2":
        description = input("Enter Item Description: ")
        item = Store_Two.find_by_desc(description)
        os.system(sweep_up_shop)
        if item:
            store_item = Store_Two.find_by_id(item)
            print(f"Qty In Stock: {store_item.stock}")
            print(Master.find_by_id(store_item.item_id))
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            print("Item Not Found")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    elif store == "3":
        description = input("Enter Item Description: ")
        item = Store_Three.find_by_desc(description)
        os.system(sweep_up_shop)
        if item:
            store_item = Store_Three.find_by_id(item)
            print(f"Qty In Stock: {store_item.stock}")
            print(Master.find_by_id(store_item.item_id))
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
        else:
            print("Item Not Found")
            print("")
            print("Press Enter to Continue")
            print("")
            input("> ")
    else: 
        os.system(sweep_up_shop)
        print("Error")
        print("")
        print("Store does not exist. Double check store")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")

def view_all_stock(store):
    if store == "1":
        items = Store_One.get_all()
        for item in items:
            item_info = Master.find_by_id(item.item_id)
            print(item_info)
            print(item)
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
    elif store == "2":
        items = Store_Two.get_all()
        for item in items:
            item_info = Master.find_by_id(item.item_id)
            print(item_info)
            print(item)
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
    elif store == "3":
        items = Store_Three.get_all()
        for item in items:
            item_info = Master.find_by_id(item.item_id)
            print(item_info)
            print(item)
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
    else: 
        os.system(sweep_up_shop)
        print("Error")
        print("")
        print("Store does not exist. Double check store")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")


def total_inventory_worth():
    items = Master.get_all()
    total_value = 0
    for item in items:
        stock_one = Store_One.find_by_id(item.id)
        stock_two = Store_Two.find_by_id(item.id)
        stock_three = Store_Three.find_by_id(item.id)
        total_stock = stock_one.stock + stock_two.stock + stock_three.stock
        print(f"Total {item.desc} Value Across Stores: $", total_stock * item.price)
        print(item)
        total_value += (total_stock * item.price)
    print(f"Total Inventory Value: ${total_value}")
    print("")
    print("Press Enter to Continue")
    print("")
    input("> ")

def store_inventory_worth(store):
    if store == "1":
        pass
    elif store == "2":
        pass
    elif store == "3":
        pass
    else: 
        os.system(sweep_up_shop)
        print("Error")
        print("")
        print("Store does not exist. Double check store")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
