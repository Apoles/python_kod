import matplotlib.pyplot as plt 
import numpy as np

x=np.linspace(-10,9,20)
y=x**3-19*x*x+12*x-90 
z=x*(x/0.5)+2*x+12

"""figure=plt.figure()  #figür oluşturduk

axes=figure.add_axes([0.1,0.1,0.8,0.8])  #sağdadan 0.2 soldan 0.2 yukardan ve aşşağıdan 0.8 kaydıracak konumunu

axes.plot(x,y,"r")
axes.set_xlabel("x axis")
axes.set_ylabel("ylabel")
axes.set_title("HELLO WORLD")


axes2=figure.add_axes([0.1,0.1,0.8,0.8])

axes2.plot(x,z,"g")
axes2.set_xlabel("x axis")
axes2.set_ylabel("ylabel")
axes2.set_title("HELLO WORLD")
"""

"""figure=plt.figure()
axes=figure.add_axes([0,0,1,1])
axes.plot(x,z,label="müko")
axes.plot(x,y,label="mükkkkkkkooo")
axes.legend()
"""




fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(4,4))

axes[0].plot(x,y)
axes[0].set_title("wierd table")
axes[1].plot(x,z)
axes[1].set_title("double wierd table")

plt.tight_layout()  #tablolar biribirine karışmasın diye

fig.savefig("figure1.svg")


plt.show()
