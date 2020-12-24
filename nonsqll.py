import pymongo
from bson.objectid import ObjectId
import time
import argparse

print(dir(argparse))
baglantı=pymongo.MongoClient("mongodb://localhost:27017") #Servera bağladık bize verilen port üzerinden. 
mydb=baglantı["muzmobref"] #collection slara bağlantı gerçekleştiriyoruz. Eğer name adında bir dokument  yoksa ve collections hali hazırda var ise muzmobref adlı dokument oluşturulur.
mycollections=mydb["Yatak_odası"] 



print(baglantı.list_database_names())
print(mydb.list_collection_names())

def  tekli_collections_ekleme():
    Name={"Name":"Zen Yatak Odası","fiyat":20758}
    result=mycollections.insert_one(Name) #Yeni collections ekledık
    print(result)
    print(type(result))
    print(result.inserted_id) #Program her bir collectiona id numarasını otomatik atar inserted_id ise bu id nmaralarını gösterir


def coklu_collections_ekleme():
    Yatak_Odası=[
        {"_id":1,"Name":"Zen Yatak Odası(Siyah)","Fiyat":17756,"Parçalar":["Zen Dolap(170 cm)= 5600 TL","ZEN DOLAP SAĞ TEK KAPILI (AÇIK GRİ)= 2470 TL","ZEN DOLAP SOL TEK KAPILI (AÇIK GRİ)= 2420 TL","ZEN KARYOLA 160*200 (AÇIK GRİ)= 3865 TL","ZEN KOMODİN (AÇIK GRİ)= 1455TL","ZEN ŞİFONYER+ AYNA (AÇIK GRİ)= 4150 TL","ZEN KOMODİN PANO (AÇIK GRİ)= 1580 TL"],
        "Teknik Özellikeri":[	
        "Takım içeriği:     Dolap,karyola: , komodin ve şifonyer ve şifonyer aynasından oluşmaktadır.",
        "Karyola:	        Karyola başlığı ve yanları sünger üzerine kapitone kumaş döşeme kullanılmıştır. 180'lik olarak standart ölçüde üretilmektedir.",
        "Komodin:	        Gövde ve çekmece kapakları boyalı MDFdir. Kapaklarda gizli kulp özelliği bulunmaktadır.Ayakları metalden üretilmiştir.",
        "6 kapılı dolap:	Gövde ve sağ,sol kapakları boyalı MDFden üretilmiş olup orta kapaklarda füme reflekte cam kullanılmıştır.",
        "Şifonyer:	        Gövde ve çekmece kapakları boyalı MDFdir.Çekmece kulp ve ayak detaylarında metal malzeme kullanılmıştır.",
        "Şifonyer ayna: 	Boyalı MDF çerçeveden üretilmiştir.",
        "Bakım:	            Hafif nemli microfiber bezle silinip temizlik bakımı yapılabilir."],
        "Modül Ölçüleri:":[
        "Modül	    Genişlik	Derinlik	Yükseklik",
        "KARYOLA	180 cm	235 cm	115 cm",
        "KOMODİN	66 cm	48 cm	43 cm",
        "6 KAPILI DOLAP	272 cm	64 cm	227 cm",
        "ŞİFONYER	131 cm	48 cm	86 cm",
        "ŞİFONYER AYNA	80 cm	3 cm	95 cm"
        ]
        
        
        
        },
        {"_id":2,"Name":"Senfoni Yatak Odası(Beyaz)","Fiyat":17362,"Parcalar":["SENFONİ DOLAP 6 KAPILI (METALİK SİYAH)= 7720 TL","SENFONİ KARYOLA 160*200 (PRL BEYAZ)= 4030 tl","SENFONİ KOMODİN (PRLK BEYAZ)= 897 TL","SENFONİ KOMODİN METAL AYAK (NİKELAJ)= 672 TL","SENFONİ ŞİFONYER (PRLK BEYAZ)= 2634 TL","SENFONİ GENEL AYAK (ŞİFONYER-KONSOL-TV) (NİKELAJ)= 860 TL","SENFONİ ŞİFONYER AYNA (PRLK BEYAZ)= 910 TL","SENFONİ KOMODİN METAL AYAK (ALTIN)= 815 TL","SENFONİ GENEL AYAK (ŞİFONYER-KONSOL-TV) (ALTIN)= 1050 TL"],
        "Teknik Özellikleri":[
        "Takım içeriği:	    Dolap,karyola , komodin ve şifonyer ve şifonyer aynasından oluşmaktadır.",
        "Komodin:       	Gövde ve çekmece kapakları boyalı MDFdir. Kapaklarda gizli kulp özelliği bulunmaktadır.Ayakları metalden üretilmiştir.",
        "6 kapılı dolap:	Gövde ve sağ,sol kapakları boyalı MDFden üretilmiş olup orta kapaklarda füme reflekte cam kullanılmıştır.",
        "Şifonyer:	        Gövde ve çekmece kapakları boyalı MDFdir.Çekmece kulp ve ayak detaylarında metal malzeme kullanılmıştır.",
        "Şifonyer ayna:	    Boyalı MDF çerçeveden üretilmiştir.",
        "Bakım:	            Hafif nemli microfiber bezle silinip temizlik bakımı yapılabilir."

        ],
        "Modul Ölcüleri":[
        "Modül	    Genişlik	Derinlik	Yükseklik",
        "KARYOLA	180 cm	235 cm	115 cm",
        "KOMODİN	66 cm	48 cm	43 cm",
        "6 KAPILI DOLAP	272 cm	64 cm	227 cm",
        "ŞİFONYER	131 cm	48 cm	86 cm",
        "ŞİFONYER AYNA	80 cm	3 cm	95 cm"
        ]
        
        
        
        },
        {"_id":3,"Name":"Zen Yatak Odası(Ekru)","Fiyat":20758,"Parcalar":["ZEN DOLAP (170 CM) (MTLK EKRU-SEDEF PRLK)= 5660 TL","ZEN DOLAP SAĞ TEK KAPILI (M.EKRU-S.PRLK)= 2470 TL","ZEN DOLAP SOL TEK KAPILI (M.EKRU-S.PRLK)= 2420 TL","ZEN KARYOLA 160*200 (M.EKRU S.PARLAK)= 3865 TL","ZEN KOMODİN (M.EKRU-SEDEF PRLK)(2 ADET)= 1455 TL","ZEN ŞİFONYER+ AYNA (M.EKRU-SEDEF PRLK)= 4150 TL","ZEN KOMODİN PANO (M.EKRU-SEDEF PRLK)= 1590 TL"]},
        {"_id":4,"Name":"Enzio Yatak Odası(Gri)","Fiyat":16803,"Parcalar":["ENZİO DOLAP (KOYU GRİ-BOHÇA)= 7690 TL","ENZİO KARYOLA 160*200 (KOYU GRİ-BOHÇA)= 3135 TL","ENZİO KOMODİN (KOYU GRİ-BOHÇA)= 1222 TL","ENZİO KOMODİN PANO (KOYU GRİ-BOHÇA)= 1230 TL","ENZİO ŞİFONYER (KOYU GRİ-BOHÇA)= 2985 TL","ENZİO ŞİFONYER AYNA (KOYU GRİ-BOHÇA)= 1385 TL"]},
        {"_id":5,"Name":"Enzio Yatak Odası(Ekru)","Fiyat":18803,"Parcalar":["ENZİO DOLAP (BEYAZ)= 7690 TL","ENZİO KARYOLA 160*200 (BEYAZ)= 3135 TL","ENZİO KOMODİN (BEYAZ)= 1222 TL","ENZİO KOMODİN PANO (BEYAZ)=1230 TL","ENZİO ŞİFONYER (BEYAZ) TL","ENZİO ŞİFONYER AYNA (BEYAZ)= 1385 TL"],
        "Teknik Özellikleri":[
            "Takım İçeriği:   Dolap,karyola , komodin ve şifonyerden oluşmaktadır.",
            "Karyola:         Karyola başlığı ve yan tahta ayak ucunda sünger üzerine kumaş döşeme kullanılmıştır. 160lık ve 180lik olarak standart 2 ölçüde üretilmektedir",
            "Komodin:         Gövde glossmax MDF,çekmece kapakları boyalı MDFdir. Kapaklarda metal kulp kullanılmıştır.",
            "Komodin pano:	  Karyola başlığı sağında ve solunda demonte olarak bulumaktadır.Glossmax MDFdir.Dokunmatik metal aplik detayı bulunmaktadır",
            "Dolap:	          Sürgülü kapaktır.Kapaklar üzerinde füme ayna detayı kullanılmıştır.",
            "Şifonyer	      İki kapak bir çekmece ve metal aynadan oluşmaktadır.Gövde glossmax, çekmece kapakları boyalı MDFdir.Metal açılı ayak detayı kullanılmıştır",
            "Şifonyer ayna:	  Metalden üretilmiştir.",
            "Bakım:	          Hafif nemli microfiber bezle silinip temizlik bakımı yapılabilir."         
        ],
        "Modül Ölçüleri":[
            "Modül	            Genişlik	    Derinlik	       Yükseklik",
            "KOMODİN	        67 cm 	         48 cm	           37 cm",
            "KOMODİN PANO	     70 cm	         8 cm	           107 cm",
            "DOLAP	            260 cm	         69 cm	           223 cm",
            "ŞİFONYER	        140 cm	         51 cm	           84 cm",
            "ŞİFONYER AYNA	     94 cm	         3 cm	           100 cm",
        ]
        
        
        },
        {"_id":6,"Name":"Diana Yatak Odası(Ceviz)","Fiyat":18414},
        {"_id":7,"Name":"Diana Yatak Odası(vizon)","Fiyat":17314},
        {"_id":8,"Name":"Solo Yatak Odası(Ceviz)","Fiyat":14014},
        {"_id":9,"Name":"Solo Yatak Odası(Ekru)","Fiyat":14026},
        {"_id":10,"Name":"Adriana Yatak Odası","Fiyat":12264},
        {"_id":11,"Name":"Lorenzo Yatak Odası","Fiyat":13823}
        ]
    
    
    result=mycollections.insert_many(Yatak_Odası)
    print(result.inserted_ids)

#coklu_collections_ekleme()
def kayıt_secme():
    """mycollections.find_one()  #Tekli kayır alma"""
    result=mycollections.find() #Bütün kayıtları getirecek
    """for i in result:
        print(i)"""

    result=mycollections.find({},{"_id":0,"Name":1,"Fiyat":1})  #İlk süslü parantez where komutunda denk gelir.#İkinci parametrede ise hangi kolonların gözükmesi gerekdiğini söylüyruz
    for i in result:
        print(i)
    


   



def Kayıt_filtreleme():
    filtre={"Name":"Senfoni Yatak Odası(Siyah)"}  #Arattığımız isim  ile  filtreleme
    result=mycollections.find(filtre)
    for i in result:
        print("1",i)
    print("============================")
    result2=mycollections.find_one({"_id":1}) # id numarasına göre filtreledik
    print(result2)
    """result3=mycollections.find_one({"_id": ObjectId("5d6a7jsad123öa2sp213cqs")}) # from bson.objectid import ObjectId bize string yazabilme şansı tanıdını bunu importlamasak yukarıdaki ifade de hata alıcakdık
    print("=============================")
    print(result3)
"""
    print("*****************************************************************")
    result4=mycollections.find({
        "Name":{
            "$in":["Senfoni Yatak Odası(Siyah)","Senfoni Yatak Odası(Beyaz)"] #Herhangi bir isim Name alandı mevcut ise bize result gelicekdir
        }
    })
    for i in result4:
        print(i)

    result5=mycollections.find({
        "Fiyat": {
            "$gt":15000    #Fiyatı 15000 den büyük olan kayıtları aldı
        }
    },{"Name":1,"Fiyat":1})
    for i in result5:
        print("*"*50)
        print(i)

    
    #    "$gte" -----> Büyük yada Eşit olan
    #    "$eq"  -----> Eşit olan
    #    "$lt"  -----> Küçük olan
    #    "$lte" -----> Küçük yada eşit olan
    #   MANTIK OPERATÖRLERİDE AYNI ŞEKİL KULLANILABİLİR AND OR NOT GİBİ
    result6=mycollections.find({
        "Name":{"$reqex":"^S"}  #Reguler exprecion yapılımı
        #Yukardıaki kod S ile başlayan sorguları bize döndürür
    })


def kayıt_sıralama():
    result=mycollections.find({},{"_id":0,"Name":1,"Fiyat":1}).sort("Fiyat",-1)  # Name e göre sıralama yapıyor 1 ise artan şekilde sıralama yaptıgımızı gösteriyor
    for i in result:
        print(i)


def guncelleme():
    mycollections.update_many(
        {"Name":"Senfoni Yatak Odası(Siyah)"},
        {'$set':{
            'Name':"Senfoni Yatak Odası(Siyahh)"
        }}
        )            #YUKARDAKİ KODDA NAME E GÖRE BİR DÜZENLEME YAPTIL $set: cümlesiyle güncelleme yapıldı.
print("*"*50)

def delete():
    #delete_one ve delete_many methodları kullanılır
    mycollections.delete_many({"Name":"Senfoni yatak odası"}) # silme işlemi yapıldı
