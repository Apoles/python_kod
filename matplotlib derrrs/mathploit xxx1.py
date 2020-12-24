import matplotlib.pyplot as plt
import numpy as np

"""örnek 1 """

x=[1,2,3,4]
y=[1,4,9,16]


plt.plot(x,color="black",linewidth=10)#kalınlık bilgisi  # x grafiği olşturduk


plt.plot(x,y,color="red",linestyle="--")  # x e karşılık y grafiği olşturduk



#        fmt=[marker][line][color]          şeklinde seçilir 
plt.plot(y,"o--r") # o marker -- line r color    hepsini vermek zorunda değiliz



plt.axis([0,6,0,20])  # x 0 da başladı 6 da bitti   y 0 dan başladı 20 de bitti aralıkları belirtiriyor

plt.title("hello world") #ana başlık oluşturuldu
plt.xlabel("hellllo wordl x") # x başıgı
plt.ylabel("hellllo world y") # y başlıgı










plt.show()   #  garfiği gösterdik



