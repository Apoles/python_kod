import clr
import time
import pyfiglet
print(dir())
ascii_banner = pyfiglet.figlet_format("APOLES",font="standard")
print(ascii_banner)


time.sleep(0.1)
print(clr.red.italic.on_black("   ||#########||       ||         ||       #######    ||############     "))
time.sleep(0.1)
print(clr.red.italic.on_black("  ||           ||      ||         ||    ###           ||                 "))
time.sleep(0.1)
print(clr.red.italic.on_black(" ||             ||     ||         ||   ###            ||                 "))
time.sleep(0.1)
print(clr.red.italic.on_black("||               ||    ||#########||     ####         ||                 "))
time.sleep(0.1)
print(clr.red.italic.on_black("||               ||               ||       ####       ||############     "))
time.sleep(0.1)
print(clr.red.italic.on_black("||###############||               ||            ##    ||                 "))
time.sleep(0.1)
print(clr.red.italic.on_black("||               ||               ||             ##   ||                 "))
time.sleep(0.1)
print(clr.red.italic.on_black("||               ||               ||          ####    ||                 "))
time.sleep(0.1)
print(clr.red.italic.on_black("||               ||     ##########||     #######      ||############     "))
print("")
print(clr.red("-------------------------------------------------------"))
time.sleep(0.5)
print("\n\nPrograma Hoşgeldiniz:")
print("")
print("")
time.sleep(0.5)
print(clr.red("-------------------------------------------------------"))
print("")
print("Bu programın komutlarını görmek için /help yazınız.")
print("")
print(clr.red("-------------------------------------------------------"))
time.sleep(0.3)
while True:
    a=input("===>")
    if a=="/help":
        time.sleep(0.3)
        print("/hesap_makinesi --------> hesap makinesini açar ")
        time.sleep(0.1)
        print("/search_file    --------> Dosya içinde kelime arayan aracı açar")
    elif a=="/hesap_makinesi":
        print("Hesap Makinesine Hoşgeldiniz......")
        while(True):
            import time
            print(50*"$")
            time.sleep(0.1)
            print("1)Toplama")
            time.sleep(0.1)
            print("2)Çıkarma")
            time.sleep(0.1)
            print("3)Çarpma")
            time.sleep(0.1)
            print("4)Bölme")
            time.sleep(0.1)
            print("5)Üs Hesaplama")
            time.sleep(0.1)
            print("6)Faktoriyel Hesaplama")
            time.sleep(0.1)
            print("7)2 Sayının Ortalamasını Hesaplama")
            time.sleep(0.1)
            print("8)3 Sayının Ortalamasını Hesaplama")
            time.sleep(0.1)
            print("9)4 Sayını Ortalamasını Hesaplama")
            time.sleep(0.1)
            print("10)5 Sayının Ortalamasını Hesaplama")
            time.sleep(0.1)
            print("11)6 Sayının Ortalamasını Hesaplama")
            time.sleep(0.1)
            print("12)7 Sayının Ortalamasını Hesaplama")
            time.sleep(0.1)
            print("13)8 Sayının Ortalamasını Hesaplama")
            time.sleep(0.1)
            print("14)9 Sayının Ortalamasını Hesaplama")
            time.sleep(0.1)
            print("15)10 Sayının Ortalamasını Hesaplama")
            time.sleep(0.1)
            print("16)Çıkış")
            time.sleep(0.1)
            print(50*"$")

            cevap=int(input("Yapmak İstediğiniz İşlemin Değerini Girin:"))
            if(cevap==1):
                aaa=int(input("Birinci Değeri Girin:"))
                aab=int(input("İkinci Değeri Girin:"))
                topl=aab+aaa
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Sonuç:",topl)
                time.sleep(3)
                continue
            elif(cevap==2):
                aac=int(input("(Eksilecek Değer)Birinci Değeri Girin:"))
                aad=int(input("(Çıkarılacak Değer)İkinci Değeri Girin:"))
                cikr=aac-aad
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Sonuç:",cikr)
                time.sleep(3)
                continue
            elif(cevap==3):
                aaf=int(input("Birinci Değeri Girin:"))
                aae=int(input("İkinci Değer Girin:"))
                carp=aae*aaf
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Sonuç:",carp)
                time.sleep(3)
                continue
            elif(cevap==4):
                print("Bölüm'den Kalanın mı hesaplanmasını istersiniz?\nYoksa Sonucun mu?\nSonuc:2\nKalan:1\nCevap")
                cevap1=int(input("Cevap:"))
                if(cevap1==1):
                    aaz=float(input("(Bölünen)Birinci Değeri Girin:"))
                    aak=float(input("(Bölen)İkinci Değeri Girin:"))
                    Kalan=aaz%aak
                    print("Hesaplanıyor....")
                    time.sleep(2)
                    print("Kalan:",Kalan)
                    time.sleep(3)
                    continue
                aan=float(input("(Bölünen)Birinci Değeri Girin:"))
                aao=float(input("(Bölen)İkinci Değeri Girin:"))
                sonuc=aan/aao
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Sonuç:",sonuc)
                time.sleep(3)
                continue
            elif(cevap==5):
                aas=int(input("(Taban)Birinci Değeri Girin:"))
                us=int(input("(Üs)İkinci Değeri Girin:"))
                sonuc2=aas**us
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Sonuç:",sonuc2)
                time.sleep(3)
                continue
            elif(cevap==6):
                faktoriyel = 1
                while (True):
                    sayi = int(input("Negatif Olmayan Bir Değer Giriniz:"))
                    if (sayi <= 0):
                        print("Lütfen Negatif Olmayan Bir Değer Giriniz:")
                    else:
                        for a in range(1, sayi + 1):
                            faktoriyel = faktoriyel * a
                        print("Hesaplanıyor....")
                        time.sleep(2)
                        print("Faktöriyel", faktoriyel)
                        break
                time.sleep(3)
                continue
            elif(cevap==7):
                x=int(input("Birinci Değeri Girin:"))
                y=int(input("İkinci Değeri Girin:"))
                ort=(x+y)/2
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Ortalama:",ort)
                time.sleep(3)
                continue
            elif(cevap==8):
                ft=int(input("Birinci Değeri Girin:"))
                fh=int(input("İkinci Değeri Girin:"))
                fr=int(input("Üçüncü Değeri Girin:"))
                ort2=(ft+fh+fr)/3
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Ortalama:",ort2)
                time.sleep(3)
                continue
            elif(cevap==9):
                hy=int(input("Birinci Değeri Girin:"))
                hr=int(input("İkinci Değeri Girin:"))
                tg=int(input("Üçüncü Değeri Girin:"))
                yj=int(input("Dördüncü Değeri Girin:"))
                ort1=(hy+hr+tg+yj)/4
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Ortalama:",ort1)
                time.sleep(3)
                continue
            elif(cevap==10):
                rf=int(input("Birinci Değeri Girin:"))
                xc=int(input("İkinci Değeri Girin:"))
                po=int(input("Üçüncü Değeri Girin:"))
                ki=int(input("Dördüncü Değeri Girin:"))
                plk=int(input("Beşinci Değeri Girin:"))
                ort6=(rf+xc+po+ki+plk)/5
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Ortalama:",ort6)
                time.sleep(3)
                continue
            elif(cevap==11):
                tre=int(input("Birinci Değeri Girin:"))
                tger=int(input("İkinci Değeri Girin:"))
                trf=int(input("Üçüncü Değeri Girin:"))
                rfe=int(input("Dördüncü Değeri Girin:"))
                yhu=int(input("Beşinci Değeri Girin:"))
                tgrf=int(input("Altıncı Değeri Girin:"))
                ort4=(tre+tger+trf+rfe+yhu+tgrf)/6
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Ortalama:",ort4)
                time.sleep(3)
                continue
            elif(cevap==12):
                qwerty=int(input("Birinci Değeri Girin:"))
                yhuj=int(input("İkinci Değeri Girin:"))
                plok=int(input("Üçüncü Değeri Girin:"))
                wesd=int(input("Dördüncü Değeri Girin:"))
                tyuj=int(input("Beşinci Değeri Girin:"))
                yujk=int(input("Altıncı Değeri Girin:"))
                trg=int(input("Yedinci Değeri Girin:"))
                ort8=(qwerty+yhuj+plok+wesd+tyuj+yujk+trg)/7
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Ortalama:",ort8)
                time.sleep(3)
                continue
            elif(cevap==13):
                azsd=int(input("Birinci Değeri Girin:"))
                tgre=int(input("İkinci Değeri Girin:"))
                asdf=int(input("Üçüncü Değeri Girin:"))
                tred=int(input("Dördüncü Değeri Girin:"))
                yhbg=int(input("Beşinci Değeri Girin:"))
                hnmk=int(input("Altıncı Değeri Girin:"))
                edcf=int(input("Yedinci Değeri Girin:"))
                tdcs=int(input("Sekizinci Değeri Girin:"))
                ort0=(azsd+tgre+asdf+tred+yhbg+hnmk+edcf+tdcs)/8
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Ortalama:",ort0)
                time.sleep(3)
                continue
            elif(cevap==14):
                rfvg = int(input("Birinci Değeri Girin:"))
                trfg = int(input("İkinci Değeri Girin:"))
                yujo = int(input("Üçüncü Değeri Girin:"))
                wertr = int(input("Dördüncü Değeri Girin:"))
                asdfg = int(input("Beşinci Değeri Girin:"))
                klii = int(input("Altıncı Değeri Girin:"))
                dera= int(input("Yedinci Değeri Girin:"))
                gbhj = int(input("Sekizinci Değeri Girin:"))
                ikir = int(input("Dokuzuncu Değeri Girin:"))
                ort7=(rfvg+trfg+yujo+wertr+asdfg+klii+dera+gbhj+ikir)/9
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Ortalama:",ort7)
                time.sleep(3)
                continue
            elif(cevap==15):
                rtyu = int(input("Birinci Değeri Girin:"))
                ukij = int(input("İkinci Değeri Girin:"))
                ftor = int(input("Üçüncü Değeri Girin:"))
                rotf = int(input("Dördüncü Değeri Girin:"))
                otrf = int(input("Beşinci Değeri Girin:"))
                trof = int(input("Altıncı Değeri Girin:"))
                fort = int(input("Yedinci Değeri Girin:"))
                ortf = int(input("Sekizinci Değeri Girin:"))
                ujky = int(input("Dokuzuncu Değeri Girin:"))
                wertf = int(input("Onuncu Değeri Girin:"))
                ort11=(rtyu+ukij+ftor+rotf+otrf+trof+fort+ortf+ujky+wertf)/10
                print("Hesaplanıyor....")
                time.sleep(2)
                print("Ortalama:",ort11)
                time.sleep(3)
                continue
            else:
                print("Kullandığınız İçin Teşşekkür Ederiz İyi Günler Dileriz..")
                time.sleep(5)
            break
    elif a=="/search_file":
        try:
            fileway = input("Dosya yolunu giriniz: ")
            with open(fileway,"r") as dosya:
                word = input("Kelimenizi giriniz: ")
                ks = len(word)
                toplam = dosya.read()
                toplam = len(toplam)
                print("Toplam karakter sayısı:",toplam)
                s = 0
                for i in range(0,toplam):
                    dosya.seek(i)
                    dosya.read(ks)
                    if(dosya.read(ks) == word):
                        s+=1
                print(s,"adet","'",word,"'","bulundu")
                break
        except FileNotFoundError:
            print("dosya yolu hatalı uygulama kapanıyor...")
        finally:
            continue
    
    else:
        time.sleep(0.5)
        print("hatalı komut girdiniz komut /help ile komutları görebilirsiniz")




