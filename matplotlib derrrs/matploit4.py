import matplotlib.pyplot as plt


yil=[2011,2012,2013,2014,2015]

oyuncu1=[8,7,6,8,4]
oyuncu2=[33,12,32,23,19]
oyuncu3=[2,3,5,1,2]


#stack plot

plt.plot([],[],color="y",label="Messi")
plt.plot([],[],color="r",label="Abdullah gümüş")
plt.plot([],[],color="b",label="Çağlar")


plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
plt.title("Yıllara göre atılan gol")
plt.legend()
plt.xlabel("yıl")
plt.ylabel("gol")




#pasta grafiği

gol_tipi="Penaltı","Serbest vuruş","ceza sahası dışı","ceza sahası içi"

gol_sayisi=[5,4,12,14]
colors=["r","b","g","y"]



plt.pie(gol_sayisi,labels=gol_tipi,colors=colors,shadow="True",explode=(0.05,0.05,0.05,0.05),autopct="%1.1f%%")  #shadow =gölge explode = aralardaki boşluklar autopct= yüzde dilimi gösterme


#bar grafiği

plt.bar([0.25,1.25,2.25,3.35,4.25],[50,49,56,80,23],label="bmw",width=.5)
plt.bar([0.23,1.15,2.15,3.25,2.25],[20,29,76,60,83],label="Honda",width=.5)
plt.legend()
plt.xlabel("Gün")
plt.ylabel("mesafe(km")
plt.title("Araç bilgisi")

#histogram grafiği

yaslar=[22,33,34,54,65,12,54,87,45,34,56,32,55,12,16,17,24,66,33,43,59,76]
yas_grupları=[0,10,20,30,40,50,60,70,80]

plt.hist(yaslar,yas_grupları,histtype="bar",rwidth=0.8,color="r")

plt.xlabel("Yaş grupları")
plt.ylabel("kişi sayısı")
plt.title("histogram")




plt.show()