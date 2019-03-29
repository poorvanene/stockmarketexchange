'''Poorva Nene 38426682'''

import urllib.request
import urllib.error
import json



def printname(url:str):
    '''takes url and downloads contents'''
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode(encoding = 'utf-8')
        newtext = json.loads(text)
        return newtext
        
    except:
        print('ERROR')
            
    
