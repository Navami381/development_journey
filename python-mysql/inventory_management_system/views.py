from mysql import connector

class inventoryCreateListRetrieveUpdateDelete:

    def __init__(self, user=None, password=None):
        if user == None or password == None:
            raise Exception("username and password required..")

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="inventory_db"
        )
        self.cursor = self.connection.cursor()

    def post(self, **kwargs):
        db_cols = (
            "product_name",
            "sku",
            "category",
            "quantity",
            "reorder_threshold",
            "price",
            "status",
            "warehouse_zone"
        )
        difference = set(db_cols).difference(kwargs.keys())
        if difference:
            raise Exception(f"{difference} required")

        col_str = ",".join(db_cols)

        query = f"""insert into inventory
        ({col_str})
        values(%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = list(kwargs.values())
        self.cursor.execute(query, values)
        self.connection.commit()
        print("record has been added....")

    def get(self):
        query = "select * from inventory"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        for inventory in records:
            print(inventory)

    def retrieve(self, id=None):
        query = "select * from inventory where id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        record = self.cursor.fetchone()
        print(record)

    def put(self, id=None, **kwargs):
        place_holder = ""

        for k in kwargs.keys():
            place_holder += k + "=%s,"

        place_holder = place_holder.rstrip(",")
        query = f"update inventory set {place_holder} where id=%s"
        values = list(kwargs.values())
        values.append(id)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("record has been updated....")

    def filter(self, **kwargs):
        # kwargs={status="low_stock",category="electronics"}

        place_holder = ""
        for k in kwargs.keys():
            place_holder += k + "=%s and "

        place_holder = place_holder.rstrip("and ")
        query = f"select * from inventory where {place_holder}"
        values = list(kwargs.values())
        self.cursor.execute(query, values)
        records = self.cursor.fetchall()
        if records:

            for inventory in records:
                print(inventory)

        else:
            print("no records")

    def summary(self):
        query = """select category, count(*) as count
                   from inventory
                   group by category"""
        self.cursor.execute(query)
        category_summary = self.cursor.fetchall()
        status_summary_query = """select status, count(*) as count
                                 from inventory
                                 group by status"""
        self.cursor.execute(status_summary_query)
        status_summary = self.cursor.fetchall()
        print("category summary", category_summary)
        print("status summary", status_summary)

    def delete(self, id=None):
        query = "delete from inventory where id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("record has been deleted...")


inventory = inventoryCreateListRetrieveUpdateDelete(
    user="root",
    password="Password@123"
)
print(inventory.connection)
# inventory.post(
#     product_name="Bluetooth Speaker",
#     sku="BS005",
#     category="Electronics",
#     quantity=0,
#     reorder_threshold=5,
#     price=1999.00,
#     status="out_of_stock",
#     warehouse_zone="C1"
# )
#inventory.get()
#inventory.retrieve(id=1)
# inventory.put(
#      id=1,
#      quantity=20,
#     status="available"
# )
#inventory.delete(id=2)
#inventory.filter(status="low_stock")
#inventory.filter(category="Electronics")
inventory.summary()