# data from datab module
import datab
from time import sleep
# requests is used to post and create sessions
import requests
#function to take event name as parameter and sent the data to applet of ifttt.
def sendtoBOT(event='tg_btc'):
  #creating empty list
  storage = []
  #to create a infinite loop
  i = 1
  while True:
    data = datab.datab()
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