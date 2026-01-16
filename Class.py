class calculator:
    num=100 #class variable
    #constructor called automatically whenever a object is created
    #self keyword-refers to the current object. Mandatory when calling variable names inside method.used to access object data
    def __init__(self,a,b):
        self.firstnumber=a     #instance variable
        self.secondnumber=b
    #Method (function inside a class)
    def summation(self):
        return self.firstnumber+self.secondnumber
    
#new keyword is not required when you create object
obj= calculator(2,10)
print(obj.summation())

