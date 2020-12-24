import pandas as pd 

"""data=pd.read_csv("nba.csv")

data.dropna(inplace=True)

result=data
#print(data.columns)
print(data)
data["Player"]=data["Player"].str.upper()  #player sutununun hepsi büyük harf yaptık

data["Player"]=data["Player"].str.lower()  #hepsi küçük oldu

data["index"]=data["Player"].str.find("a") #index datası oluşturp player sutunundaki a yı bulup index numarasını yazdırdık


data=data[data.Player.str.contains("jordan")]  #Player sutununda isim arattık


data=data.Player.str.replace(" ","-") #  replace metodu ile boşluk karakterlerinin yerine çizgi karakteri koyuyoruz



print(data.head(15))

print(result)



result[['First name'],["last name"]]=result["Player"].loc[result["Player"].str.split().str.len()==2].str.split(expand=True)  """

