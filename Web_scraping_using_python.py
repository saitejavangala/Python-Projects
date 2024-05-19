import requests
import pandas
from bs4 import BeautifulSoup 
response=  requests.get("https://www.flipkart.com/search?q=redmi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off") 
soup=BeautifulSoup(response.content,"html.parser")
names=soup.find_all("div",class_="_4rR01T")
name=[]
for i in names[0:10]:
    d=i.text

    name.append(d)
#print(name)   
prices=soup.find_all("div",class_="_25b18c")
price=[]
for i in prices[0:10]:
    d=i.text
    
    price.append(d)
#print(price)    




#print(name)
links=soup.find_all("a",class_="_1fQZEK")
link=[]
for i in links[0:10]:
    d="https://www.flipkart.com/"+i["href"]
    link.append(d)
    #print(link)
feauters=soup.find_all("li",class_="rgWa7D")
feuter=[]
for i in feauters[0:10]:
    d=i.text
    feuter.append(d)
    #print(feuter) 
ratings=soup.find_all("span") 
rating=[]
for i in ratings[0:10]:
    d=i.text
    rating.append(d)  
#print(rating) 
images=soup.find_all("img",class_="_396cs4")
image=[]
for i in images[0:10]:
    d=i["src"]
    image.append(d)
print(image)         
data={"names":name,"links":link,"images":image,"feauters":feuter,"rating":rating}
df=pandas.DataFrame(data)
print(df)
df.to_csv("moblie.csv")



         