import os
import time
import pandas

while True:
    if os.path.exists(r'C:\Users\CHANDRABRATA\Desktop\Python Basic\UdemyResources\temps_today.csv'):
        pd=pandas.read_csv(r'C:\Users\CHANDRABRATA\Desktop\Python Basic\UdemyResources\temps_today.csv')
        print(pd.mean()['st1'])
    
    else:
        print('File not found')
    time.sleep(5)
    