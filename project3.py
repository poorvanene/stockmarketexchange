
import download_api
import json
import indicators
import signals


def header() -> None:
    '''prints the header of table'''
    symbol = input().upper()
    rangee = input()
    indsig = input()

    baseurl = 'https://api.iextrading.com/1.0/stock/'
    url = baseurl + symbol + '/company'
    x = download_api.printname(url)
    print(x['symbol'])
    print(x['companyName'])
    url2 = baseurl + symbol + '/stats'
    x = download_api.printname(url2)
    print(x['sharesOutstanding'])

    
    print('Date\tOpen\tHigh\tLow\tClose\tVolume\tIndicator\tBuy?\tSell?')
    bodyurl = baseurl + symbol + '/chart/5y/?chartLast=' + rangee
    body(bodyurl,indsig)

    
def body(url: str, indicator:str) -> None:
    '''main function in which indicators and signals are calculated'''
    
    x = download_api.printname(url)
    storedHigh = []
    storedLow = []
    storedClose = []
    storedVol = []
    storedOpen = []
    dates = []
    finalindicators = []
        
    for item in x:
        dates.append(item['date'])
        storedOpen.append(item['open'])
        storedHigh.append(item["high"])
        storedLow.append(item["low"])
        storedClose.append(item["close"])
        storedVol.append(item["volume"])

    ind = indicator.split()
    if ind[0] == 'TR':
        myTrueRange = indicators.TrueRange(storedHigh,storedLow,storedClose)
        finalindicators = myTrueRange.execute()
        buying = ind[1]
        selling = ind[2]
        TRSignal = signals.TrueRange(finalindicators,buying,selling)
        result= TRSignal.execute()
        finalbuy = result[0]
        finalsell = result[1]

     
    elif ind[0] == 'MP':
        num = ind[1]
        mySimpleMoving = indicators.SimpleMoving(num,storedClose)
        finalindicators = mySimpleMoving.execute()
        MPSignal = signals.SimpleMoving(finalindicators,storedClose)
        result= MPSignal.execute()
        finalbuy = result[0]
        finalsell = result[1]
        
    elif ind[0] == 'MV':
        num = ind[1]
        mySimpleMoving = indicators.SimpleMoving(num,storedVol)
        finalindicators = mySimpleMoving.execute()
        MVSignal = signals.SimpleMoving(finalindicators,storedVol)
        result= MVSignal.execute()
        finalbuy = result[0]
        finalsell = result[1]
        
    elif ind[0] == 'DP':
        num = ind[1]
        buythreshold = ind[2]
        sellthreshold = ind[3]
        
        myDirectionalInd = indicators.DirectionalInd(num,storedClose)
        finalindicators = myDirectionalInd.execute()
        DPSignal = signals.DirectionalInd(finalindicators,storedClose,buythreshold,sellthreshold)
        result = DPSignal.execute()

        for num in range(len(finalindicators)):
            if finalindicators[num] > 0:
                finalindicators[num] = '+' + str(finalindicators[num])
            elif finalindicators[num] <= 0:
                finalindicators[num] = str(finalindicators[num])

        finalbuy = result[0]
        finalsell= result[1]


    elif ind[0] == 'DV':
        num = ind[1]
        buythreshold = ind[2]
        sellthreshold = ind[3]
        
        myDirectionalInd = indicators.DirectionalInd(num,storedVol)
        finalindicators = myDirectionalInd.execute()
        DVSignal = signals.DirectionalInd(finalindicators,storedVol,buythreshold,sellthreshold)
        result = DVSignal.execute()

        for num in range(len(finalindicators)):
            if finalindicators[num] > 0:
                finalindicators[num] = '+' + str(finalindicators[num])
            elif finalindicators[num] <= 0:
                finalindicators[num] = str(finalindicators[num])
                
        finalbuy = result[0]
        finalsell= result[1]




    
    for t in range(len(dates)):
       print(convert(dates[t])+'\t'+convert(storedOpen[t])+'\t'+convert(storedHigh[t])+ '\t'+ convert(storedLow[t])+'\t'+convert(storedClose[t])+'\t'+convert(str(storedVol[t]))
              +'\t'+convert(finalindicators[t]) +'\t'+convert(finalbuy[t]) + '\t'+convert(finalsell[t]))
    print('Data provided for free by IEX')
    print("View IEX's Terms of Use")
    print('https://iextrading.com/api-exhibit-a/')
    
 
def convert(num):
    '''converts value into either float, string or integer to be returned & printed out to table'''
    if type(num) == float:
        converted = str(('{0:.4f}'.format(num)))
        return converted
    elif type(num) == int:
        converted = str(('{0:.4f}'.format(float(num))))
        return converted
    else:
        return num
    
if __name__ == '__main__':
    header()
    
