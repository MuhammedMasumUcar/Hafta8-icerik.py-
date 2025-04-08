""" Colabde Çalışıyor  İmportlamıyor requests'i"""
import requests
from bs4 import BeautifulSoup 
url="https://www.milligazete.com.tr/haber/24244937/serdar-haydanli-kimdir"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
def content(url):
     tarih1 =soup.find_all("span",{"class": "tarih"})
     print("Sayfadaki Tarih : ",tarih1[0].text)
     icerik=soup.find("p")
     print("Sayfadaki İçerik : ",icerik.text)
     başlık=soup.find("h1")
     print("Sayfadaki Başlık : ",başlık.text)
haber = content(url)
