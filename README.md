# Inventory Monster

## A Python based CLI Application that uses ORM methods with SQLite3 to interact with an inventory database system.

This is a project made by Andrew Staveley for Flatiron School.

This program allows for a user to interact with a database that is setup for a small chain of stores.
Each store has its own table with the item id and stock. The item id relates back to the item information
stored inside of the master table inside of the database. Each item inside of the master table has a description,
sku, and price. 

### Admin Menu

The admin menu (option 6) allows the primary user to completely reset the database to a small set of items.
The current password for the admin menu is:
`password`
To change this password, line 28 in `inventory-monster/library/cli.py`