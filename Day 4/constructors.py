#init function by default
#invoke at creation of object
class Student:
    def __init__(self): #default constructors
        pass
#define only one constructors
    #parameterized constructor
    def __init__(self,fullname,marks): #self for new object also #use multiple parameter in constructor if we need to add multiple students name
        self.name=fullname
        self.marks=marks
        print("adding new student in databasee...")

s1=Student("kallu",88) #call it self
#self always first parameter
print(s1.name,s1.marks)

s2=Student("pandu",89)
print(s2.name,s2.marks)


