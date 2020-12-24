import pandas as pd 
import numpy as np



#df=pd.read_csv("got_deaths.csv",encoding="utf-8")
#df=pd.read_json("GoT-deaths-by-season.json")
df=pd.read_csv("apoles.csv")



result=df

result=df.columns
result=df.info




#    PANDAS HAKKINDA QUİZ SORULARU VE CEVAPLARI 
#1
"""result=df.head()
print(result)

#2

result=df.head(10)
print(result)

#3

result=df.tail()
print(result)
"""
#4
result=df.columns
print(result)


result=df[["name","attacker_king","defender_king","attacker_size","defender_size"]].head()


result=df[(df["attacker_size"]<15000) & (df["defender_size"]<3000)][["attacker_king","defender_king","battle_type","location","attacker_size","defender_size","region","note"]]




print(result)

