import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.bikewale.com/hero-bikes/")
#print(response)
soup=BeautifulSoup(response.content,"html.parser")
#print(soup)
names=soup.find_all('h3',class_="o-jjpuv o-cVMLxW o-mHabQ o-fzpibK")
name=[]
for i in names[0:10]:
    a=i.get_text()
    name.append(a)
print(name)

ratings=soup.find_all('div',class_="o-fzoTnS o-daXxmY o-wuqlZ o-BosvO o-fvgKOf o-fzqLoc o-bJruGr o-bsCSvY o-dMmXZk")
rate=[]
for i in ratings[0:10]:
    b=i.get_text()
    rate.append(b)
print(rate)

prices=soup.find_all('span',class_="o-eZTujG o-byFsZJ o-bkmzIL o-bVSleT")
price=[]
for i in prices[0:10]:
    c=i.get_text()
    price.append(c)
print(price)


images=soup.find_all('img',class_="o-bXKmQE o-cgkaRG o-cQfblS o-bNxxEB o-pGqQl o-wBtSi o-bwUciP o-btTZkL o-bfyaNx o-eAZqQI")
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
print(image)

links=soup.find_all('a',class_="o-cpnuEd o-SoIQT o-eZTujG o-fzpilz")
link=[]
for i in links[0:10]:
    f="https://www.bikewale.com/hero-bikes/"+i['href']
    link.append(f)
print(link)

df=pd.DataFrame()
print(df)
df["bikes"]=name
df["ratings"]=rate
df["prices"]=price
df["images"]=image
df["links"]=link
print(df)
df.to_csv("bikes.csv") #to changes into csv#