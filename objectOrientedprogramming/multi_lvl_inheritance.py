class Grandparents:
    def properties(self):
        print("2 acre land....")

class Parent(Grandparents):
    def home(self):
        print("1500sqft home...")

class Child(Parent):
    def socail_media_account(self):
        print("social media account...")

child_instance=Child()
child_instance.socail_media_account()
child_instance.home()
child_instance.properties()