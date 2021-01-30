from bs4 import BeautifulSoup
import requests
import re
URL="https://www.jesuismort.com/tombe/jean-pierre-michel-politicien"
page=requests.get(URL)

soup=BeautifulSoup(page.content,'html.parser')
k=soup.find('div',class_="overflowed_intern")
def tombstone(bs4elementTag):
    string=str(bs4elementTag)
    CauseOfDeath=""
    enumerate=0
    for a,b,c in zip(string,string[1:],string[2:]):
        enumerate+=1
        if a=="a" and b=="n" and c==">":
            return ((string[enumerate+2:-13].replace('\n','')).replace('\t','')).replace('Mort','Mort ')
            
