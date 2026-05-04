class Student:
    #same name so store only one time
    college_name="Everest Engineering College"
    #name="anonymous"
    def __init__(self,name,age):
        self.name=name #obj attr > class attr
        self.age=age
        print("this will run anyway")

s1=Student("karan",23)
print(s1.name,s1.age)

print(Student.college_name)