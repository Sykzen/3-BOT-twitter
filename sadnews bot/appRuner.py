import tweepy
import time
from bs4 import BeautifulSoup
from Extract import Extract
import requests
import re
import os
from bing_image_downloader import downloader
import sys
import shutil
from _token import *
auth = tweepy.OAuthHandler(API_KEYS, API_SECRET_KEYS)
auth.set_access_token(TOKEN, TOKEN_SECRET)
api = tweepy.API(auth)
try:
    api.verify_credentials()
except:
    print("Error during authentication")




LastDeath="Jean-Claude Carrière"


def CheckNews():
    global LastDeath
    global soup
    print(LastDeath)
    e=0
    URL="https://www.jesuismort.com/cimetiere/mort-recente"
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')

    alldeathe = soup.find_all(class_='page block celebrity blockList')
   

    for i in alldeathe:
        for s in i:
            
            k=s.find('img')
            if k!=-1:
                e=e+1
                print(LastDeath)
                if k.get('title')==LastDeath:
                            
                    print(e-1)
                    return e-1
    
    

def MakeMsg():
    global LastDeath
    global soup
    chdif=CheckNews()
    deathOfLapsus=soup.find_all(class_='page block celebrity blockList')[:chdif]
    listeOfDeathOfLapsus=[]
    for death in deathOfLapsus:
        tempsys={}
        bsfourElementTag=Extract(death)
        tempsys['name']=bsfourElementTag.XtractName()
        tempsys['info']=bsfourElementTag.XtractAreaLife()
        tempsys['text']=bsfourElementTag.XtractText()
        tempsys['tombstone']=bsfourElementTag.XtractDeathCause()
        listeOfDeathOfLapsus.append(tempsys)
    LastDeath=death.a.find('img',title=True)['title']
    return listeOfDeathOfLapsus

def Hashtag(ProperName):
    hashOne=ProperName.split()
    chstring=""
    for i in hashOne:
        chstring+="#"+i+" "
    returne=chstring + "#"+''.join(hashOne)
    return returne,len(returne)

def fetchIMG(name):
    downloader.download(name, limit=1)
    return 'dataset/',name,'/',os.listdir("dataset/"+str(name))[0]
def Cizel(name, infoA,infoB,diff,text,tombstone):
    Hashtg,lenstatic0=Hashtag(name)
    lenstatic1="%s : %s - %s  (%s ans)\n" % (name, infoA,infoB,diff)
    lenstatic2="Cause décès: %s" % (tombstone)
    Lenmin=len(lenstatic1)+len(lenstatic2)+lenstatic0
    mintexte=280-Lenmin-3
    texte=text[0:mintexte]
    LASTEtexte="""%s : %s - %s  (%s ans)\n%s\n Cause décès: %s\n%s""" % (name, infoA,infoB,diff,texte,tombstone,Hashtg)
    return LASTEtexte

def tweetPublish(*args):
    name,info,text,tombstone,imglink=args
    Hashtg,a=Hashtag(name)
    imglink=''.join(list(imglink))
    diff=int(info[1])-int(info[0])

    message="""%s : %s - %s  (%s ans)\n%s\nCause décès: %s\n%s""" % (name, info[0],info[1],diff,text,tombstone,Hashtg)
    message=[message,Cizel(name, info[0],info[1],diff,text,tombstone)][len(message)>280]
    api.update_with_media(filename = imglink, status =message,auto_populate_reply_metadata=True)
    print('tweet published')

    
def pushMsg():
    listeOfDeathOfLapsus=MakeMsg()
    for i in listeOfDeathOfLapsus:
        imglink=fetchIMG(i['name'])
        
        tweetPublish(i['name'],i['info'],i['text'],i['tombstone'],imglink)
        shutil.rmtree("dataset")
        time.sleep(5)
def Checkalize():
    if CheckNews()>0:
        pushMsg()    
    else:
        time.sleep(60*60)
while 1:
   Checkalize()
   print('--')
    