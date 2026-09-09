class Book:

    title:str
    price:float
    pages:int
    author:str
    def __init__(self,title,price,pages,author):

        self.title=title       #self is to point currect object
        self.price=price
        self.pages=pages
        self.author=author

    def get_book(self):
        print(self.title,self.price,self.pages,self.author)

rm_instance=Book("randamoozham",700,500,"mt")

rm_instance.get_book()