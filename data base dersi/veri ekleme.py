import sqlite3 
baglan=sqlite3.connect("Ne_severiz_ne_yapariz.db")
imlec=baglan.cursor()

def tablo_olusturma():
    imlec.execute("CREATE TABLE IF NOT EXISTS telefon_kaydı (ad TEXT,Soyad TEXT,numara İNT,TC_kimlik İNT)")
def veri_girme():
    ad=input("Adınızı girin:")
    soyad=input("soyad giriniz:")
    Telno=int(input("Telefon giriniz:"))
    Tckml=int(input("TC giriniz:"))
    liste=[(ad,soyad,Telno,Tckml)]
    for i in liste:
        imlec.execute("INSERT INTO telefon_kaydı VALUES(?,?,?,?)",i)
def okuma():
    imlec.execute("SELECT *FROM telefon_kaydı")
    veri=imlec.fetchall()
    print(veri)
    baglan.commit()
    baglan.close()
tablo_olusturma()
a=input("Deftere veri eklemek istiyorumusunuz y/n:")
while True:
    if a=="y":
        veri_girme()
        c=input("başka veri girmek istermsiniz y/n:")
        if c=="y":
            print("veri işlemi bitmiştir")
        else:
            break
    else:
        print("veri girilmedi")
        break
okuma()
