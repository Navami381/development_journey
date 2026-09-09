class Superhero:
    name:str
    power:str
    universe:str

    def __init__(self,name,power,universe):
        self.name=name
        self.power=power
        self.universe=universe
    def get_superhero(self):
        print(self.name,self.power,self.universe)

superhero_instance1=Superhero("spiderman","spreadingweb","marvel")

superhero_instance2=Superhero("batman","money","dc")

superhero_instance3=Superhero("minnal murali","run","basil joseph")



superhero_instance1.get_superhero()

superhero_instance2.get_superhero()

superhero_instance3.get_superhero()