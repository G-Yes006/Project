try:
  from time import sleep
  from tqdm import tqdm
  import sys
  
  print ("Automated Bitcoin Price Alerts\n")
  # data is taken from update
  import update
  update.sendtoBOT()
except(Exception):
  #Notification for Error
  print('Server is Down')