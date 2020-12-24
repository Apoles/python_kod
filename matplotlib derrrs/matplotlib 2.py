import matplotlib.pyplot as plt
import numpy as np

"""örnek 2 """

x=np.linspace(0,2,100)
"""
plt.plot(x,x,"o--r",label="lineer")
plt.plot(x,x*x,"-g",label="kare")
plt.plot(x,x*x*x,"--y", label="küb")
plt.plot(x,x*x*x*x,"--p", label="4. kuvvet")
plt.xlabel("xlabel")
plt.ylabel("ylabel")

plt.legend()

plt.title("grafffik")




plt.show()"""


figür,axs=plt.subplots(2) # 2 tane grafik alt alta oluşturduk

axs[0].plot(x,x,color="red")
axs[1].plot(x,x*x,color="green") 

plt.show()