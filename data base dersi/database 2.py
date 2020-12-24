import mysql.connector
import time
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Gumuş"+" " + "Sulalesi Data Base",font="standard")
print(ascii_banner)

print("Programımıza hoş geldiniz...")
print("-----------------------------")

def insertProduct(İsim,Soyİsim,Yas):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoles123...",
        database="Apoles"
    )

    cursor=connection.cursor()


    sql="INSERT INTO Apoles (İsim,Soyİsim,Yas) VALUES(%s,%s,%s)"
    values=(İsim,Soyİsim,Yas)
    cursor.execute(sql,values)
    

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kayıdın id numarası:{cursor.lastrowid}') #son eklenen kaydın id bilgisi lastrowid methodu ile yapılır
    
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("data base e bağlandı ve oluştutuldu")




def insertProducts(liste):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoles123...",
        database="Apoles"
    )

    cursor=connection.cursor()


    sql="INSERT INTO Apoles (İsim,Soyİsim,Yas) VALUES(%s,%s,%s)"
    values=(liste)
    cursor.executemany(sql,values) #çoklu kayıt ekleme executemany
    

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

    İsim=input("Kayıdı eklenecek kişisinin İsmini giriniz:")
    Soyİsim=input("Kayıdı eklenecek kişisinin soyismini giriniz:")
    Yas=int(input("Kayıdı eklenecek kişisinin Yaşını giriniz:"))

    liste.append((İsim,Soyİsim,Yas))


    result=input("Kayıt işlemine devam edilsinmi? (Y/N)----->")
    
    
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
        insertProducts(liste)
        break

input()
#insertProduct(İsim,Soyİsim,Yas)

