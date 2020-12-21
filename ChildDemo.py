from OoopsDemo import calculator


class childimp(calculator):
    num2=300

    def __init__(self):
        calculator.__init__(self,2,10)

    def getCompleteData(self):
        return self.num2+self.num+self.mul()

obj=childimp()
print(obj.getCompleteData())
print('*****************************')
