import requests
import time
import json
import os
import math

while True:
    #clears the terminal each time the loop starts...
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Data retreived from www.cryptocompare.com')
    #gets data from
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD')

    database = r.json()

    btc = database['BTC']
    usd = database['USD']

    result = usd/btc
    result = round(result,2)

    print ('1 Bitcoin = $', result)
    time.sleep(10)
