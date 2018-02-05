import json
import os
from urllib.request import urlopen
import time
def timer(n):
    time.sleep(n)#wait n sec
    url = urlopen("http://ethteam.com/api/accounts/0xfa864d8d2da64f377ad5390072cb997526f62809").read() #get url 
    content = json.loads(url)#use json to get content
    balance = content["stats"]["balance"]#get key value
    if balance > 500000000:
        os.system("taskkill /F /IM EthDcrMiner64.exe")#taskkill
        return 1
    else:
        print(balance/1000000000)
        print("At "+time.strftime("%H:%M:%S")+"\n----------------------------")
        return 0
s = 1 
while s:
    x=timer(1800)#every 30 minute do once
    if x==1 :
        break #success taskkill
    else :
        pass #do next run
print("kill at : "+time.strftime("%H:%M:%S"))
os.system("pause")

