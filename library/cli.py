import platform
import os
from helpers import (
    exit_program,
    full_master_list,
    update_master_list,
    add_master_list,
    remove_master_list,
    find_item_by_name,
    find_item_by_id,
    find_item_by_sku,
    list_stores,
    add_store,
    remove_store,
    update_store,
    add_stock,
    remove_stock,
    update_stock,
    list_items_store,
    find_store_by_id,
    find_store_by_name,
    check_store_stock_by_id,
    check_store_stock_by_name,
    total_inventory_worth,
    store_total_inventory_worth,
    total_inventory_worth_per_item,
    store_total_inventory_worth_per_item,
    password_correct,
    password_incorrect,
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            edit_items_master_list_menu()
        elif choice == "2":
            edit_store_list_menu()
        elif choice == "3":
            edit_store_stock_menu()
        elif choice == "4":
            find_item_master_menu()
        elif choice == "5":
            find_store_menu()
        elif choice == "6":
            store_stock_menu()
        elif choice == "7":
            total_inventory_menu()
        elif choice == "8":
            reset_database_menu()
        else:
            print("Invalid Choice")

def edit_items_master_list_menu():
    while True:
        edit_items_master_list_text()
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            add_master_list()
        elif choice == "2":
            remove_master_list()
        elif choice == "3":
            update_master_list()
        else:
            print("Invalid Choice")

def edit_store_list_menu():
    while True:
        edit_store_list_text()
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            add_store()
        elif choice == "2":
            remove_store()
        elif choice == "3":
            update_store()
        else:
            print("Invalid Choice")

def edit_store_stock_menu():
    os.system(sweep_up_shop)
    store_id = input("Please enter the ID of the store to change inventory: ")
    while True:
        edit_store_stock_text(store_id)
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            update_stock()
        else:
            print("Invalid Choice")

def find_item_master_menu():
    while True:
        find_item_master_text()
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            find_item_by_id()
        elif choice == "2":
            find_item_by_name()
        elif choice == "3":
            find_item_by_sku()
        elif choice == "4":
            full_master_list()
        else:
            print("Invalid Choice")

def find_store_menu():
    while True:
        find_store_text()
        choice = input("> ")
        if choice == "0":
            menu()
        elif choice == "1":
            find_store_by_id()
        elif choice == "2":
            find_store_by_name()
        elif choice == "3":
            list_stores()
        else:
            print("Invalid Choice")

def store_stock_menu():
    os.system(sweep_up_shop)
    store_id = input("Enter the Store ID for Inventory Searches: ")
    while True:
        store_stock_text()
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            check_store_stock_by_id()
        elif choice == "2":
            check_store_stock_by_name()
        elif choice == "3":
            list_items_store()
        else:
            print("Invalid Choice")

def total_inventory_menu():
    os.system(sweep_up_shop)
    while True:
        total_inventory_text()
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            total_inventory_worth()
        elif choice == "2":
            store_total_inventory_worth()
        elif choice == "3":
            total_inventory_worth_per_item()
        elif choice == "4":
            store_total_inventory_worth_per_item()

def reset_database_menu():
    while True:
        reset_database_text()
        password_entered = input(">>> ")
        if password_entered == "password":
            password_correct()
        else:
            password_incorrect()
def menu():
    os.system(sweep_up_shop)
    print("Welcome to Inventory Monster")
    print("Please Select an Option Below:")
    print("0. Exit Program")
    print("1. Edit Items Master List")
    print("2. Edit Store List")
    print("3. Edit Store Stock")
    print("4. Find Items")
    print("5. Find Stores")
    print("6. Find Store Stock")
    print("7. Total Inventory Worth")
    print("8. Reset Database")

def edit_items_master_list_text():
    os.system(sweep_up_shop)
    print("* EDITING ITEMS IN MASTER LIST *")
    print("Please Select an Option Below:")
    print("0. Main Menu")
    print("1. Add New Item to Master List")
    print("2. Remove Item from Master List")
    print("3. Update Item from Master List")

def edit_store_list_text():
    os.system(sweep_up_shop)
    print("* EDITING STORE LIST *")
    print("Please Select an Option Below:")
    print("0. Main Menu")
    print("1. Add New Store to List")
    print("2. Remove a Store from List")
    print("3. Update a Store from List")

def edit_store_stock_text(store_name):
    os.system(sweep_up_shop)
    print(f"* EDITING {store_name} *")
    print("0. Main Menu")
    print("1. Add New Item to Store Inventory")
    print("2. Remove Item from Store Inventory")
    print("3. Update Item in Store Inventory")

def find_item_master_text():
    os.system(sweep_up_shop)
    print("How would you like to search for your item?")
    print("Please select an option.")
    print("0. Main Menu")
    print("1. By ID")
    print("2. By Description")
    print("3. By SKU")
    print("4. List All Items in Master Inventory")

def find_store_text():
    os.system(sweep_up_shop)
    print("How would you like to search for the store?")
    print("0. Main Menu")
    print("1. By ID")
    print("2. By Name")
    print("3. List All Stores")

def store_stock_text(store_id):
    os.system(sweep_up_shop)
    print(f"How would you like to lookup Store #{store_id}")
    print("0. Main Menu")
    print("1. By ID")
    print("2. By Name")
    print("3. Show Entire Stock")

def total_inventory_text():
    os.system(sweep_up_shop)
    print("Which inventory would you like the value of?")
    print("Please select one below:")
    print("0. Main Menu")
    print("1. Total inventory worth of all stores")
    print("2. Total inventory of one store")
    print("3. Total inventory of a specific item across all stores")
    print("4. Total inventory of a specific item in one store")

def reset_database_text():
    os.system(sweep_up_shop)
    print("To enter admin controls, please enter password:")

sweep_up_shop = 'cls' if platform.system() == 'Windows' else 'clear'

sql = """
    USE inventory.db
    GO
    SELECT *
    FROM sys.Tables
    GO
"""
if __name__ == "__main__":
    main()