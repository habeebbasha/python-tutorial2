#THIS MY EXAMPLE
class person1:
    def __init__(self,money,borro):
        self.money=money
        self.borro=borro
    def getbarro(self):
        return self.borro
    def profit(self,prof):
        self.prof=800
        return self.prof
class person2(person1):
    def __init__(self,money,borro,loss):
        super().__init__(money,borro)
        self.loss=loss
    def profit(self,pro):
        self.pro=1000
        return self.pro
a=person1(9000,10000,1000)
print(a.profit(1000))