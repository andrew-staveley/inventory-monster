from models.__init__ import CONN, CURSOR
from seed import seed_database
import os
import time
from helpers import (
    sweep_up_shop,
    exit_program,
    add_master_list,
    remove_master_list,
    update_master_list,
    add_store_inv,
    remove_store_inv,
    update_store_inv,
    view_item_by_id,
    view_item_by_desc,
    view_item_by_sku,
    view_all_items,
    view_stock_by_id,
    view_stock_by_sku,
    view_stock_by_desc,
    view_all_stock,
    total_inventory_worth,
    store_inventory_worth,
    )

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            edit_master_list_menu()
        elif choice == "2":
            edit_store_list_menu()
        elif choice == "3":
            view_item_menu()
        elif choice == "4":
            view_stock_menu()
        elif choice == "5":
            total_inventory_menu()
        elif choice == "6":
            total_items_menu()
        elif choice == "7":
            reset_database_menu(main)
        else:
            print("Invalid Choice")
            time.sleep(2)

def edit_master_list_menu():
    while True:
        edit_master_list_text()
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
            time.sleep(2)

# STORE_ID VALIDATION NEEDED
def edit_store_list_menu():
    os.system(sweep_up_shop)
    store_list_text()
    store = input("> ")
    os.system(sweep_up_shop)
    while True:
        edit_store_list_text(store)
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            add_store_inv(store)
        elif choice == "2":
            remove_store_inv(store)
        elif choice == "3":
            update_store_inv(store)
        else:
            print("Invalid Choice")
            time.sleep(2)

def view_item_menu():
    while True:
        view_item_text()
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            view_item_by_id()
        elif choice == "2":
            view_item_by_desc()
        elif choice == "3":
            view_item_by_sku()
        elif choice == "4":
            view_all_items()
        else:
            print("Invalid Choice")
            time.sleep(2)

#ALSO NEEDS STORE VALIDATION
def view_stock_menu():
    os.system(sweep_up_shop)
    store_list_text()
    store = input("> ")
    while True:
        view_stock_text(store)
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            view_stock_by_id()
        elif choice == "2":
            view_stock_by_sku()
        elif choice == "3":
            view_stock_by_desc()
        elif choice == "4":
            view_all_stock()
        else:
            print("Invalid Choice")
            time.sleep(2)

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
            store_inventory_worth()
        else:
            print("Invalid Option")
            time.sleep(2)

def total_items_menu():
    pass

def reset_database_menu(cb):
    while True:
        reset_database_text()
        password_entered = input(">>> ")
        if password_entered == "password":
            os.system(sweep_up_shop)
            print("Hello User, are you sure you want to reset the database?")
            print("Note: This will seed the database with sample data")
            print("y / n")
            yn = input(">>> ")
            if yn == "y":
                os.system(sweep_up_shop)
                print("Working...")
                time.sleep(3)
                seed_database()
                print("Success")
                print("")
                print("Press Enter to Continue")
                print("")
                input("> ")
                main()
            elif yn == "n":
                main()
            else:
                print("Invalid Input")
                time.sleep(2)
        else:
            os.system(sweep_up_shop)
            print("Password Incorrect")
            time.sleep(2)
            os.system(sweep_up_shop)
            main()

def menu():
    os.system(sweep_up_shop)
    print("Welcome to Inventory Monster")
    print("Please Select an Option Below:")
    print("0. Exit Program")
    print("1. Edit Master Inventory")
    print("2. Edit Store Inventory")
    print("3. View Item Information")
    print("4. View Item Stock")
    print("5. Inventory Worth")
    print("6. Total Inventory (Under Construction)")
    print("7. Admin")

def edit_master_list_text():
    os.system(sweep_up_shop)
    print("* EDITING ITEMS IN MASTER LIST *")
    print("Please Select an Option Below:")
    print("0. Main Menu")
    print("1. Add New Item to Master")
    print("2. Remove Item from Master")
    print("3. Change Item from Master")

def edit_store_list_text(store_id):
    os.system(sweep_up_shop)
    print(f"* EDITING STORE {store_id} INVENTORY *")
    print("Please Select an Option Below:")
    print("0. Main Menu")
    print("1. Add New Stock")
    print("2. Remove Stock")
    print("3. Update Stock")

def store_list_text():
    print("Please Select a Store Below")
    print("1. Store One")
    print("2. Store Two")
    print("3. Store Three")


def view_item_text():
    os.system(sweep_up_shop)
    print("How would you like to search for your item?")
    print("Please select an option.")
    print("0. Main Menu")
    print("1. By ID")
    print("2. By Description")
    print("3. By SKU")
    print("4. List All Items in Master Inventory")

def view_stock_text(store_id):
    os.system(sweep_up_shop)
    print(f"* VIEWING INVENTORY FOR STORE {store_id} *")
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
    print("2. Total inventory worth of one store")

def total_items_text():
    pass

def reset_database_text():
    os.system(sweep_up_shop)
    print("To enter admin controls, please enter password:")

if __name__ == "__main__":
    main()