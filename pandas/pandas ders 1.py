
import pandas as pd
import numpy as np


#data
numbers=[20,30,40,50]
letters=["a","b","c","d"]
pandas_series=pd.Series(numbers)
letters_series=pd.Series(letters)

print(pandas_series)
print(letters_series)
"""
result=pd.Series(5,[0,1,2,3,4]) #5 değerini verdiğimiz indexlere dağıtır
print(result)

resulta=pd.Series(numbers,["a","b","c","4"])
print(result)

random_numbers=np.random.randint(10,100,6)

dict={"a":10,"b":20,"c":30}
result=pd.Series(dict)
print(result)

result=pd.Series(random_numbers)
print(result)

a=resulta["a"]
print(a)
a=result[:3]
print(a)

resulta=pd.Series(numbers,["a","b","c","4"])

a=resulta.ndim #boyut verir
print(a)

a=resulta.dtype #data tipini verir
a=resulta.shape #data tipinin matrslerini verir 4 e 1 , 3 e 2 gibi 
a=resulta.sum() #elemanlarını toplar
a=resulta.max() #max değerini verir 

a=resulta[resulta>=30]
print(a)

"""


#                    ~~~~~~~~~~~~  DATA FRAME ~~~~~~~~~~~~

"""import pandas as pd
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

"""