from models.store_one import Store_One
from models.store_two import Store_Two
from models.store_three import Store_Three
from models.master import Master
import platform
import os
import time

sweep_up_shop = 'cls' if platform.system() == 'Windows' else 'clear'

def error_print(etype):
    if etype == "item_error":
        exc = "Item not found. Please doublecheck ID."
    elif etype == "store_error":
        exc = "Store not found. Please verify store."
    else:
        exc = etype
    os.system(sweep_up_shop)
    print("There was an error completing the request.")
    print("")
    print(exc)
    print("")
    print("Press Enter to Continue")
    print("")
    input("> ")

def controlled_print(message, message2 = ""):
    os.system(sweep_up_shop)
    print(message)
    print(message2)
    print("Press Enter to Continue")
    print("")
    input("> ")

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
        controlled_print(f"Success! Item {desc} Added")
    except Exception as exc:
        error_print(exc)

def remove_master_list():
    item_id = input("Enter the Item ID: ")
    if item_id := Master.find_by_id(item_id):
        item_id.delete()
        controlled_print(f"Item {item_id} has been deleted successfully.")
    else:
        error_print("item_error")


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
            controlled_print(f"Success in updating item {item_id}")
        except Exception as exc:
            error_print(exc)
    else:
        error_print("item_error")


def add_store_inv(store):
    if store == "1":
        item_id = input("Please enter the ID of an item from master: ")
        stock = input("Please enter the stock amount: ")
        try:
            store_item = Store_One.create(int(item_id), int(stock))
            controlled_print(f"Success! Item {store_item} has been added.")
        except Exception as exc:
            error_print(exc)
    elif store == "2":
        item_id = input("Please enter the ID of an item from master: ")
        stock = input("Please enter the stock amount: ")
        try:
            store_item = Store_Two.create(int(item_id), int(stock))
            controlled_print(f"Success! Item {store_item} has been added.")
        except Exception as exc:
            error_print(exc)
    elif store == "3":
        item_id = input("Please enter the ID of an item from master: ")
        stock = input("Please enter the stock amount: ")
        try:
            store_item = Store_Three.create(int(item_id), int(stock))
            controlled_print(f"Success! Item {store_item} has been added.")
        except Exception as exc:
            error_print(exc)
    else:
        error_print("store_error")

def remove_store_inv(store):
    if store == "1":
        item_id = input("Please Enter Item ID: ")
        if store := Store_One.find_by_id(item_id):
            store.delete()
            controlled_print("Item has been removed from the master list.")
        else:
            error_print("item_error")
    elif store == "2":
        item_id = input("Please Enter Item ID: ")
        if store := Store_Two.find_by_id(item_id):
            store.delete()
            controlled_print("Item has been removed from the master list.")
        else:
            error_print("item_error")
    elif store == "3":
        item_id = input("Please Enter Item ID: ")
        if store := Store_Three.find_by_id(item_id):
            store.delete()
            controlled_print("Item has been removed from the master list.")
        else:
            error_print("item_error")
    else:
        error_print("store_error")

def update_store_inv(store):
    if store == "1":
        item_id = input("Please Enter Item ID: ")
        if store := Store_One.find_by_id(item_id):
            try:
                stock = input("Enter Stock: ")
                store.stock = stock
                store.update()
                controlled_print("Success. Item Updated")
            except Exception as exc:
                error_print(exc)
    elif store == "2":
        item_id = input("Please Enter Item ID: ")
        if store := Store_Two.find_by_id(item_id):
            try:
                stock = input("Enter Stock: ")
                store.stock = stock
                store.update()
                controlled_print("Success. Item Updated")
            except Exception as exc:
                error_print(exc)
    elif store == "3":
        item_id = input("Please Enter Item ID: ")
        if store := Store_Three.find_by_id(item_id):
            try:
                stock = input("Enter Stock: ")
                store.stock = stock
                store.update()
                controlled_print("Success. Item Updated")
            except Exception as exc:
                error_print(exc)
    else:
        error_print("store_error")

def view_item_by_id():
    id_ = input("Enter the item's id: ")
    item = Master.find_by_id(id_)
    controlled_print(item) if item else controlled_print(f'Item {id_} not found')

def view_item_by_desc():
    desc = input("Enter the item's description: ")
    item = Master.find_by_desc(desc)
    controlled_print(item) if item else controlled_print(f"Item {desc} not found")

def view_item_by_sku():
    sku = input("Enter the item's SKU: ")
    sku_num = int(sku)
    item = Master.find_by_sku(sku_num)
    controlled_print(item) if item else controlled_print(f"Item {sku} not found")

def view_all_items():
    items = Master.get_all()
    os.system(sweep_up_shop)
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
        if item:
            controlled_print(f"Qty In Stock: {item.stock}", Master.find_by_id(item.item_id))
        else:
            error_print("item_error")
    elif store == "2":
        id_ = input("Please enter item ID: ")
        item = Store_Two.find_by_id(id_)
        if item:
            controlled_print(f"Qty In Stock: {item.stock}", Master.find_by_id(item.item_id))
        else:
            error_print("item_error")
    elif store == "3":
        id_ = input("Please enter item ID: ")
        item = Store_Three.find_by_id(id_)
        if item:
            controlled_print(f"Qty In Stock: {item.stock}", Master.find_by_id(item.item_id))
        else:
            error_print("item_error")
    else: 
        error_print("store_error")

def view_stock_by_sku(store):
    if store == "1":
        sku_ = input("Enter item SKU here: ")
        sku_num = int(sku_)
        item = Store_One.find_by_sku(sku_num)
        if item:
            store_item = Store_One.find_by_id(item)
            controlled_print(f"Qty In Stock: {store_item.stock}", Master.find_by_sku(sku_num))
        else:
            error_print("item_error")
    elif store == "2":
        sku_ = input("Enter item SKU here: ")
        sku_num = int(sku_)
        item = Store_Two.find_by_sku(sku_num)
        if item:
            store_item = Store_Two.find_by_id(item)
            controlled_print(f"Qty In Stock: {store_item.stock}", Master.find_by_sku(sku_num))
        else:
            error_print("item_error")
    elif store == "3":
        sku_ = input("Enter item SKU here: ")
        sku_num = int(sku_)
        item = Store_Three.find_by_sku(sku_num)
        if item:
            store_item = Store_Three.find_by_id(item)
            controlled_print(f"Qty In Stock: {store_item.stock}", Master.find_by_sku(sku_num))
        else:
            error_print("item_error")
    else: 
        error_print("store_error")

def view_stock_by_desc(store):
    if store == "1":
        description = input("Enter Item Description: ")
        item = Store_One.find_by_desc(description)
        if item:
            store_item = Store_One.find_by_id(item)
            controlled_print(f"Qty In Stock: {store_item.stock}", Master.find_by_id(store_item.item_id))
        else:
            error_print("item_error")
    elif store == "2":
        description = input("Enter Item Description: ")
        item = Store_Two.find_by_desc(description)
        if item:
            store_item = Store_Two.find_by_id(item)
            controlled_print(f"Qty In Stock: {store_item.stock}", Master.find_by_id(store_item.item_id))
        else:
            error_print("item_error")
    elif store == "3":
        description = input("Enter Item Description: ")
        item = Store_Three.find_by_desc(description)
        if item:
            store_item = Store_Three.find_by_id(item)
            controlled_print(f"Qty In Stock: {store_item.stock}", Master.find_by_id(store_item.item_id))
        else:
            error_print("item_error")
    else: 
        error_print("store_error")

def view_all_stock(store):
    if store == "1":
        items = Store_One.get_all()
        os.system(sweep_up_shop)
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
        os.system(sweep_up_shop)
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
        os.system(sweep_up_shop)
        for item in items:
            item_info = Master.find_by_id(item.item_id)
            print(item_info)
            print(item)
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
    else: 
        error_print("store_error")

def total_inventory_worth():
    items = Master.get_all()
    total_value = 0
    os.system(sweep_up_shop)
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
        items = Master.get_all()
        total_value = 0
        stock = 0
        os.system(sweep_up_shop)
        for item in items:
            store_item = Store_One.find_by_id(item.id)
            stock = store_item.stock
            print(f"Total {item.desc} Value: $", stock * item.price)
            print(item)
            total_value += (stock * item.price)
        print(f"Total Inventory Value: ${total_value}")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
    elif store == "2":
        items = Master.get_all()
        total_value = 0
        stock = 0
        os.system(sweep_up_shop)
        for item in items:
            store_item = Store_Two.find_by_id(item.id)
            stock = store_item.stock
            print(f"Total {item.desc} Value: $", stock * item.price)
            print(item)
            total_value += (stock * item.price)
        print(f"Total Inventory Value: ${total_value}")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
    elif store == "3":
        items = Master.get_all()
        total_value = 0
        stock = 0
        os.system(sweep_up_shop)
        for item in items:
            store_item = Store_Three.find_by_id(item.id)
            stock = store_item.stock
            print(f"Total {item.desc} Value: $", stock * item.price)
            print(item)
            total_value += (stock * item.price)
        print(f"Total Inventory Value: ${total_value}")
        print("")
        print("Press Enter to Continue")
        print("")
        input("> ")
    else: 
        error_print("store_error")
