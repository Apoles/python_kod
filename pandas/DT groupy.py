import pandas as pd
import numpy as np


df=pd.read_excel("Çalışan.xlsx")
result=df

print(df)
result=df["maaş"].sum() #maaş bilgisi toplamı
print(result)

result=df.groupby("İş").groups # iş sutunundakı benzer işleri gruplandırdık

result=df.groupby(["İş","şehir"]).groups # iş ve şehiri aynı olaları grupladık

şehirler=df.groupby("şehir")

for name,group in şehirler:
    print(name)
    print(group)

#yukarıdaki döngüde şehirleri grupladık ve döngü ile şehirleri ayırdık name ile şehir ismini group ile de şehirleri gruplara ayırdık


for name,group in df.groupby("İş"):
    print(name)
    print(group)




result=df.groupby("şehir").get_group("Bursa")  #şehiri bursa olan insaları almış oluyoruz
result=df.groupby("İş").sum() #İş leri gruplara ayırıp topluyor saçma

result=df.groupby("İş").mean() #işleri gruplayıp o işdeki insaların yaş ortalamasını ve maaş ortalamasını aldık
result=df.groupby("İş")["maaş"].mean() #sadece maaş bilgilerinin ortalamasını getirdim yukardaki ile farkı bu
result=df.groupby("şehir")["Yaş"].mean()
result=df.groupby("şehir")["Ad"].count() #şehirlere göre gurplara ayırıp kaç kişinin çalıştıgını hesapladı
result=df.groupby("İş")["Yaş"].max() #işlerdeki insaların max yaşını hesapladı
result=df.groupby("İş")["Yaş"].max()["Öğrenci"] #sadece öğrenci seçildi yukardakinde farklı olarak
result=df.groupby("İş").agg(np.mean)

result=df.groupby("İş")["maaş"].agg(np.max,np.min)









print(result)