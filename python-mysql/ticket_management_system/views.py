from mysql import connector
class ticketCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        if user==None or password==None:
           raise Exception("username and password required..")
        self.connection=connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="customer_support_db"
        )
        self.cursor=self.connection.cursor()

    def post(self,**kwargs):
        db_cols=("customername","email","subject","description","category","priority","status","assignedto")

        difference=set(db_cols).difference(kwargs.keys())   #if a colomn is missed to add raise exception
        if difference:
            raise Exception(f"{difference} required")

        col_str=",".join(db_cols)

        query=f"insert into supportticket ({col_str}) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        values=list(kwargs.values())
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been added....")

    def get(self):
        query="select * from supportticket"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for ticket in records:
            print(ticket)

    def retrieve(self,id=None):
        query="select * from supportticket where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        record=self.cursor.fetchone()
        print(record)

    def put(self,id=None,**kwargs):
        place_holder=""
        
        for k in kwargs.keys():
                  place_holder +=k+"=%s,"
        
        place_holder=place_holder.rstrip(",")
    
        query=f"update supportticket set {place_holder} where id=%s"
        values=list(kwargs.values())
        values.append(id)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been updated....")

    def filter(self,**kwargs):
         #kwargs={status="pending","priority":"high"}
         place_holder=""
         for k in kwargs.keys():
                    place_holder +=k+"=%s and "
                 
         place_holder=place_holder.rstrip("and ")

         query=f"select * from supportticket where {place_holder}"
         values=list(kwargs.values())
         self.cursor.execute(query,values)
         records=self.cursor.fetchall()
         if records:
               for t in records:
                     print(t)
         else:
               print("no records")


    def summary(self):
         query="select status,count(*)as count from supportticket group by status"
         self.cursor.execute(query)  
         response=self.cursor.fetchall()
         priority_summary_query="select priority,count(*) as count from supportticket group by priority"
         self.cursor.execute(priority_summary_query)
         priority_summary=self.cursor.fetchall()
         print("priority summary",priority_summary)
         print(response)         
                             

    def delete(self,id=None):
         query="delete from supportticket where id=%s"
         values=(id,)
         self.cursor.execute(query,values)
         self.connection.commit()
         print("record has been deleted...")
         
            
    


ticket=ticketCreateListRetrieveUpdateDelete(user="root",password="Password@123")
print(ticket.connection)
# ticket.post(
#     customername='Vishnu',
#     email='vishnu@gmail.com',
#     subject='Product not delivered',
#     description='My order was supposed to arrive three days ago but I still have not received it.',
#     category='delivery',
#     priority='high',
#     status='inprogress',
#     assignedto='Rahul'
# )
#ticket.get()
#ticket.retrieve(id=3)
#ticket.put(id=3,customername="sanjali",email="sanjali@gmail.com")
#ticket.delete(id=4)
#ticket.filter(status="inprogress",priority="medium")
#ticket.filter(customername="Vishnu")
ticket.summary()