documan_list="""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1>
       python kursu 
    </h1 id="header">
<div class="anan_Za">
     <h2>
        programlama 
    </h2>
        <ul>
        <li>menu 1</li>
            <li>menu 2</li>
            <li>menu 3</li>
        </ul>
    </div>
    <div class="anan_Za2">
     <h2>
        moduller
        </h2>
        <ul>
            <li>menu 1</li>
            <li>menu 2</li>
            <li>menu 3</li>
        </ul>
    </div>
    <img src="a.jpg" alt="">
    
</body>
</html>



"""

from bs4 import BeautifulSoup

soup=BeautifulSoup(documan_list,'html.parser') 
result=soup.prettify #prettify komutu girintileri karışık olan html kodlarını dzeünliyor.
result=soup.title    #title etiketini alır. 
result=soup.head     #head etiketini alır.
result=soup.body     #body etiketini alır.


result2=soup.title.string #title ın string değerini alır.

result=soup.h1 #h1 etiketini alır.
result=soup.h2.string #ilk h2 etiketini getirir.
result=soup.find_all("h2")  #sayfada bulunan bütün h2 etiketlerini getirir
result=soup.find_all('h2')[0] #0.indexdeki h2 yi alır. not:Bütün h2 ler yazdırılırken liste şeklinde yazıdırılır. 
result=soup.find_all('div')  #bütün div leri bulur ve liste şeklinde gösterir
result=soup.find_all("div")[0].ul.find_all("li")
result=soup.div.findChildren() #div etiketi altındaki bütün alt elemanlar gelir
result=soup.div.findNextSibling()  #Birden fazla div oludugunda 2. dive geçmek için kullanılır
result=soup.div.findNextSibling().findNextSibling()  #2 div birden geçer
result=soup.findPreviousSibling() #bi önecki dive gider
result=soup.find_all('a') # a etiketine ulaşırız
print(link.get("href")) #a etiketi içindeki linkleri yazdırır

print(result)