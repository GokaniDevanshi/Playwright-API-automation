
from Class import calculator

class implementChild(calculator):
    num=100

    def __init__(self):
        super().__init__(1,2)
        
    def data(self):
        return self.num+self.summation()

obj1= implementChild()
print(obj1.data())