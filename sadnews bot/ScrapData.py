from bs4 import BeautifulSoup
from Extract import Extract
import requests
import re
import sys
URL="https://www.jesuismort.com/cimetiere/mort-recente"
page=requests.get(URL)
deathActually=constante
soup=BeautifulSoup(page.content,'html.parser')
ifd=soup.find("div",{'id':'page_rightColumn'})
numberOfBloc=soup.select("div",{'id':'page_centerColumn'})
death = soup.find(class_='page block celebrity blockList')
alldeath = soup.find_all(class_='page block celebrity blockList')[0]
def CounterDeath():
    k=0
    for i in numberOfBloc:
        ch=i.descendants
        for d in ch:
            if d.name and d.get('class')==['page','block']:
                return k
            if d.name=="div" and d.get('class')==['celebrity', 'block', 'colored', 'dark2']:
                if d.name and d.get('class')==['page']:
                    return k
                
                k=k+1

    return k

def MakeMsg():
    global deathActually
    chdif=CounterDeath()-deathActually
    deathOfLapsus=soup.find_all(class_='page block celebrity blockList')[0:chdif]
    listeOfDeathOfLapsus=[]
    for death in deathOfLapsus:
        tempsys=sys._xoptions
        bsfourElementTag=Extract(deathOfLapsus)
        tempsys['name']=bsfourElementTag.XtractName()
        tempsys['href']=bsfourElementTag.XtractHref()
        tempsys['info']=bsfourElementTag.XtractAreaLife()
        tempsys['text']=bsfourElementTag.XtractText()
        listeOfDeathOfLapsus.append(tempsys)
    deathActually=CounterDay()
    return listeOfDeathOfLapsus

def Checkalize():
    if CounterDeath()>deathActually:
        pushMsg()
    
def pushMsg():
    listeOfDeathOfLapsus=MakeMsg()
    for i in listeOfDeathOfLapsus:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        