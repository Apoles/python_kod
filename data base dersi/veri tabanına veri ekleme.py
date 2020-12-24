import sqlite3

con=sqlite3.connect("adli.db")

cursor=con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT,soyad TEXT,numara İNT)")
def degerekle():
    b=input("ad gir:")
    c=input("soyad gir:")
    d=int(input("yaş gir:"))
    liste=[(b,c,d)]
    g=len(liste)
    print("boyutunuz",g)
    print(liste)
    for veri in liste:
        cursor.execute("INSERT INTO ogrenciler VALUES(?,?,?)", veri)
            
def okuma():
    cursor.execute("SELECT *FROM ogrenciler")
    ogrenciler=cursor.fetchall()
    print("\n",ogrenciler)
    con.commit()
    con.close()
tabloolustur()
a=input("deger eklensinmi y/n:")
if a=="y":
    degerekle()
else:
    print("deger eklenmedi")
okuma()
