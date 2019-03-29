'''Poorva Nene 38426682'''

class TrueRange():
    '''class that goes through list of data and gets true range indicators'''

    def __init__(self, storedHigh, storedLow, storedClose):
        self.high = storedHigh
        self.low = storedLow
        self.close = storedClose


    def execute(self) -> list:
        '''returns list of indicators'''
        
        indicatorList = []
        
        for i in range(len(self.high)):
            if i == 0:
                indicatorList.append('')
            elif i > 0:
                if self.close[i-1] > self.high[i]:
                    truerange = self.close[i-1] - self.low[i]
                    indicatorList.append((truerange / self.close[i-1]) * 100)
                elif self.close[i-1] < self.low[i]:
                    truerange = self.high[i] - self.close[i-1]
                    indicatorList.append((truerange / self.close[i-1]) * 100)
                else:
                    truerange = self.high[i]-self.low[i]
                    indicatorList.append((truerange / self.close[i-1]) * 100)


        return indicatorList


class SimpleMoving():
    '''class that goes through list of data and gets simple moving indicator'''
    def __init__(self, days:str,data:list):
        self.days = days
        self.data = data
        
    def execute(self) -> list:
        '''returns list of indicators'''
        indicatorList = []
        for i in range(len(self.data)):
            if i < int(self.days) - 1:
                indicatorList.append('')
            else:
                total = 0
                for a in range(int(self.days)):
                    total += (self.data[i-a])
                average = (total / float(self.days))
                indicatorList.append(average)
                
        return indicatorList
                            


        
class DirectionalInd():
    '''class that goes through list and gets directional indicators'''
    def __init__(self, days:str,data:list):
        self.days = days
        self.data = data

    def execute(self) -> list:
        '''returns list of indicators'''
        indicatorList = []

        for i in range(len(self.data)):
            decreased = 0
            increased = 0
            if i == 0:
                indicatorList.append(0) 
            elif i < int(self.days)+1:
                if self.data[i] > self.data[i-1]:
                    prevval = indicatorList[-1]
                    indicatorList.append(prevval + 1)
                elif self.data[i] < self.data[i-1]:
                    prevval = indicatorList[-1]
                    indicatorList.append(prevval - 1)
                else:
                    prevval = indicatorList[-1]
                    indicatorList.append(prevval)
            
            elif i >= int(self.days)+1:
                for a in range(int(self.days)):
                    if self.data[i-a] > self.data[(i-a)-1]:
                        increased +=1
                    elif self.data[i-a] < self.data[(i-a)-1]:
                        decreased +=1
                total = increased - decreased
                indicatorList.append(total)
                
        return indicatorList
            
 
