import pandas as pd
import numpy as np

customers={
    'CustomerId':[1,2,3,4],
    'FirstName':["Ahmet","Ali","Hasan","Canan"],
    "LastName":["Gümüş","Elmas","Altun","Güzel"]
}

Orders={
    "OrderId":[10,11,12,13],
    "CustomerId":[1,2,5,7],
    'OrderDate':['2010-07-04',"2010-08-04","2010-09-04","2010-10-04"]

}

df_Customers=pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
df_Orders=pd.DataFrame(Orders,columns=["OrderId","CustomerId","OrderDate"])

print(df_Customers)
print(df_Orders)



result=pd.merge(df_Customers,df_Orders,how="inner")  #Tabloları birleştiriyoruz inner a göre inner'ı araştır.
print(result)
result=pd.merge(df_Customers,df_Orders,how="left") #Left e göre  birleştirir
print(result)
result=pd.merge(df_Customers,df_Orders,how="right") #right a göre birleştirir
print(result)
result=pd.merge(df_Customers,df_Orders,how="all")
print(result)
