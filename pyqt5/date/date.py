import sys
from PyQt5 import QtWidgets
from datee import Ui_MainWindow
from PyQt5.QtCore import QDate,QTime,QDateTime # zamanla alakı sınıfları importladık

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)

        self.UI.pushButton.clicked.connect(self.hesapla)


    def hesapla(self):
        start=self.UI.dateEdit.date()  # Seçilen date widget ın değerini veriyyor
        end=self.UI.dateEdit_2.date()  # Seçilen date widget ın değerini veriyyor
        print(start,end)

        print('Days in month:{0}'.format(start.daysInMonth()))  #ay içersinde ki gün sayısı PYTHON IN KEDİ SAYFASINDAN DATE DATE TİME İLE DÖKÜMANLARDA AYRINTILARI VERİLMİŞTİR

        print("Toplam iki tarih arası gün sayısı {0} ".format(start.daysTo(end)))

        now =QDate.currentDate() # şimdiki zamanı verir
        
       

def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()