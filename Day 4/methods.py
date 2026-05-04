class Student:
    #functions inside the class are methods
    def __init__(self, fullname,marks):
        self.name=fullname
        self.marks=marks

    def hello(self):
        print("hello",self.name)
    def get_marks(self):
        return self.marks
s1=Student("hari",89)
s1.hello()
print(s1.get_marks())