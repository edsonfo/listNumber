class ListNumber:
    def __init__(self,iniNum):
        self.iniNum=iniNum

    def addNum(self):
        self.iniNum.pop(0)
        addNumber= self.iniNum[len(self.iniNum)-1]+1
        self.iniNum.append(addNumber)        
        return self.iniNum