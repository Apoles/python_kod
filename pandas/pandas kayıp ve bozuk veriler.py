import pandas as pd
import numpy as np


data=np.random.randint(10,100,15).reshape(5,3)

df=pd.DataFrame(data, index=["a","c","e","f","h"], columns=["clm1","clm2","clm3"])

df=df.reindex(["a","b","c","d","e","f","g","h"])
result=df


result=df.drop("clm1",axis=1) #colmuns 1 i siler
result=df.drop("a",axis=0) # a indexsini siler

result=df.isnull() # nan olan değerleri false olarak döndürür
result=df.notnull() # nan olmayan veri olan değerleri false döndürür
result=df.isnull().sum() #nan değerleri toplar kaç tane oldugunu  gösterir
result=df["clm2"].isnull().sum() #columns 2 deki nan değerleri toplar


newColumn=[np.nan,30,np.nan,51,np.nan,10,20,90]
df["clmn4"]=newColumn #yeni columns olşturduk

#print(df)

result=df

result=df[df["clmn4"].isnull()] #column 4 deki nan ları getirir
result=df[df["clmn4"].isnull()]["clmn4"]["a"]


result=df.dropna() #satırda nan değeri v varsa satırı siler 
result=df.dropna(axis=1) #sütüda nan değeri varsa sutunu siler
result=df.dropna(how="all") # tüm satır nan ise satırı siler
result=df.dropna(subset=["clm2","clm1"]) # subset metodu ile sadece column lara bakılır
result=df.dropna(subset=["clm2","clm1"],how="all")

result=df.fillna(value="no input") #nan değerlere kendimiz bilgi atayaibliyoruz




print(result)
