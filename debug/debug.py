from library.models.__init__ import CONN, CURSOR
from library.models.master_model import Master
from library.models.store_model import Store
import ipdb

def reset_database():
    Master.drop_table()
    Store.drop_table()
    Master.create_table()
    Store.create_table()