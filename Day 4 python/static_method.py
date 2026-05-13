#for no self parameter
class Student:
    @staticmethod #decorator
    def college():
        print("Everest Engineering College")
Student.college()
#abstraction = hide the implementation
#encapsulation = wrapping data and function into single unit(object)
class Car:
    def __init__(self):
        self.accelerator = False
        self.stop = False
        self.clutch = False
    def start(self):
        self.clutch= True
        self.accelerator = True
        print("car started...")
car1=Car()
car1.start()
