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

    sql="INSERT INTO okul(KitapIsmi,Yazar,Sayfa,Tür,Durum) VALUES(%s,%s,%s,%s,%s)"
    values=(liste)
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
        print("data base e bağlandı ve oluştutuldu")
        print("------------------------------------------")




liste=[]
while True:
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
    Tür=input("Kitabın türünü giriniz")
    print("------------------------------------------")
    time.sleep(1)
    Durum=input("kitap bittimi (Y/N)")
    print("------------------------------------------")
    liste.append((KitapIsmi,Yazar,Sayfa,Tür,Durum))


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



input()