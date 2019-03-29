
class TrueRange():
    '''class that generates signals based on true range'''
    def __init__(self,finalindicators:list,buying:list,selling:list):
        self.indicators = finalindicators
        self.buy = buying
        self.sell = selling
        

    def execute(self) -> tuple:
        '''returns a list of buy signals and sell signals for true range indicators'''
        buy = []
        sell = []
        for item in self.indicators:
            if item == '':
                buy.append('')
                sell.append('')
            else:
                buysign = self.buy[0]
                buynum = float(self.buy[1:])
                
                sellsign = self.sell[0]
                sellnum = float(self.sell[1:])
                
                if buysign == '<':
                    if item < buynum:
                        buy.append('BUY')
                    else:
                        buy.append('')
                if buysign == '>':
                    if (item) > buynum:
                        buy.append('BUY')
                    else:
                        buy.append('')
                    
                if sellsign == '<':
                    if (item) < sellnum:
                        sell.append('SELL')
                    else:
                        sell.append('')
                if sellsign == '>':
                    if (item) > sellnum:
                        sell.append('SELL')
                    else:
                        sell.append('')
        return buy,sell 
            
            
            


class SimpleMoving():
    '''class that generates signals based on simple moving'''   
    def __init__(self,finalindicators:list,data:list):
        self.indicators = finalindicators
        self.data = data

    def execute(self) -> tuple:
        '''returns a list of buy signals and sell signals for simple moving indicators'''

        buy = []
        sell = []
        for a in range(len(self.indicators)):
            if a == 0:
                buy.append('')
                sell.append('')
                
            elif a >0 and self.indicators[a] == '' or self.indicators[a-1] == '':
                buy.append('')
                sell.append('')               
            else:
                if self.data[a] > self.indicators[a] and self.data[a-1] <= self.indicators[a-1]:
                    buy.append('BUY')
                else:
                    buy.append('')
                    
                if self.data[a] < self.indicators[a] and self.data[a-1] >= self.indicators[a-1]:
                    sell.append('SELL')
                else:
                    sell.append('')
        return buy,sell 

        
                     
class DirectionalInd():
    '''class that generates signals based on directional indicator'''

    def __init__(self,finalindicators:list,data:list,buythreshold:str,sellthreshold:str):
        self.indicators = finalindicators
        self.data = data
        self.buythreshold = buythreshold
        self.sellthreshold = sellthreshold

    def execute(self) ->tuple:
        '''returns a list of buy signals and sell signals for directional indicators'''

        buy = []
        sell = []
        for a in range(len(self.indicators)):
            if a == 0:
                buy.append('')
                sell.append('')              
            else:
                if (self.indicators[a] > float(self.buythreshold)) and (self.indicators[a-1] <= float(self.buythreshold)):
                    buy.append('BUY')
                else:
                    buy.append('')
                    
                if (self.indicators[a] < float(self.sellthreshold)) and (self.indicators[a-1] >= float(self.sellthreshold)):
                    sell.append('SELL')
                else:
                    sell.append('')
        return buy,sell 
