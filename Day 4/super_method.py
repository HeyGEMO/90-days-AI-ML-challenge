class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name,type):
        self.name=name
        super().__init__(type) #used to access parent class
        super().start()
car1=ToyotaCar("thar","electric")
print(car1.type)