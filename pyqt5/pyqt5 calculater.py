import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow


class Mainform(QMainWindow):
    def __init__(self):

        super(Mainform,self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):

        self.lbl_sayi1=QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("sayi1:")
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1=QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)


        self.lbl_sayi2=QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("sayi2:")
        self.lbl_sayi2.move(50,80)

        
        self.txt_sayi2=QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.buton1=QtWidgets.QPushButton(self)
        self.buton1.setText('Topla')
        self.buton1.move(150,130)
        self.buton1.clicked.connect(self.Hesap)


        self.buton2=QtWidgets.QPushButton(self)
        self.buton2.setText('Çıkar')
        self.buton2.move(150,180)
        self.buton2.clicked.connect(self.Hesap)

        
        self.buton3=QtWidgets.QPushButton(self)
        self.buton3.setText('Çarp')
        self.buton3.move(150,230)
        self.buton3.clicked.connect(self.Hesap)

        self.buton4=QtWidgets.QPushButton(self)
        self.buton4.setText('böl')
        self.buton4.move(150,280)
        self.buton4.clicked.connect(self.Hesap)


        self.sonuc=QtWidgets.QLabel(self)
        self.sonuc.setText("Sonuc")
        self.sonuc.move(150,350)
    """
    def Topla(self):
        print(int(self.txt_sayi1.text())+int(self.txt_sayi2.text()))
        
    def cikar(self):
        print(int(self.txt_sayi1.text())-int(self.txt_sayi2.text()))        

    def bol(self):
        print(int(self.txt_sayi1.text())/int(self.txt_sayi2.text()))
    def carp(self):
        print(int(self.txt_sayi1.text())*int(self.txt_sayi2.text()))
    """
    
    # TEK TEK HESAPLAMAK YERİNE TEK BİR FONKSİYONDA HESAPLAYALIM

    def Hesap(self):
        sender=self.sender()
        if sender.text()=="Topla":
            result=0
            result=int(self.txt_sayi1.text())+int(self.txt_sayi2.text())
            print(result)

        elif sender.text()=="Çıkar":
            print(int(self.txt_sayi1.text())-int(self.txt_sayi2.text()))
        elif sender.text()=="Çarp":
            print(int(self.txt_sayi1.text())*int(self.txt_sayi2.text()))
        elif sender.text()=="böl":
            try:
                print(int(self.txt_sayi1.text())/int(self.txt_sayi2.text()))
            except ZeroDivisionError:
                print("Sayısı 0 a bölemezsin")
def app():
    app=QApplication(sys.argv)
    win=Mainform()
    win.show()
    sys.exit(app.exec_())


app()



