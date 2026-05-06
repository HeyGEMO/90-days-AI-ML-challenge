#many forms
#operator overloading
#implicit overloading
#same operator have different meaning
print(1+2)# addition
print("no"+ "college") #concatenate
print([1,32,3] + [3,4,5]) #merge

#explicit overloading
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def showNumber(self):
        print(self.real,"i +", self.imag,"j")
    
    #def add(self,num2):
     #   newReal= self.real + num2.real
      #  newImag= self.imag + num2.imag
       # return Complex(newReal,newImag)
    def __add__(self,num2): #dunder function
        newReal= self.real + num2.real
        newImag= self.imag + num2.imag
        return Complex(newReal,newImag)
    def __sub__(self,num2):
        newReal= self.real - num2.real
        newImag= self.imag - num2.imag
        return Complex(newReal,newImag)
num1=Complex(3,4)
num1.showNumber()

num2=Complex(5,6)
num2.showNumber()

#num3=num1.add(num2)
num3=num1 + num2
num3.showNumber()
num3=num1 - num2
num3.showNumber()