class Animal:
    name:str
    sound:str

    def walk(self):

        print("Animal is walking...")

    def sleep(self):

        print("Animal is sleeping...")

cat_instance=Animal()

dog_instance=Animal()

dog_instance.sleep()
cat_instance.walk()
