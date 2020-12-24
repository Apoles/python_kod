import mysql.connector
import time
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Kitap Data",font="standard")
print(ascii_banner)

print("Programımıza hoş geldiniz...")
print("-----------------------------")


def KayıtEtme(liste):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoles123...",
        database="okul"
    )

    cursor=connection.cursor()

    sql="INSERT INTO okul(Id,KitapIsmi,Yazar,Sayfa,Tür,Durum) VALUES(%s,%s,%s,%s,%s,%s)"
    values=(liste)
    print(type)
    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        time.sleep(1)
        print("------------------------------------------")
        time.sleep(1)
        print(f'son eklenen kayıdın id numarası:{cursor.lastrowid}') #son eklenen kaydın id bilgisi lastrowid methodu ile yapılır
        time.sleep(1)
        print("------------------------------------------")
        
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        time.sleep(1)
    ascii_banner = pyfiglet.figlet_format("İşlem Başarılı",font="standard")
    print(ascii_banner)

def kayitSorgulama():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoles123...",
        database="okul"
    )
    cursor=connection.cursor()

    #cursor.execute('Select * From okul') #Tüm kolonları getirir
    cursor.execute('Select KitapIsmi,Sayfa From okul')
    result=cursor.fetchall()  #birden fazla kayıt almak istediğimizde fetchall methodu kullanılır
    """result=cursor.fetchone() #Bulduğu ilk kaydı getirir."""

    for i in result:
        print(f"Kitap ismi:{i[0]} Kitap sayfası:{i[1]}")

#f'Kitap ismi: {i[1]} Kitap sayısı: {i[4]


def Filtreleme():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoles123...",
        database="okul"
    )
    cursor=connection.cursor()

    

    #cursor.execute('Select * From okul Where Id=1') #Where komutu filtreleme işine yarar id si 1 olan kaydı verir
    #cursor.execute('Select * From okul where KitapIsmi="Simyacı"')#isme göre filtreledik
    print("------------------------------------------")
    print("Yazara göre filtreleme yapmak için komutlar aşşağıda görülecekdir")
    time.sleep(1)
    print("------------------------------------------")
    print("George R.R için -->1")
    time.sleep(1)
    print("------------------------------------------")
    print("Mustafa Altınkaynak için -->2")
    time.sleep(1)
    print("------------------------------------------")
    print("Markuz zusak için -->3")
    time.sleep(1)
    print("------------------------------------------")
    print("Tuncel Altınköprü için-->4")
    time.sleep(1)
    print("------------------------------------------")
    print("Maxime Chattam-->5")
    time.sleep(1)
    print("------------------------------------------")
    print("Lev Tolstoy-->6")
    
    
    time.sleep(1)
    print("------------------------------------------")
    girilen=input("Girilen Değer-->")
    print("------------------------------------------")
    if girilen=="1":
        cursor.execute('Select * From okul where Yazar="George R.R."')
        result=cursor.fetchall()
        for i in result:
            print(i)        
    elif girilen=="2":
        cursor.execute('Select * From okul where Yazar="Mustafa Altınkaynak"')
        result=cursor.fetchall()
        for i in result:
            print(i)  
    elif girilen=="3":
        cursor.execute('Select * From okul where Yazar="Markuz Zusak"')
        result=cursor.fetchall()
        for i in result:
            print(i)
    elif girilen=="4":
        cursor.execute('Select * From okul where Yazar="Tuncel Altınköprü"')
        result=cursor.fetchall()
        for i in result:
            print(i)
    elif girilen=="5":
        cursor.execute('Select * From okul where Yazar="Maxime Chattam"')
        result=cursor.fetchall()
        for i in result:
            print(i)

    elif girilen=="6":
        cursor.execute('Select * From okul where Yazar="Lev Tolstoy"')
        result=cursor.fetchall()
        for i in result:
            print(i)



def DataBilgi():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoles123...",
        database="okul"
    )
    cursor=connection.cursor()
    time.sleep(2)
    print("------------------------------------------")
    time.sleep(1)
    print("Data bilgileri seçimleri aşağıda görülecekdir:")
    print("------------------------------------------")
    time.sleep(1)
    print("Veri sayısı için -->1")
    print("------------------------------------------")
    time.sleep(1)
    print("sayfa sayısı ortalaması için -->2")
    print("------------------------------------------")
    time.sleep(1)
    print("Toplam sayfa sayısı için -->3")
    print("------------------------------------------")
    time.sleep(1)
    print("Max sayfa sayısı için -->4")
    print("------------------------------------------")
    time.sleep(1)
    a=input("seçim-->")


    if a=="1":
        cursor.execute('Select COUNT(*) from okul where Sayfa >1')#Tablodaki bütün verilerin sayısını sayar
        result=cursor.fetchall()
        print(result)    
    elif a=="2":
        cursor.execute('Select AVG(Sayfa) from okul ')#sayfa sayısı ortalaması getirir
        result=cursor.fetchall()
        print(result) 
    
    elif a=="3":
        cursor.execute('Select SUM(Sayfa) from okul ') #tÜM KAYITLARI TOPLAR
        result=cursor.fetchall()
        print(result) 

    elif a=="4":
        cursor.execute("select MAX(Sayfa) from okul") #Max değeri verir
        result=cursor.fetchall()
        print(result)
        
     


def Uptade():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoles123...",
        database="okul"
    )
    cursor=connection.cursor()
 
    cursor.execute("Uptdate okul Set KitapIsmi='BLA bla bla' where id=5") #id si 5 olan kaydı bla bla  bla olarak uptade eder
    cursor.execute("Uptade okul Set KitapIsmi='bla bla', Sayfa=1000 where Id=1") #sayfa sayısı 100o olan ve Id si 1 olan satırı günceller
    


def Delete(Id):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoles123...",
        database="okul"
    )
    cursor=connection.cursor()

    
    sql="delete from okul where Id=%s" # girilen Id numaralı Id silinir.
    values=(Id,)
    cursor.execute(sql,values)
    try:
        connection.commit()

        print(f'{cursor.rowcount} tane kayıt silindi')
    except mysql.connector.Error as err:
        print("hata",err)

    finally:
        connection.close()
        ascii_banner = pyfiglet.figlet_format("Silme Başaralı",font="standard")
        print(ascii_banner)
    

    





print("Kayıt etmek için 1 \nkayıt sorgulamak için 2\nFiltreleme için 3\nData bilgiler için 4")
print("Silme işlemi için 5")
a=input("Seçim-->")


liste=[]
while True:
    if a=="1":
        print(f'son eklenen kayıdın id numarası:{cursor.lastrowid}')
        while True:
            Id_ismi=input("id ismi gir")
            print("------------------------------------------")
            KitapIsmi=input("Kayıdı eklenecek Kitabın ismi:")
            print("------------------------------------------")
            time.sleep(1)
            Yazar=input("Kayıdı eklenecek kitabın Yazarı:")
            print("------------------------------------------")
            time.sleep(1)
            Sayfa=int(input("Kayıdı eklenecek kitabın sayfa sayısı:"))
            print("------------------------------------------")
            time.sleep(1)
            Tür=input("Kitabın türünü giriniz:")
            print("------------------------------------------")
            time.sleep(1)
            Durum=input("kitap bittimi (Y/N)")
            print("------------------------------------------")
            liste.append((Id_ismi,KitapIsmi,Yazar,Sayfa,Tür,Durum))


            result=input("Kayıt işlemine devam edilsinmi? (Y/N)----->")
            print("------------------------------------------")

                

                
                
            if result=="n":
                print("------------------------------------------")
                time.sleep(1)
                print("Kayıtlarınız kayıt alanına aktarılıyor ....")
                time.sleep(1)
                print("-------------------------------------------")
                time.sleep(1)
                print(liste)
                time.sleep(1)
                print("-------------------------------------------")
                KayıtEtme(liste)
                break

    elif a=="2":
        kayitSorgulama()
        break
        

    elif a=="3":
        Filtreleme()
        break

    elif a=="4":
        DataBilgi()
        break

    elif a=="5":
        print("------------------------------------------")
        time.sleep(1)
        Id=input("girmek istediğn kaydın Id numarasını giriniz-->")
        print("------------------------------------------")
        time.sleep(1)
        Delete(Id)
        break


    else:
    
        print("Hatalı işlem")


input()
""" FİLTRELEME İŞLEMLERİ İÇİN NOTLAR"""

def Ders_notları():
    cursor.execute('Select * From okul Where KitapIsmi="Game Of Thrones" and Sayfa=1220')
    #yukardaki satırda filtreleme yaparken and bağlacı kullandık 2 koşula göre filtreliyecekdir
    cursor.execute('Select * From okul Where KitapIsmi="Game Of Thrones" or Sayfa=1220')
    #yukarıdaki satırda or=yada koşulu kullanıldı
    cursor.execute('Select * From okul Where KitapIsmi LIKE "%Game%"')
    #Yukarıdakı LİKE kitap isminin içinde game geçen sözcükleri bulur ve filtreler
    cursor.execute('Select * From okul Where KitapIsmi LIKE "Game%"') 
    #Yukarıdaki kod da başı game ile başlayan ifadeleri filtreler başında % kullanmadık




""" ORDER BY LİSTELEME """
def orderBy():
    cursor.execute('Select * From okul Order By name') 
    #nameleri harf sırasına göre listeler
    cursor.execute('Select * From okul Order By name DESC')
    # DESC azalan bi şekilde sıralama yapmamaızı sağlar
     


