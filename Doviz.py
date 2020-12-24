import requests
import time



def Doviz():
    
    print("Para birimlerin kısaltımı aşşağıdaki gibidir")
    print("")
    print("")
    time.sleep(1)

    print(f"""
        CAD     ------------------------------>  Kanada
        HKD     ------------------------------>  Hong Kong Doları
        ISK     ------------------------------>  İzlanda Kronu
        PHP     ------------------------------>  Filipin pesosu
        DKK     ------------------------------>  Danimarka kronu
        HUF     ------------------------------>  Macar forinti
        CZK     ------------------------------>  Çek korunası  
        AUD     ------------------------------>  Avusturalya doları
        RON     ------------------------------>  Rumen Leyi
        SEK     ------------------------------>  İsveç Kronu
        IDR     ------------------------------>  Endonezya Rupisi 
        BRL     ------------------------------>  Brezilya Reali
        RUB     ------------------------------>  Rus rublesi 
        HRK     ------------------------------>  Hırvatistan Kunası
        JPY     ------------------------------>  Japon Yeni
        THB     ------------------------------>  Tayland Bahtı      
        CHF     ------------------------------>  İsviçre Frangı       
        SGD     ------------------------------>  Singapur Doları      
        PLN     ------------------------------>  Polanya Zilotisi      
        TRY     ------------------------------>  Türk lirası       
        CNY     ------------------------------>  Çin yuanı      
        NOK     ------------------------------>  Norceç Kronu      
        NZD     ------------------------------>  Yeni zelanda Doları     
        ZAR     ------------------------------>  Güney afrika     
        USD     ------------------------------>  ABD Doları     
        KRW     ------------------------------>  Güney kore Wonu     
        MRY     ------------------------------>  Malezya Ringiti    
        EUR     ------------------------------>  Euro    
        MXN     ------------------------------>  Mexica Pesosu    
        ILS     ------------------------------>  Yeni israil Şekeli
        """)
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
        

    
    url = 'https://api.exchangeratesapi.io/latest?base='
    birinci = input("(+) Dönüştürülecek Döviz birimi (example=TRY) --> ")
    ikinci = input("(+) Hangi birime dönüşecek (example TRY-->USD  (USD)-->  ")
    miktar = float(input("Miktar: "))

    response = requests.get(url + birinci)
    #print(response)
    json_verisi = response.json()
    print(float(json_verisi["rates"][ikinci]) * miktar)
