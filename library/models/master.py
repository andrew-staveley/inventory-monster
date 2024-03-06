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
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS master (
            id INTEGER PRIMARY KEY,
            name TEXT
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS master;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO master (desc, sku, price)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.desc, self.sku, self.price))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, desc, sku, price):
        master = cls(desc, sku, price)
        master.save()
        return master
    
    def update(self):
        sql = """
            UPDATE master
            SET desc = ?, sku = ?, price = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.desc, self.sku, self.price))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM master
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        master = cls.all.get(row[0])
        if master:
            master.desc = row[1]
            master.sku = row[2]
            master.price = row[3]
        else:
            master = cls(row[1], row[2], row[3])
            master.id = row[0]
            cls.all[master.id] = master
        return master
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM master
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM master
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_desc(cls, desc):
        sql = """
            SELECT *
            FROM master
            WHERE desc is ?
        """
        row = CURSOR.execute(sql, (desc,)).fetchone()
        return cls.instance_from_db(row) if row else None
