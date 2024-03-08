from models.__init__ import CURSOR, CONN
from models.master import Master

class Store_Three:
    
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
        if type(store_id) is int and Store_Three.find_by_id(store_id):
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
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS store_three
            id INTEGER PRIMARY KEY,
            item_id INT,
            store_id INT,
            stock INT,
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS store_three
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO store_three (store_id, item_id, stock)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.store_id, self.item_id, self.stock))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE store_three
            SET store_id = ?, item_id = ?, stock= ?
            WHERE id = ?
        """
        CURSOR.execute(sql(self.store_id, self.item_id, self.stock))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM store_three
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, store_id, item_id, stock):
        item = cls(store_id, item_id, stock)
        item.save()
        return item

    @classmethod
    def instance_from_db(cls, row):
        item = cls.all.get(row[0])
        if item:
            item.store_id = row[1]
            item.item_id = row[2]
            item.stock = row[3]
        else:
            item = cls(row[1], row[2], row[3])
            item.id = row[0]
            cls.all[item.id] = item
        return item
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM store_three
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM store_three
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """"
            SELECT *
            FROM store_three
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name)).fetchone()
        return cls.instance_from_db(row) if row else None