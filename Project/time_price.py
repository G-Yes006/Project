# iporting requests module to fetch api
import requests
# function to return data based on currency
def get_data(currency):
  try:
    # connection is being established to the url
    connection = requests.get(url='https://blockchain.info/ticker')
    data_in__json = connection.json()
    #latest bitcoin price and symbol will return the symbol of the currency provided.
    return (str(data_in__json[currency.upper()]['last']) +' '+  str(data_in__json[currency.upper()]['symbol']))
  except Exception:
  #print Error if Server is Down  
    print('Error')