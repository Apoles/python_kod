import requests
from bs4 import BeautifulSoup

url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")

list=soup.find_all("li",{"class":"column"},limit=10)

for li in list:
    name=li.div.a.h3.text.strip()
    link=li.div.a.get("href")
    oldprice=li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip("tl")
    newprice=li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip("tl")
    print(f"name:{name}\nlink:{link}\noldprice:{oldprice}\nnewprice:{newprice}")


