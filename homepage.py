import requests
import os
from bs4 import BeautifulSoup
url="https://timesofindia.indiatimes.com/"
os.makedirs('Homepage')
f1=open("Homepage/Homepage.txt","w",encoding="utf-8")
def nish(url1):
    r=requests.get(url1)
    html=r.text
    soup=BeautifulSoup(html,'html.parser')
    title=soup.find("h1",{"class":"_23498"})
    datad=soup.find("div",{'class':"_3Mkg- byline"})
    texta=soup.find("div",{'class':"ga-headlines"})
    if title!=None and datad!=None and texta!=None :
        f1.write("Title\n")
        f1.write(title.get_text()+"\n")
        f1.write('\n')
        f1.write("URL\n")
        f1.write(url1+'\n')
        f1.write('\n')
        f1.write("Date" + '\n')
        f1.write(datad.get_text()+'\n')
        f1.write('\n')
        f1.write("Text" + '\n')
        f1.write(texta.get_text()+'\n')
        f1.write('\n')
        f1.write('\n')

r=requests.get(url)
html=r.text
soup=BeautifulSoup(html,"html.parser")
anchor=soup.find_all('a')
for link in anchor:
    ma=str(link.get("href"))
    if "https" in ma:
        nish(ma)
    elif ma[:1]=='/' :
        nish("https://timesofindia.indiatimes.com"+ma)


f1.close()
