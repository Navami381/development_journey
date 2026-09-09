"""
Employee id,name,salary,phone,department
        -setemployee(id,name,salary,phone,department)
        -getemployee()
"""
class Employee:
    id:int
    name:str
    salary:int
    phone:int
    department:str
    def __init__(self,id,name,salary,phone,department):
        self.id=id
        self.name=name
        self.salary=salary
        self.phone=phone
        self.department=department
    def get_employee(self):
        print(self.id,self.name,self.salary,self.phone,self.department)


sharukh_instance=Employee(2,"Sharukhan",700000,1234567890,"hr")

sharukh_instance.get_employee()
