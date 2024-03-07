from models.__init__ import CONN, CURSOR
import os
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
    view_item_by_name,
    view_all_items,
    view_stock_by_id,
    view_stock_by_sku,
    view_stock_by_desc,
    view_all_stock,
    total_inventory_worth,
    store_inventory_worth,
    password_correct,
    password_incorrect,
    reset,
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
            reset_database_menu()
        else:
            print("Invalid Choice")

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

# STORE_ID VALIDATION NEEDED
def edit_store_list_menu():
    os.system(sweep_up_shop)
    store_list_text()
    store_id = input("> ")
    os.system(sweep_up_shop)
    while True:
        edit_store_list_text(store_id)
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            add_store_inv()
        elif choice == "2":
            remove_store_inv()
        elif choice == "3":
            update_store_inv()
        else:
            print("Invalid Choice")

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
            view_item_by_name()
        elif choice == "4":
            view_all_items()
        else:
            print("Invalid Choice")
#ALSO NEEDS STORE VALIDATION
def view_stock_menu():
    os.system(sweep_up_shop)
    store_list_text()
    input("> ")
    while True:
        view_stock_text()
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

def total_items_menu():
    pass

def reset_database_menu():
    while True:
        reset_database_text()
        password_entered = input(">>> ")
        if password_entered == "password":
            password_correct(main)
        else:
            password_incorrect(main)

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
    print("6. Admin")

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
    sql = """
        SELECT *
        FROM sys.Tables
    """
    tables = CURSOR.execute(sql).fetchall()
    for table in tables:
        if table == "master":
            pass
        else:
            print(f"{table}")


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
    print("2. Total inventory worth of one store")

def total_items_text():
    pass

def reset_database_text():
    os.system(sweep_up_shop)
    print("To enter admin controls, please enter password:")

if __name__ == "__main__":
    main()