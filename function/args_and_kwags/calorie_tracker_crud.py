#CRUD SIMULATION

#create|add=post
#list all=get
#detail=retrieve
#update=put
#remove=delete

class DietLens:
    def __init__(self):
       self.food_logs=[
           {id:1,"name":"mandhi","calorie":200,"owner":"navami"}           
           ]
       
    def post(self,**kwargs):
        required_fields={"id","name","calorie","owner"}

        missing_fields=required_fields.difference(kwargs.keys())

        if missing_fields:
            raise Exception(missing_fields,"is missing")
            
        self.food_logs.append(kwargs)
        print('record has been added....')


    def get(self):
        if len(self.food_logs)==0:
            print("no records found...")
        else:
            for log in self.food_logs:
                print(log)

    def retrieve(self,id=None):
        if not id:
            raise ValueError("id is missing")
        else:
            return [log for log in self.food_logs if log.get("id")==id]

    def put(self,id=None,**kwargs):
        log=[log for log in self.food_logs if log.get("id")==id][0]

        log.update(kwargs)
        print("record has been updated..")
        print(log)

    def delete(self,id=None):
        log=[log for log in self.food_logs if log.get("id")==id] [0]
        
        self.food_logs.remove(log)
        print("food removed...")
        print(self.get())

    
diet_instance=DietLens()
diet_instance.post(id=2,name="dosa",calorie=170,owner="hari")
diet_instance.post(id=3,name="chappathi",calorie=70,owner="anu")
diet_instance.get()
print(diet_instance.retrieve(id=2))
diet_instance.put(id=2,name="ghee roast",calorie=400)
diet_instance.delete(id=3)