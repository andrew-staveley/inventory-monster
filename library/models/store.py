from models.__init__ import CURSOR, CONN

class Store:
    
    all = {}

    def __init__(self, name, location, id=None):
        self.name = name
        self.location = location

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Location must be a non-empty string")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS stores;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO stores (name, location)
            VALUES = (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location): 
        store = cls(name, location)
        store.save()
        return store
    
    def update(self):
        sql = """
            UPDATE stores
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM stores
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        store = cls.all.get(row[0])
        if store:
            store.name = row[1]
            store.location = row[2]
        else:
            store = cls(row[1], row[2])
            store.id = row[0]
            cls.all[store.id] = store
        return store

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM stores
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM stores
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name)).fetchone()
        return cls.instance_from_db(row) if row else None