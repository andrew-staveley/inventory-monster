from models.__init__ import CONN, CURSOR
from models.inventory import Inventory
from models.master import Master
from models.store import Store

def seed_database():
    #Table Reset
    Inventory.drop_table()
    Master.drop_table()
    Store.drop_table()
    Inventory.create_table()
    Master.create_table()
    Store.create_table()

    # Table Seed Data

    # X is Items
    x1 = Master.create("Boston Red Sox Hat", 78592982, 29.99)
    x2 = Master.create("New England Maple Syrup", 493929322, 6.99)
    x3 = Master.create("Boston Baked Beans", 432883, 8.99)
    x4 = Master.create("Superbowl Ring", 2841913, 2999999.99)
    x5 = Master.create("$25 Dunkin Donuts Gift Card", 999373292, 23.99)

    # Y is Stores
    y1 = Store.create("Seaport - Boston", "2000 Seaport Blvd, Boston, MA")
    y2 = Store.create("Downtown Crossing - Boston", "322 Tremont St, Boston, MA")

    #Store Inventory for Store 1 
    Inventory.create(y1.id, x3.id, 66)
    Inventory.create(y1.id, x2.id, 12)
    Inventory.create(y1.id, x1.id, 20)
    Inventory.create(y1.id, x4.id, 2)
    Inventory.create(y1.id, x5.id, 1)

    #Store Inventory for Store 2
    Inventory.create(y2.id, x1.id, 19)
    Inventory.create(y2.id, x2.id, 100)
    Inventory.create(y2.id, x3.id, 45)
    Inventory.create(y2.id, x4.id, 3)
    Inventory.create(y2.id, x5.id, 6)


seed_database()