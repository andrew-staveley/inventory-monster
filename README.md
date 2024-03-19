# Inventory Monster

## A Python based CLI Application that uses ORM methods with SQLite3 to interact with an inventory database system.

This is a project made by Andrew Staveley for Flatiron School.

This program allows for a user to interact with a database that is setup for a small chain of stores.
Each store has its own table with the item id and stock. The item id relates back to the item information
stored inside of the master table inside of the database. Each item inside of the master table has a description,
sku, and price. 

### Admin Menu

The admin menu (option 6) allows the primary user to completely reset the database to a small set of items.
The current password for the admin menu is `password`.
To change the password, update `user_password` on line 28 in `inventory-monster/library/cli.py`
Please note that this must be a string, as it is later compared to a string entered.

### Resetting Database

As said above, the admin menu allows the user to reset the database. If you would like to update
the information that gets added into the database, update `inventory-monster/library/seed.py` to the
information of your choosing.