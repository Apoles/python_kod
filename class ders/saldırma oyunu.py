# iletişim için skype: ertugrul2727tr
# paketleri dahil ediyoruz
from tkinter import *
from tkinter import messagebox
import sys, sqlite3

# veri tabanı işlemlerini yapıyoruz
con = sqlite3.connect("şampiyonlar.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS winners (kazanan TEXT)")


class Oyuncu:  # sınıfımızı oluşturuyoruz
    def __init__(self, can, enerji, mermi, güç):
        # sınıfa özellikler ekliyoruz
        self.can = can
        self.enerji = enerji
        self.mermi = mermi
        self.güç = güç

    def goster(self):  # sınıftan türeyen nesnesin özelliklerini göstermesi için bir fonksiyon oluşturuyoruz
        print("Can: ", self.can, "Enerji: ", self.enerji, " Mermi: ", self.mermi, " Güç: ", self.güç)


# nesneleri oluşturmak için veri alıyoruz
o1c = int(input("1. Oyuncu can: "))
o1e = int(input("1. Oyuncu enerji: "))
o1m = int(input("1. Oyuncu mermi: "))
o1g = int(input("1. Oyuncu güç: "))
print("==" * 20)
o2c = int(input("2. Oyuncu can: "))
o2e = int(input("2. Oyuncu enerji: "))
o2m = int(input("2. Oyuncu mermi: "))
o2g = int(input("2. Oyuncu güç: "))

# nesneleri oluşturuyoruz
oyuncu1 = Oyuncu(o1c, o1e, o1m, o1g)
oyuncu2 = Oyuncu(o2c, o2e, o2m, o2g)

sıra = "1."  # sayac gibi kullanılan bir sıra değişkeni oluşturuyoruz


def saldır1():  # 1. oyuncu için saldırma fonksiyonu oluşturuyoruz
    global sıra  # sayacımızı içe aktarıyoruz
    if (sıra == "1."):  # sıranın bizde olup olmadığını kontrol edip ona göre işlem yapıyoruz
        oyuncu2.can -= oyuncu1.güç
        oyuncu1.enerji -= 10
        oyuncu1.mermi -= 1
        sıra = "2."  # sıra bizdeyse işlemleri yapıp sırayı 2. oyuncuya veriyoruz
        # burdaki koşullarda enerjilerin veya canların sıfırlanıp sıfırlanmadığını kontrol edip oyunun devam etmesine karar veriyoruz
        if (oyuncu1.can == 0 or oyuncu1.enerji == 0):
            cur.execute("INSERT INTO winners (kazanan) VALUES ('Oyuncu2')")  # veritabanına kazananı ekliyoruz
            con.commit()
            messagebox.showinfo("Bitti", "Kazanannn: Oyuncu2")
            sys.exit()
            con.close()
        if (oyuncu2.can == 0 or oyuncu2.enerji == 0):
            cur.execute("INSERT INTO winners (kazanan) VALUES ('Oyuncu1')")
            con.commit()
            messagebox.showinfo("Bitti", "Kazanannn: Oyuncu1")
            sys.exit()
            con.close()
        print("SIRA 2. OYUNCUDA")  # sıranın rakipde olduğunu belirtiyoruz
    else:
        messagebox.showerror("Hata",
                             "Sıra sende değil!")  # sıra bizde değilse bildirim göndererek sıranın bizde olmadığını söylüyoruz


def saldır2():  # yukardakilerin aynını burdada yapıyoruz
    global sıra
    if (sıra == "2."):
        oyuncu1.can -= oyuncu2.güç
        oyuncu2.enerji -= 10
        oyuncu2.mermi -= 1
        sıra = "1."
        if (oyuncu1.can == 0 or oyuncu1.enerji == 0):
            cur.execute("INSERT INTO winners (kazanan) VALUES ('Oyuncu2')")
            con.commit()
            messagebox.showinfo("Bitti", "Kazanannn: Oyuncu2")
            sys.exit()
            con.close()
        if (oyuncu2.can == 0 or oyuncu2.enerji == 0):
            cur.execute("INSERT INTO winners (kazanan) VALUES ('Oyuncu1')")
            con.commit()
            messagebox.showinfo("Bitti", "Kazanannn: Oyuncu1")
            sys.exit()
            con.close()
        print("SIRA 1. OYUNCUDA")
    else:
        messagebox.showerror("Hata", "Sıra sende değil!")


def pas():  # burda her 2 oyuncu içinde kullanılabilecek bir sıra atlama fonksiyonu oluşturuyoruz
    global sıra
    if (sıra == "1."):
        sıra = "2."
        print("SIRA 2. OYUNCUDA")
        return
    elif (sıra == "2."):
        sıra = "1."
        print("SIRA 1. OYUNCUDA")
        return


# görsel arayüzümüzü oluşturuyoruz
p = Tk()
p.tk_setPalette("white")
l1 = Label(text="Oyuncu 1").grid(row=1, column=1, padx=20, pady=20)
l2 = Label(text="Oyuncu 2").grid(row=1, column=3, padx=20, pady=20)
b1 = Button(text="Göster", command=oyuncu1.goster).grid(row=2, column=1, padx=20, pady=10)
b3 = Button(text="Saldır", command=saldır1).grid(row=4, column=1, padx=20, pady=10)
b4 = Button(text="Göster", command=oyuncu2.goster).grid(row=2, column=3, padx=20, pady=10)
b5 = Button(text="Pas geç", command=pas).grid(row=3, column=2, padx=20, pady=10)
b6 = Button(text="Saldır", command=saldır2).grid(row=4, column=3, padx=20, pady=10)
mainloop()  # arayüzü ekranda tutuyoruz

