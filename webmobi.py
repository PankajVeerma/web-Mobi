import requests
from bs4 import BeautifulSoup
import pandas
import re
name=[]
date=[]
location = []
price=[]
desc=[]
orgnizer=[]
for i in range(0,20):
    urls="https://www.eventbrite.com/d/india/b2b/"+str("i")
    r=requests.get(urls)
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find_all("div",{"class":"Layout-module__layout___1vM08"})
    
    names=box.find_all("div",{"class":"event-title css-0"})
    for i in names:
        name.append(i.text)
    dates=box.find_all("div",{"class":"date-info__full-datetime"})
    for i in dates:
        date.append(i.text)
    locations=box.find_all("div",{"class":"location-info__address-text"})
    for i in locations:
        location.append(i.text)
     
    prices=box.find_all("div",{"class":"event-details__section --padding-top"}) 
    for i in prices:
        price.append(i.text)
    
    
      
    discription=box.find_all("ul",{"class":"eds-text--left"}) 
    for i in discription:
        desc.append(i.text)
    
    
    
    Orgnizers=box.find_all("div",{"class":"descriptive-organizer-info-mobile__name"})
    for i in Orgnizers:
       Orgnizer.append(i.text)
     
    
df=pandas.DataFrame({"product":name,"Date":dates,"price":price,"description":desc,"orgnizer":Orgnizers})
print(df)
# df.to_excel("MObile_Data")