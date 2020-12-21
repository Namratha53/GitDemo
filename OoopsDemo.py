class calculator:
    num=100

    def __init__(self,x,y):
        self.i=x
        self.j=y
        print('Default constructor calling!')

    def get_data(self):
        print("Executing get_data function")

    def mul(self):
        return self.i*self.j

a= calculator(2,3)
a.get_data()
print(a.mul())
print('**************************************')



