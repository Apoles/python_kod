import pandas as pd
import numpy as np

data={
    "Column1":[1,2,3,4,5,6,7],
    "Column2":[12,23,53,24,15,26,47],
    "Column3":[13,22,32,43,45,66,77],
    "Column4":[11,12,33,45,75,76,27],
    "Column1":["ass","bdd","cas","asd","sdf","dsa","bgd"]

}


df=pd.DataFrame(data)


result=df
result=df["Column2"].unique() #tekrarlamayan bilgileri getirir

result=df["Column1"].nunique() #sutundaki eleman sayısı
result=df["Column2"].value_counts() #sutundaki elemanlaın ne kadar tekrar ettıgını gosterir



def kareal(x):
    
    return x * x


result=df["Column2"].apply(kareal) #apply metodu ile sutundakı her bilgiyi parametre olarak kara al fonlsıyonuna atar
result=df["Column3"].apply(lambda x:x*x) #bir başka yöntem kare alma
result=df.sort_values("Column1") #azdan  çoğa doğru sıralara sutunlardakı sayıları veya harfrleri




print(df.pivot_table(index="Column1",columns="Column2",values=("Column3")))










print(result)