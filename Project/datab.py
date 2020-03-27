# data is taken from time_price
import time_price
from datetime import datetime
#importing time zone pytz module
from pytz import timezone
'''
currency is used to easily change currency
in which we wish to recieve the updates
eg: US dollar= USD Indian Rupees= INR .etc
'''
currency = 'INR'
def datab():
  try:
    data = time_price.get_data(currency)
    format = "Date: %d-%m-%Y \n Time: %H:%M:%S"
    # Coordinated Universal time
    univ_time = datetime.now(timezone('UTC'))
    # Converting to Indian Standard Time(IST)
    ist = univ_time.astimezone(timezone('Asia/Kolkata'))
    time = (ist.strftime(format))
    return (f'BTC Price : {data} <br> {time} <br> <br>')
  except Exception :
    print("Error")