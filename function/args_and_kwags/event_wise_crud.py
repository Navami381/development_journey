# event add,list,detail,update,delete

class EventWise:

    def __init__(self):

        self.programs =[
            {"id":1,"event":"group song","name":"abi","contact":"345678","batch":"djangoct","faculty":"anju"},

        ] 

    def post(self,**kwargs):

        self.programs.append(kwargs)

        print("record has been created.....")

    def get(self):

        if len(self.programs)==0:

            print("no records")

        else:
            for p in self.programs:

                print(p)

    def retrieve(self,id=None):

        program = [ p for p in self.programs if p.get("id")==id][0]

        print(program)

    def put(self,id=None,**kwargs):

        program = [p for p in self.programs if p.get("id")==id][0]

        program.update(kwargs)

        print("record hasbeen updated...")

        print(program)

    def delete(self,id=None):

         program = [p for p in self.programs if p.get("id")==id][0]

         self.programs.remove(program)

         print("deleted...")

         self.get()
        

evnt_instance =  EventWise()

evnt_instance.post(id=2,event="dance",name="avin",contact="456789",batch="djaug",faculty="sukumar")

# evnt_instance.get()

# evnt_instance.retrieve(id=10)

# evnt_instance.put(id=2,name="avin a.b",contact="567890")

evnt_instance.delete(id=2)