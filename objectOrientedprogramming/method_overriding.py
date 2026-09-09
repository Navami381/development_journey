class Parent:
    def mobile(self):
        print("Redmi note 15 pro")

class Child(Parent):
     def mobile(self):
         print("iphone 17 pro")

child_instance=Child()
child_instance.mobile()