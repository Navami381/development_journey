from mysql import connector

class ExpenseListCreateRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        self.connection=connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="tripwise_db"
        )

        self.cursor=self.connection.cursor()

    def post(self,**kwargs): 
     query="insert into expense(trip,paid_by,amount,category) values(%s,%s,%s,%s) "
          
     values=list(kwargs.values())
     self.cursor.execute(query,values)
     self.connection.commit()
     print("expenses are added...")

    def get(self):
       query="select * from expense"
       self.cursor.execute(query)
       records=self.cursor.fetchall()
       for exp in records:
          print(exp)

    def retrieve(self,id=None):
       query="select * from expense where id=%s"
       values=(id,)
       self.cursor.execute(query,values)
       record=self.cursor.fetchone()
       print(record)

    def put(self,id=None,**kwargs):
    #kwargs=(id=2,trip="nepal",amount=8500,paid_by="zendayaaa")
       place_holder=""

       for k in kwargs.keys():
          place_holder +=k+"=%s,"

       place_holder=place_holder.rstrip(",")

       query=f"update expense set {place_holder} where id=%s"
       values=list(kwargs.values())   #list because we have to add id
       values.append(id)
       self.cursor.execute(query,values)
       self.connection.commit()
       print("record has been updated...")

    def delete(self,id=None):
            query="delete from expense where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            self.connection.commit()
            print("record deleted...")

exp_instance=ExpenseListCreateRetrieveUpdateDelete(user="root",password="Password@123")
print(exp_instance.connection)
#exp_instance.post(trip="thekkadi",paid_by="manju",amount=7000,category="food")
exp_instance.get()
#exp_instance.retrieve(id=2)
#exp_instance.put(id=2,trip="nepal",amount=8500,paid_by="zendayaaa")
#exp_instance.put(id=2,category="shopping")
#exp_instance.delete(id=1)
