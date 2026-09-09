class Food:
    id:int
    name:str
    category:str
    price:float
    quantity:int
    calories:float
    def __init__(self,id,name,category,price,quantity,calories):
        self.id=id
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
        self.calories=calories
    def get_food(self):
        print(self.id,self.name,self.category,self.price,self.quantity,self.calories)
burger_instance=Food(1, "Burger", "Fast Food", 150, 1, 500)
pizza_instance=Food(2, "Pizza", "Fast Food", 250, 2, 800)


burger_instance.get_food()


pizza_instance.get_food()