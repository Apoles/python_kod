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
