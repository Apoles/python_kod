import os
import time
from datetime import datetime
import pyfiglet
import colorama
import speech_recognition as sr
import webbrowser
from gtts import gTTS
from playsound import playsound
import random
from colorama import Fore, Back, Style
from math import *
from tkinter import *



colorama.init()


def help():
    print(Fore.LIGHTBLACK_EX)
    print("==============================")
    time.sleep(0.1)
    print("Bash Apoles version 1.1.1 ")
    time.sleep(0.1)
    print("welcome bash Apoles")
    time.sleep(0.1)
    print("Komutlar Aşşağıda gözükecekdir")
    time.sleep(0.1)
    print("===============================")
    time.sleep(0.1)
    print("")
    print("Information for Apoles bash")
    time.sleep(3)
    print("===============================")
    
    print(Fore.BLUE,"""
These shell commands are defined internally.  Type `help' to see this list.
Type `help name' to find out more about the function `name'.
Use `info bash' to find out more about the shell in general.
Use `man -k' or `info' to find out more about commands not in this list.

A star (*) next to a name means that the command is disabled.""")
    print("===============================")
    print(Fore.YELLOW,"APOELS BASH COMMAND:")
    time.sleep(2)
    print("")
    print("""
        cd                       ---   ---  ---              Dizin değiştirmek için kullanılır.
        --version                ---   ---  ---              Sürüm bilgisi.
        ls                       ---   ---  ---              Dizin içine girer.
        pwd                      ---   ---  ---              Hangi dizinde oldugunu gösteririr.
        mkdir                    ---   ---  ---              Dizin oluşturmamızı sağlar.
        rename                   ---   ---  ---              Dizin veya dosya ismini değştirir.
        rmdir                    ---   ---  ---              Boş dizini siler.
        remove                   ---   ---  ---              Dizin yada dosya siler.
        du                       ---   ---  ---              Dosya boyutlarını verir.   
        cat                      ---   ---  ---              Dosya okuma işlemi.
        start                    ---   ---  ---              Programı başlatır.
        top                      ---   ---  ---              Görev Yöneticisini çalıştırır.
        date time                ---   ---  ---              Zaman bilgisini verir.
        calculator -i            ---   ---  ---              Apoles hesap makinesi.
        Döviz                    ---   ---  ---              Para birimleri çevirir.
        
    """)
    print("===============================")
    print("")
    print("")


def ls():
    print(Fore.YELLOW)
    #ls komutu fonksiyonu
    dizin=os.getcwd()
    dir_list=os.listdir(dizin)
    """for s in enumerate(dir_list):
	    print()"""
    
    dir_list=list(dir_list)
    
    for s in enumerate(dir_list):
        print(s)
    



while(1):
    #mydizin=print(os.getcwd())
    print(Fore.RED)
    
    a=input(f'kali@Apoles:~ {os.getcwd()}$'+" ")  #dizin gösterimi
    
    if a=="--version": #windows versiyonu
        print(Fore.YELLOW)
        print(os.name)

    elif a=="ls":  #linux ls komutu dizin  bilgisi alma
        ls()

    elif a== "cd" or a=="cd " :  #Dizin değiştirme   
        #cd()
        print(Fore.YELLOW)
        try:
            b=input("cd"+" ") #dizin yolu girilir
            os.chdir(fr"C:\Users\DELL\{b}") # Girilen dizin yolu oldugumuz dizine eklenir ve istenilen dizine girilir.
        except:
            print("No such file or directory")

    elif a=="pwd": #Hangi dizinde olduğumuzu gösterir
        print(Fore.YELLOW)
        print(os.getcwd()) 

    elif a=="help":
        help()

    elif a=="":
        pass
    elif a=="mkdir": #dizin oluşturma
        print(Fore.YELLOW)
        try:
            dizinolusturma=input("mkdir"+" ") # Oluşturacagımız dizin girilir

            os.mkdir(dizinolusturma)    # os.mkdir ile dizin oluşturma gerçekleştirilir
        except FileExistsError:
            print("=========================================================")
            time.sleep(0.5)
            print("Dizin oluşturma hatalı... Varolan bir dizin oluşturulamaz")
            time.sleep(0.5)
            print("=========================================================")
            time.sleep(0.1)
            
    elif a=='rename': #Dizin ismi değiştirme
        print(Fore.YELLOW)
        try:
            change_Dosya=input("Değişcek dizin veya dosya: ")
            dos=input("Yeni isim:")
            os.rename(change_Dosya,dos)
        except FileNotFoundError:

            print("------------------------------------")
            print("")
            time.sleep(0.5)
            print(" Sistem belirtilen yolu bulamıyor...")
            print(" ")
            time.sleep(0.5)
            print("------------------------------------")
            time.sleep(0.5)

    elif a=="rmdir": #Boş dizin silme
        print(Fore.YELLOW)
        try:
            filee=input()
            os.rmdir(filee)
        except OSError:
            print(" Bu komut sadece boş dizinler için geçerlidir...")
    elif a=="remove": # Dizin silme
        try:
            filee=input()
            os.remove(filee)
        except PermissionError:
            print(" Bu işlemi yapmak için admin yetkisi gerekir...")
         
        except FileNotFoundError:
            print(" Belirtilen dosya yolu geçersiz...")
           
    elif a=="du": #Dizin bilgilerini verir
        print(Fore.YELLOW)
        try:
            stat=input()
            a=os.stat(stat)
           
            print(a)
        except FileNotFoundError:
            print("Öyle bir dosya yok...")

    elif a=="cat": #Verilen dosyayı okur
        print(Fore.BLUE)
        value=input("-->")
        try:
            with open(f'{value}', 'r') as file: #Dosya açma işlemi
                print(file.read()) #  Dosya okuma işlemi
        except PermissionError:
            print(Fore.WHITE)
            print("Dosya okunamıyor...")
        except FileNotFoundError:
            print(Fore.WHITE)
            print("")
            print("Öyle bir dosya yok...")
        except UnicodeDecodeError:
            print("Dosya okunamayacak kadar büyük. Lütfen dosyayı bizzat açmayı deneyiniz...")

    elif a=="start": # Dosya açma işlemi
        print(Fore.BLUE)
        try:
            dosya=input("-->")
            yol=os.getcwd() #şuan oldugumuz dinizi değişkene atıyoruz
            b=f'{yol}\{dosya}' #açmak istefiğimiz dosyası yazıyoruz ve dizinleri birleştirioyurz
            print(b)
            os.startfile(b)
        except FileNotFoundError:
            print("Sistem belirtilen dosyası bulamıyor...")
    elif a=="voice asistan":
        print(Fore.YELLOW)
       
        print("""
        ______________________________________________________________________________
        |                                                                              |
        |                          3Kom SuperHack II Logon                             |
        |______________________________________________________________________________|
        |                                                                              |
        |                                                                              |
        |                                                                              |
        |                 User Name:          [   Apoles      ]                        |
        |                                                                              |
        |                 Password:           [   Gümüş       ]                        |
        |                                                                              |
        |                                                                              |
        |                                                                              |
        |                                   [ OK ]                                     |
        |______________________________________________________________________________|
        |                                                                              |
        |                                                       https://Apoles.com     |
        |______________________________________________________________________________|
        """)



        r=sr.Recognizer()

        def ses_kaydı(ask=False):
            with sr.Microphone() as source:
                if ask:
                    speak(ask)
                audio=r.listen(source) 
                voice=''
                try:
                    voice=r.recognize_google(audio,language="tr-TR ")    
                except sr.UnknownValueError:
                    print("============================")
                    time.sleep(0.5)
                    print("VOİCE DONT GET UNDERSTAND ")
                except sr.RequestError:
                    print("SYSTEM FOUNT ERROR")
                return voice

        def dönüş(voice):
            if 'nasılsın' in voice:
                speak("I am good how you doin?")
            if 'saat kaç' in voice:
                #speak(datetime.datetime.now())
                speak(datetime.now().strftime('%H:%M:%S:'))
            if 'arama yap' in voice:
                search=ses_kaydı("what do you want to search")
                url='https://google.com/search?q='+search
                webbrowser.get().open(url)
                speak("what I found for "+search)
            if 'tamamdır' in voice:
                speak("See you later")
                exit()
            if ' mal insanı kimdir' in voice:
                speak("Abdussametdir")
            
        def speak(string):
            tts=gTTS(string)#,lang='tr')
            rand=random.randint(1,10000) 
            file='audio-'+str(rand)+'.mp3'
            tts.save(file)
            playsound(file)
            os.remove(file)


        speak("May I help you?")
        time.sleep(1)
        while 1:
            voice=ses_kaydı()
            print("============================")
            time.sleep(0.5)
            print(voice)
            time.sleep(0.5)
            print("============================")
            dönüş(voice)
            a=input("-->")
            if a=="exit":
                break
            elif a=="keep":
                continue

 
    elif a=="top": #Görev yöneticisini açar
        os.startfile("C:\Windows\system32\Taskmgr.exe")

    elif a=="date time": #Tarih bilgisini verir
        print(Fore.MAGENTA)
        date=datetime.now()
        tarih=datetime.ctime(date)
        print(tarih)
    elif a=="hello world":
        result = pyfiglet.figlet_format("HELLO WORLD") 
        print(result)
    elif a=="calculator -i":
        from math import *
        from tkinter import *

        def hesapla():
            veri = kutu.get()
            veri = str(veri)
            if veri == "":
                sonuc.config(text = "Lütfen boş bırakmayın.")
            else:
                isle = "global sonuc2;sonuc2 ="+veri
                exec(isle)
                print(isle,"\n",sonuc2)
                sonuc.config(text = str(sonuc2))

        anapencere = Tk()
        anapencere.geometry("800x600+100+100")
        anapencere.title("Hesap Mak. V0.1 Beta")

        sonuc = Label(anapencere)
        sonuc.config(text = "Henüz işlem yapılmadı\n", font = "bold 18",fg = "blue")
        sonuc.pack()

        kutu = Entry(anapencere)
        kutu.pack()

        buton = Button(anapencere)
        buton.config(text = "Hesapla!",command = hesapla)
        buton.pack()

        mainloop() 

    #elif a=="calculator -a":

    elif a=="Döviz":
        import Doviz
        print(Fore.WHITE)
        try:
            Doviz.Doviz()
        except KeyError:
            print(Fore.YELLOW)
            print("Girdiğiniz para birimi hatalı...")
            print("Para birimleri için help -i yazınz.")
        except ValueError:
            print("Girdiğiniz Para miktarı bir sayı olmalıdır...")

    else: 
        print("")
        print(Fore.GREEN)
        print("bash: sd: command not found")

    
        

