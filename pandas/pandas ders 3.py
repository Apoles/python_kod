import pandas as pd

"""
df=pd.read_csv("anan.csv")

print(df) """

from numpy.random import randn


df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Columns1","Columns2","Columns3"])

result=df
result=df["Columns1"] #sutun seçme
result=df[["Columns1","Columns2"]] #Birden fazla sutun seçme


result=df.loc["A"]  #satırı seçer
result=df.loc["A","Columns3"] #satır ve sütün bilgisi verdiğimiz değeri seçdi
result=df.loc[:,"Columns2"] #sadece sütün seçdik
result=df.loc[:,"Columns1":"Clomuns3"] #sutun 1 ile sutun 3  arasını seçdik   başlangıç ve bitiş dahil
result=df.loc["A":"B","Columns1":"Columns3"] #A ile B arasındakı satırlardan sutun 1 ve sutun 3 e kadar olanları seçdik 

df["Columns4"]=pd.Series(randn(3),["A","B","C"])  #sutun 4 ü ekledik
print(df.drop("Columns4",axis=1)) #seçilen sutunları siler    axis=1  y ekseni yukardan aşşa axis=0 x ekseni sağdan sola


#print(result)


print(df)
