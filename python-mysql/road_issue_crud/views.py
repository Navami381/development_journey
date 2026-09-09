from mysql import connector
class ExpenseCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):     #connection established
        self.connection=connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="road_issue_db"
        )
        self.cursor=self.connection.cursor()

    def post(self,**kwargs):                     #insert data into the table
        query="insert into issues(title,location,posted_by,status)values(%s,%s,%s,%s)"
        values=list(kwargs.values())
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been added...")

    def get(self):
        query="select * from issues"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for issues in records:
            print(issues)

    def retrieve(self,id=None):
            query="select * from issues where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            print(record)

    def put(self,id=None,**kwargs):
        place_holder=""
        for k in kwargs.keys():
                place_holder +=k+"=%s,"         #title="drainage,loaction="tvm,"
        place_holder=place_holder.rstrip(",") 

        query=f"update issues set {place_holder} where id=%s"
        values=list(kwargs.values())
        values.append(id)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("record has been updated...")

    def delete(self,id=None):
         query="delete from issues where id=%s"
         values=(id,)
         self.cursor.execute(query,values)
         self.connection.commit()
         print("record deleted...")


issue_instance=ExpenseCreateListRetrieveUpdateDelete(user="root",password="Password@123")  #created object
print(issue_instance.connection)
#issue_instance.post(title = "Blocked drainage", location = "Palakkad", posted_by = "Meera", status = "solved")
issue_instance.get()
#issue_instance.retrieve(2)
#issue_instance.put(id=2,location="tvm",posted_by="lizy")
#issue_instance.delete(id=4)
