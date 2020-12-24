import mysql.connector


mydb=mysql.connector.connect(  #mysql e bağlanmamız gerekiyor

    host="localhost",  # host bilgisi verildi İNTERNETTEN SERVER ALDIYSAK 102.168.1.2 TARZI İP  ADRES YAZILR
    user="root",
    password="Apoles123...",
    database="mydatabase"  #kullanmak istediğim databesi yazıyorum birden fazlda data base olanbilir..

)


mycursor=mydb.cursor()  #cursor oluşturduk

#mycursor.execute("CREATE DATABASE mydatabase") # Boş bir data base oluştuduk

"""mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
   """   #DATA BASELERİMİZİ GÖSTERDİK

mycursor.execute("CREATE TABLE customers(name VARCHAR(255),adress VARCHAR(255))") #DATA BASE OLUŞTURDUK VE NAME ADRESS KOLONLARI OLUŞTURDUK





