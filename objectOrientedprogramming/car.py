from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod         #@ is decorator
    def start(self):pass

    @abstractmethod
    def accelerate(self):pass
    
    @abstractmethod
    def stop(self):pass

class Baleno(Car):
    def start(self):
        print("baleno start method..")
    def accelerate(self):
        print("baleno accelaerate method..")
    def stop(self):
        print("baleno stop method...")

baleno_instance=Baleno()
baleno_instance.start()
baleno_instance.accelerate()
baleno_instance.stop()

