import pandas as pd 
import numpy as np

data =np.random.randint(10,100,75).reshape(15,5)

print(data)

df=pd.DataFrame(data,columns=["columns1","columns2","columns3","columns4","columns5"])
result=df

df.columns  # sutun bilgierini verir
result=df.head() #5 tane satır bilgisi verir
result=df.head(10) #10 tane satır bilgisi verir
result=df.tail() #sondaki 5 satırı seçer

result=df["columns1"].head(5) #sutun 1 deki 5 satırı alıcakdır
result=df[5:15]["columns1"].head(5) #5 ile 15 arasındaki kayıtlardan sutunu 1 olan ilk 5 kaydı alıyoruz
result=df>50 #true false değerlerini koşula bağlı olarak döndürür

result=df[df>50] #50 den kucuk değerlere nan atar
result=df["columns1"]>50 #stuna göre filtreleme
result=df[df["columns1"]>50][["columns1","columns2"]].head()

result=df[(df["columns1"]>50) & (df["columns1"]<70)][["columns1","columns2"]]
result=df.query("columns1>50 & columns2>50")["columns1"]  #koşullu ifadeleri vermenın kısayolu







print(result)



