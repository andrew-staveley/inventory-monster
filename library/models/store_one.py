from models.__init__ import CURSOR, CONN
from models.master import Master

class Store_One:
    
    all = {}

    def __init__(self, item_id, stock, id=None):
        self.id = id
        self.item_id = item_id
        self.stock = stock
        
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
        if isinstance(int(stock), int):
            self._stock = stock
        else:
            raise ValueError("Stock must be an integer")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS store_one (
            id INTEGER PRIMARY KEY,
            item_id INT,
            stock INT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS store_one
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO store_one (item_id, stock)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.item_id, self.stock))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE store_one
            SET item_id = ?, stock= ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.item_id, self.stock, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM store_one
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, item_id, stock):
        item = cls(item_id, stock)
        item.save()
        return item

    @classmethod
    def instance_from_db(cls, row):
        item = cls.all.get(row[0])
        if item:
            item.item_id = row[1]
            item.stock = row[2]
        else:
            item = cls(row[1], row[2])
            item.id = row[0]
            cls.all[item.id] = item
        return item
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM store_one
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM store_one
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """"
            SELECT *
            FROM store_one
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name)).fetchone()
        return cls.instance_from_db(row) if row else None