
"""numberss=np.array([0,5,10,15,20,25,50,75])


result=numberss[5]
print(result)

result=numberss[0:3] #0 ile 3 arasındaki indexler
result=numberss[:3] #aynı bok
result=numberss[:3] #3 den sona kadar
result=numberss[::] #tüm liste
  #dizinin çok boyutlu yanı matrsi oldugu durumda
result=numberss[0,2] #0.satırın 2. indexdeki elemanı
result=numberss[:,2] #bütün satırlardan 2. indexdeki elemanı almak
result=numberss[:,0:2] # tüm satırlardakı 0 ile 2. index elemanları"""



"""
numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result=numbers2+numbers2 #dizileri toplar


mnumber1=numbers1.reshape(2,3)
mnumber2=numbers2.reshape(2,3)



result=np.vstack((numbers1,numbers2)) #matrsileri dikey olarak birleştirir
result=np.hstack((numbers1,numbers2)) #matrisleri yatay olarak birleştirir

result=numbers1 >=5 #elemenları kontrol eder 5 den buyukse true değeri döner
print(numbers1[result])  #matrisde sadece koşulu sağlayan elemanları dizi içinde gösteririr yukarıda koşul verilmiştir
"""



#NUMPY VERİ ANALİZİ PROGRAM

import numpy as np






sr1=np.array([10,15,30,45,60])
sr2=np.arange(5,16)
sr3=np.arange(50,100,5)
sr4=np.zeros(10)
sr5=np.ones(10)
sr6=np.linspace(0,100,5)
sr7=np.random.randint(10,30,5)
sr8=np.random.randn(5)

sr9=np.random.randint(10,50,15)
result=sr9.reshape(3,5)
print(result)



print(result.sum(axis=1))
print(result.sum(axis=0))

a=result.max()
print(a)
a=result.min()
print(a)
a=result.mean()
print(a)

a=result.argmax()
print(a)



matris=np.arange(10,20)


a=matris[:3]
print(a)

a=matris[::-1]
print(a)

a=result[1,2]
print(a)

a=result**2
print(a)

nicem=np.arange(-50,50)

çift=nicem[nicem %2==0]
pzitif=çift[çift>0]
print(pzitif)

















