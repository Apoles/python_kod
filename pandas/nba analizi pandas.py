import pandas as pd
import numpy as np


data=pd.read_csv("nba.csv")

#print(data)


result=data


result=data.columns


result=data.head(10)  # ilk 10 kayıt

result=len(data.index)  #satır bilgilei
result=len(data.columns) #sütün bilgileri

result=data["height"].mean()   # boy ortalaması alındı

result=data["height"].max()   #  en yüksek boy

result=data[data["height"]==data["height"].max()]["Player"]  # max bouylu insan kımdır

result=data[data["born"]>=1995][["Player","birth_city","born"]].sort_values("born") 

result=data[data["Player"]== "Gil McGregor"]["collage"]

result=data.groupby(["birth_state"]).mean()["height"].head()
result=data["birth_state"].nunique()  #kaç farklı şehir mevcut

















print(result)

