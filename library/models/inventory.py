from models.__init__ import CURSOR, CONN
from models.store import Store
from models.master import Master

class Inventory:
    
    all = {}

    def __init__(self, store_id, item_id, stock, id=None):
        self.id = id
        self.store_id = store_id
        self.item_id = item_id
        self.stock = stock

    @property
    def store_id(self):
        return self._store_id
    
    @store_id.setter
    def store_id(self, store_id):
        if type(store_id) is int and Store.find_by_id(store_id):
            self._store_id = store_id
        else:
            raise ValueError("Store ID must match with a store. Use 'List Stores' to see each store's ID.")
        
    @property
    def item_id(self):
        return self._item_id
    
    @item_id.setter
    def item_id(self, item_id):
        if type(item_id) is int and Master.find_by_id(item_id):
            self._item_id = item_id
        else:
            raise ValueError("Item ID must represent an item in the master table of the database")
        
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, stock):
        if isinstance(stock, int):
            self._stock = stock
        else:
            raise ValueError("Stock must be an integer")