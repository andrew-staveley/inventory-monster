from models.__init__ import CURSOR, CONN

class Master:

    all = {}

    def __init__(self, desc, sku, price, id=None):
        self.id = id
        self.desc = desc
        self.sku = sku
        self.price = price

    @property
    def desc(self):
        return self._desc
    
    @desc.setter
    def desc(self, desc):
        if isinstance(desc, str) and len(desc):
            self._desc = desc
        else:
            raise ValueError("Item description must be a non-empty string")
        
    @property
    def sku(self):
        return self._sku
    
    @sku.setter
    def sku(self, sku):
        if isinstance(sku, int) and (len(sku) >= 3 and len(sku) <= 10):
            self._sku = sku
        else:
            raise ValueError("SKU must be an integer between 3 and 10 characters")
        
    @property
    def price(self):
        return self._price
    ### Update price formatting requirements###
    @price.setter
    def price(self, price):
        if isinstance(price, float) and (price > 0.00):
            self._price = price
        else:
            raise ValueError("Price must be a number with two decimals, greater than 0.00")