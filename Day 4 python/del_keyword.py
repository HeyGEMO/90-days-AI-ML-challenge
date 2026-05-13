#delete oject and properties
class Student:
    def __init__(self,name):
        self.name=name

s1= Student("pandu")
print(s1.name)
#del s1.name
#print(s1.name)

#private attribute and methods
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #private
    def reset_pass(self):
        print(self.__acc_pass)
acc1= Account("12345","password")
#print(acc1.acc_no,acc1.__acc_pass)
print(acc1.reset_pass())

class Person:
    __name="anonymous"
    def __hello(self):
        print("Hello jani!")
    def welcome(self): #only access by the function inside the class 
        self.__hello()
p1=Person()
print(p1.welcome())