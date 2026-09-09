from mysql import connector

class HospitalCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):
    
            if user==None or password==None:
               raise Exception("username and password required..")
            self.connection=connector.connect(
                user=user,
                password=password,
                host="localhost",
                database="hospital_db"
            )
            self.cursor=self.connection.cursor()

    def post(self,**kwargs):
         db_cols=("patient_name","phone_number","assigned_doctor","department","appointment_date","status","consultation_fee")
         
         difference=set(db_cols).difference(kwargs.keys())   #if a colomn is missed to add raise exception
         if difference:
                     raise Exception(f"{difference} required")
         
         col_str=",".join(db_cols)
         
         query=f"insert into patients ({col_str}) values(%s,%s,%s,%s,%s,%s,%s)"
         values=list(kwargs.values())
         self.cursor.execute(query,values)
         self.connection.commit()
         print("record has been added....")

    def get(self):
          query="select * from patients"
          self.cursor.execute(query)
          records=self.cursor.fetchall()
          for patient in records:
                print(patient)

    def retrieve(self,patient_name=None,phone_number=None):
            query=f"select * from patients where patient_name=%s or phone_number=%s "
            values=(patient_name,phone_number)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            print(record)

    def put(self,patient_id=None,**kwargs):
           place_holder=""                   
           for k in kwargs.keys():
                place_holder +=k+"=%s,"
                   
           place_holder=place_holder.rstrip(",")
           query=f"update patients set {place_holder} where patient_id=%s"
           values=list(kwargs.values())
           values.append(patient_id)
           self.cursor.execute(query,values)
           self.connection.commit()
           print("record has been updated...")

    def filter(self,**kwargs):
             
             place_holder=""
             for k in kwargs.keys():
                        place_holder +=k+"=%s and "
                     
             place_holder=place_holder.rstrip("and ")    
             query=f"select * from patients where {place_holder}"
             values=list(kwargs.values())
             self.cursor.execute(query,values)
             records=self.cursor.fetchall()
             if records:
                   for t in records:
                         print(t)
             else:
                   print("no records")

    
    def summary(self):
                 query="select status,count(*)as count from patients group by status"
                 self.cursor.execute(query)  
                 response=self.cursor.fetchall()
                 dept_summary_query="select department,count(*) as count from patients group by department"
                 self.cursor.execute(dept_summary_query)
                 dept_summary=self.cursor.fetchall()
                 print("department=",dept_summary)
                 print("status=",response)  

    def delete(self,patient_id=None):
             query="delete from patients where patient_id=%s"
             values=(patient_id,)
             self.cursor.execute(query,values)
             self.connection.commit()
             print("record has been deleted...") 
    
    


patient=HospitalCreateListRetrieveUpdateDelete(user="root",password="Password@123")
print(patient.connection)
# patient.post(
#     patient_name="Rahul Das",
#     phone_number="9876543214",
#     assigned_doctor="Dr. Arun Kumar",
#     department="Orthopedics",
#     appointment_date="2026-09-08",
#     status="Cancelled",
#     consultation_fee=0
# )
#patient.get()
#patient.retrieve(patient_name="Arjun Kumar")
#patient.put(patient_id=1,status="completed")
#patient.filter(department="cardiology",status="completed")
#patient.summary()
#patient.delete(patient_id=8)