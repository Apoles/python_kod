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




"""import random
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
        print(self.isim+"saldırıyor")
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
#for dusman in dusmanlar:
 #   dusman.yazdır()    
i=0
while (i<3):
    randomdusman1=random.randrange(0,10)
    randomdusman2=random.randrange(0,10)
    donen_deger=dusmanlar[randomdusman1].saldır() #harcanan mermi 15 saldırı gucu 5 ise  0. insex 15 1. index 5

    dusmanlar[randomdusman2].saldırıya_ugra(donen_deger[0],donen_deger[1])
    print("raund bitti")
    i+=1 """

#karmaşık class kullanarak saldırmalık oyun
# nesne tabanlı programlama
#ingiliz alman italyan türk amerika

"""import time
import random

class rekabet():
    def __init__(self, isim, can, saldiri_gucu, kalan_mermi):
        self.isim=isim
        self.can=can
        self.guc=saldiri_gucu
        self.kalan_mermi=kalan_mermi

    def saldir(self):
        print(self.isim, "saldırıyor!")
        harcanan_mermi=random.randrange(1,10)

        if (self.kalan_mermi <= harcanan_mermi):
            harcanan_mermi=self.kalan_mermi
            print(str(self.kalan_mermi), "mermi harcandı.")
        else:
            print(str(harcanan_mermi), "mermi harcandı.")
        self.kalan_mermi -= harcanan_mermi

        return(harcanan_mermi, self.guc)

    def vuruldu(self, harcanan_mermi, guc):
        print(self.isim, "vuruldu.\n")
        self.can -= (guc * harcanan_mermi)

    def mermi_bitti_mi(self):
        if(self.kalan_mermi<=0):
            print(self.isim, "konuşuyor: Mermim bitti! Çekiliyorum.")

            if(len(dusmanlar)==1):
                return
            dusmanlar.remove(self)

            return True
        return False

    def hayatta_mi(self):
        if(self.can<=0):
            print(self.isim, "öldü.")

            dusmanlar.remove(self)

            return True
        return False


    def print(self):
        time.sleep(2)
        print(self.isim+",", "Can: {} Saldırı gücü: {} Mermi sayısı: {}".format(self.can,self.guc,self.kalan_mermi))

    def kazanan(self):
        return self.isim

#----------------------------------------------------------------------
#----------------------------------------------------------------------



dusmanlar= []
karakter_isimleri=["Türk Askeri","Rus Askeri","Amerikan Askeri","İtalyan Askeri","Fr
eri"]



i=0
while(i<5):
    rastgele_isim = karakter_isimleri[i]
    rastgele_can = random.randrange(200, 350)
    rastgele_guc = random.randrange(15, 20)
    rastgele_mermi = random.randrange(15, 20)
    dusman = rekabet(rastgele_isim, rastgele_can, rastgele_guc, rastgele_mermi)
    dusmanlar.append(dusman)
    i+=1





print("Düşmanlar basılıyor...\n")
time.sleep(3)


random.shuffle(dusmanlar)
for dusman in dusmanlar:
    dusman.print()
    i+=1



print("\nDüşmanlar birbirine saldırıyor...\n")
time.sleep(3)



while(True):
    if (len(dusmanlar)==5):
        dusman1 = random.randint(0,4)  # 0 ve 4 dahil. random.randrange(0,4) yapsaydık 0 dahil olacak ama 4 olmayacaktı.
        dusman2 = random.randint(0,4)
        if (dusman2 == dusman1) or ((dusman2>dusman1) and (dusman2==4)):
            continue
        else:
            print("\n\n")
            donen_deger = dusmanlar[dusman1].saldir()  # return ile "donen_deger"e iki tane argüman atadık.
            dusmanlar[dusman2].vuruldu(donen_deger[0], donen_deger[1])
            time.sleep(2)

            dusmanlar[dusman1].mermi_bitti_mi()
            dusmanlar[dusman2].hayatta_mi()

            time.sleep(4)


    elif (len(dusmanlar) == 4 ):
        dusman1 = random.randint(0,3)
        dusman2 = random.randint(0,3)
        if (dusman2 == dusman1) or ((dusman2>dusman1) and (dusman2==3)):
            continue
        else:
            print("\n\n")
            donen_deger = dusmanlar[dusman1].saldir()  # return ile "donen_deger"e iki tane argüman atadık.
            dusmanlar[dusman2].vuruldu(donen_deger[0], donen_deger[1])
            time.sleep(2)

            dusmanlar[dusman1].mermi_bitti_mi()
            dusmanlar[dusman2].hayatta_mi()

            time.sleep(4)


    elif (len(dusmanlar) == 3 ):
        dusman1 = random.randint(0,2)
        dusman2 = random.randint(0,2)
        if (dusman2 == dusman1) or ((dusman2>dusman1) and (dusman2==2)):
            continue
        else:
            print("\n\n")
            donen_deger = dusmanlar[dusman1].saldir()  # return ile "donen_deger"e iki tane argüman atadık.
            dusmanlar[dusman2].vuruldu(donen_deger[0], donen_deger[1])
            time.sleep(2)

            dusmanlar[dusman1].mermi_bitti_mi()
            dusmanlar[dusman2].hayatta_mi()

            time.sleep(4)

    elif (len(dusmanlar) == 2 ):
        dusman1 = random.randint(0,1)
        dusman2 = random.randint(0,1)
        if (dusman2 == dusman1) or (dusman2==0):
            continue
        else:
            print("\n\n")
            donen_deger = dusmanlar[dusman1].saldir()  # return ile "donen_deger"e iki tane argüman atadık.
            dusmanlar[dusman2].vuruldu(donen_deger[0], donen_deger[1])
            time.sleep(2)

            dusmanlar[dusman2].hayatta_mi()
            dusmanlar[dusman1].mermi_bitti_mi()

            time.sleep(4)


            if(len(dusmanlar)==1):
                kazanan_dusman1=dusmanlar[0].kazanan()
                print("\nSAVAŞ BİTTİ!")
                print("Kazanan: {}".format(kazanan_dusman1))
                input()
                break



    elif (len(dusmanlar) == 1):
        kazanan_dusman2=dusmanlar[0].kazanan()
        print("\nSAVAŞ BİTTİ!")
        print("Kazanan: {}".format(kazanan_dusman2))
        input()
        break

    else:
        print("HERKES ÖLDÜ, KAZANAN YOK!")
        input()
        break   """




"""class Çalışan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()

    def personel_sayısını_görüntüle(self):
        print(len(self.personel))

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    def personeli_görüntüle(self):
        print('Personel listesi:')
        for kişi in self.personel:
            print(kişi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)   """

"""class Calısan():
    def __init__(self,isim,maas,departman):
        print("çalışan sınıfının yapıcı fonksiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgileri_göster(self):
        print("çalışan sınıfnın bilgileri gösteriliyor")
        print("isim:",self.isim,"maaş",self.maas,"departman",self.departman)
    def zam_yap(self,zam_miktari):
        print("zam yapılıyor")
        self.maas+=zam_miktari
        print(self.maas)
    def departmandegiştir(self,yeni_departman):
        print("yeni departman olusuturuluyot")
        self.departman=yeni_departman
    

calısan=Calısan("apoles",2400,"yazılımcı")
calısan.bilgileri_göster()
calısan.zam_yap(2500)
calısan.zam_yap(2500)

class Yonetici(Calısan):
    def __init__(self, isim, maas, departman,kisi_sayısı):
        print("yöneticinin yapıcı fonksiyonu")
        self.isim=isim          
        self.maas=maas
        self.departman=departman
        super().__init__(isim,maas,departman) #yukardaki gibi kod kalabılıgı yapmasın diye yukardaki init fonksiyonunu cagırdık
        self.kisi_yasısı=kisi_sayısı #ek özellik
        super().bilgileri_göster()
    def bilgileri_göster(self):
        print("yönetici sınıfının bilgieri gösterilyor...")
        print("isim:",self.isim,"maaş",self.maas,"departman",self.departman,"çalışan sayısı:",self.kisi_yasısı)
    def kisisayısı_arttır(self,arttır):
        print("kişi sayısı arttırılıyor")
        self.kisi_yasısı+=arttır


yönetici=Yonetici("ali",3000,"mal",30)
yönetici.bilgileri_göster()
yönetici.kisisayısı_arttır(12)
yönetici.bilgileri_göster()"""





"""class movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("olusturuldu")
    def isim(self):
        print("isim:",self.title,"yapmcı:",self.director,"süre:",self.duration)
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print("silidni")



m=movie("sövme anama sövme","apoles",1)
m.isim()
print(str(m))

print(len(m))

del m

try:
    print(m)
except:
    pass """


     
