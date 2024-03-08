from models.__init__ import CONN, CURSOR
from models.master import Master
from models.store_one import Store_One
from models.store_two import Store_Two
from models.store_three import Store_Three

def seed_database():
    #Table Reset
    Store_One.drop_table()
    Store_Two.drop_table()
    Store_Three.drop_table()
    Master.drop_table()
    Store_One.create_table()
    Store_Two.create_table()
    Store_Three.create_table()

    # Table Seed Data

    #Initialize items inside of Master list
    item1 = Master.create("Boston Red Sox Hat", 78592982, 29.99)
    item2 = Master.create("New England Maple Syrup", 493929322, 6.99)
    item3 = Master.create("Boston Baked Beans", 432883, 8.99)
    item4 = Master.create("Superbowl Ring", 2841913, 2999999.99)
    item5 = Master.create("$25 Dunkin Donuts Gift Card", 999373292, 23.99)

    #Initialize Store Stock
    Store_One.create(item1.id, 23)
    Store_One.create(item2.id, 8)
    Store_One.create(item3.id, 239)
    Store_One.create(item4.id, 5)
    Store_One.create(item5.id, 21)
    Store_Two.create(item1.id, 23)
    Store_Two.create(item2.id, 8)
    Store_Two.create(item3.id, 239)
    Store_Two.create(item4.id, 5)
    Store_Two.create(item5.id, 21)
    Store_Three.create(item1.id, 23)
    Store_Three.create(item2.id, 8)
    Store_Three.create(item3.id, 239)
    Store_Three.create(item4.id, 5)
    Store_Three.create(item5.id, 21)