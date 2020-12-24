"""class Dusman:
    kalan_can=3
    def saldır(self):
        print("hücüüüüüüüm")
        self.kalan_can-=1
    def hayatta_mı(self):
        if (self.kalan_can<=0):
            print("öldür")
        else:
            print(str(self.kalan_can)+"canın kaldı")"""


"""class Dusman:
    def __init__(self,isim,kalan_can,saldırı_gucu,mermi_sayisi):
        self.isim=isim
        self.kalan_can=kalan_can
        self.saldırı_gucu=saldırı_gucu
        self.mermi_sayisi=mermi_sayisi

    def yazdır(self):
        print("basılıyor........")
        print("isim:",self.isim,"can:",self.kalan_can,"saldırı gücü:",self.saldırı_gucu,"mermi sayısı",self.mermi_sayisi)




dusman1=Dusman("Ali",2000,30,50)
dusman2=Dusman("APO",3000,50,23)

print("Dusman1*****************")
dusman1.yazdır()
print("dusman2************")
dusman2.yazdır()
dusman1.yazdır()"""


import random
class Dusman:
    def __init__(self,isim,kalan_can,saldırı_gucu,mermi_sayisi):
        self.isim=isim
        self.kalan_can=kalan_can
        self.saldırı_gucu=saldırı_gucu
        self.mermi_sayisi=mermi_sayisi

    def yazdır(self):
        print("basılıyor........")
        print("isim:",self.isim,"can:",self.kalan_can,"saldırı gücü:",self.saldırı_gucu,"mermi sayısı",self.mermi_sayisi)
    def saldır(self):
        print(self.saldır+"saldırıyor")
        harcanan_mermi=random.randrange(0,10)
        print(str(harcanan_mermi)+"kadar harcandı")
        self.mermi_sayisi-=harcanan_mermi
        return(harcanan_mermi,self.saldırı_gucu)
    def saldırıya_ugra(self,harcanan_mermi,saldırı_gucu):
        print("vuruldum")
        self.kalan_can-=(harcanan_mermi*saldırı_gucu)
    def mermi_bittimi(self):
        if(self.mermi_sayisi<=0):
            print(self.isim+"konusuyor mermi bitti oyunda çıkıyorum")
            return True
        return False
    def hayattamı(self):
        if (self.kalan_can<0):
            print("öldümmmmmmm")
dusmanlar=[]

i=0
while(i<10):
    rastgelecan=random.randrange(100,200)
    rastgelesaldırıgucu=random.randrange(10,20)
    rastgelemermi=random.randrange(20,30)
    yenidusman=Dusman("dusman"+str(i+1),rastgelecan,rastgelesaldırıgucu,rastgelemermi)
    dusmanlar.append(yenidusman)

    i+=1
for dusman in dusmanlar:
    dusman.yazdır()
input()
input()
    
