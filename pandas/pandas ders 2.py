#                    ~~~~~~~~~~~~  DATA FRAME ~~~~~~~~~~~~

import pandas as pd
import numpy as np


s1=pd.Series([3,2,0,1])
s2=pd.Series([0,3,7,2])

data=dict(apples=s1,oranges=s2) #dict tanımlaması yapıldı

df=pd.DataFrame(data) #dataFrame oluşturuldu
print(df)


df2=pd.DataFrame() #boş bir dataframe
print(df2)

df3=pd.DataFrame([1,2,3,4,5,6]) #liste şeklinde bir dataframe verdik
print(df3)

df4=pd.DataFrame([["Apoles",60],["ali",79],["ayşe",12]])

print(df4)




##################    ##################

data2=[["Apoles",60],["ali",79],["ayşe",12]]  #liste datası

dict2={"name":["Apoles","Ali","ayşe"],"score":[60,79,12]} #dict datası

df5=pd.DataFrame(data2,columns=["name","score"],index=[1,2,3],dtype=str) #columns  ve index bilgierlini default değilde biz kendimiz girdik
print(df5)


df6=pd.DataFrame(dict2,index=["A:","B:","C:"])
print(df6)


dic_list=[
    {"name":"ahmet","score":50},
    {"name":"Ali","score":79},
    {"name":"apoles","score":12}
]


df7=pd.DataFrame(dic_list,index=["A-","B-","C-"])   #liste içinde dict yapısı kullandık
print(df7)


