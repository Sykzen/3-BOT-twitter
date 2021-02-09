from bs4 import BeautifulSoup
import requests
import re
def tombstone(bs4elementTag):
    string=str(bs4elementTag)
    CauseOfDeath=""
    enumerate=0
    for a,b,c in zip(string,string[1:],string[2:]):
        enumerate+=1
        if a=="a" and b=="n" and c==">":
            ch= ((string[enumerate+2:-13].replace('\n','')).replace('\t','')).replace('Mort','Mort ')
            return "inconnue" if '<em' in ch else ch

class Extract:
    def __init__(self,bsfourElementTag):
        self.a=bsfourElementTag.a
        self.p=bsfourElementTag.p
        self.t=bsfourElementTag.find('div',class_="overflowed_intern").text
    def XtractHref(self):
        """bs4.element.tag ---> string
           get the main page of the defunt"""
        return "https://www.jesuismort.com"+self.a['href']
        
    def XtractName(self):
       """ self----->string
       get name of defunt """
       return self.a.find('img',title=True)['title']
    def XtractAreaLife(self):
        """self --->list
        get date of death and birth and nationality"""
        liste=[]
        for i in self.p:
            try:
                liste.append(i.text if i.text!='' else None)
            except:
                None
        return [i for i in liste if i!=None]
    def XtractText(self):
        """self------> txt
        get a brief decription of the defunt"""
        txt=self.t.replace('\n','')
        return txt.replace('\t','')

    def XtractDeathCause(self):
        """ self ---> string
        get the main cause of the death """
        URL=self.XtractHref()
        page=requests.get(URL)
        soup=BeautifulSoup(page.content,'html.parser')
        return tombstone(soup.find('div',class_="overflowed_intern"))
