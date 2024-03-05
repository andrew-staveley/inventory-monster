from library.models.__init__ import CONN, CURSOR
from library.models.master import Master
from library.models.store import Store
from library.models.inventory import StoreInventory
import ipdb

def reset_database():
    Master.drop_table()
    Store.drop_table()
    Master.create_table()
    Store.create_table()