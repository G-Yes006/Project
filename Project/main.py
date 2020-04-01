# requests module is used to access data from api
import requests
#time to wait (sleep) is define d in seconds
from time import sleep
# System specific parameters and functions
import sys
#import timezone
import pytz
#import date and time
from datetime import datetime
#importing time zone pytz module
from pytz import timezone
#print the project title
print ("Automated Bitcoin Price Alerts\n")

print("Currency Codes\nIndia - INR\nUSA - USD\nJapan - JPY\nRussia - RUB\n")
# get_data function will return the data from url based on the currency given 
def get_data(currency):
  try:
    # connection is being established to the url
    connection = requests.get(url='https://blockchain.info/ticker')
    # data is encoded into json format
    data_in__json = connection.json() 
    # returning the data to the function, which can be accessed in other module
    #last will get the latest bitcoin price and symbol will return the symbol of the currency provided.
    return (str(data_in__json[currency.upper()]['last']) +' '+  str(data_in__json[currency.upper()]['symbol']))
  # if in case the url we gave is offline the code will terminate and we need to change the url.  
  except Exception:
    print('Data is not accessable from the url provided.')
'''
currency is used to easily change currency
in which we wish to recieve the updates
eg: US dollar= USD Indian Rupees= INR etc
'''
currency = input ("Please Enter Currecncy Code: ")
#currency = 'INR'
def datab():
  try:
    data = get_data(currency)
    format = "Date: %d-%m-%Y \n Time: %H:%M:%S"
    # Coordinated Universal time
    univ_time = datetime.now(timezone('UTC'))
    # Converting to Indian Standard Time(IST)
    ist = univ_time.astimezone(timezone('Asia/Kolkata'))
    time = (ist.strftime(format))
    return (f'BTC Price : {data} <br> {time} <br> <br>')
  except Exception :
    print("Error")
#function to take event name as parameter and sent the data to applet of ifttt.
def sendtoBOT(event='tg_btc'):
  #creating empty list
  storage = []
  #to create a infinite loop
  i = 1
  while True:
    data = datab()
    #collected data is addeding to the list.
    storage.append(data)
    print(f'Price collected {i} times.')
    i += 1
    #Time interval can modify for collecting prices in seconds(s)
    sleep(5)
    #IFTTT Token
    ifttt_url = f'https://maker.ifttt.com/trigger/{event}/with/key/bmPZdMLZhQ_icQNrW3IQ00'
    if len(storage) == 5 :
      try:
        # the data in list is add to string module . 
        string = "".join([x+'\n' for x in storage])
        #assigning our string to datafield in aplet
        data = {'value1' : (string)}
        s = requests.session()
        requests.post(ifttt_url,json=data)
        print(f'Updated Telegram Bot.\n ') 
        #print(*storage)
        s.close
        #deleting old data
        del data
        storage = [] 
        #Fetching Data again
        print('Collecting latest Bitcoin Prices\n')
        sendtoBOT()
      except Exception:
        print('Error')
        sendtoBOT()
sendtoBOT().sendtoBOT()