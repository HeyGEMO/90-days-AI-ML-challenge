class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for val in self.marks:
            sum += val
        print(self.name, "average :" , sum/3)
s1=Student("rikesh",[99,78,56])
s1.average()
s1.name="bibek"
s1.average()