import sys
from PyQt5 import QtWidgets
from Aktivite import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()


        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)

        self.UI.Film.stateChanged.connect(self.show_state) # Eğet film butnu tıklanıp seçilirse çalışacak olan script

        self.UI.Spor.stateChanged.connect(self.show_state)

        self.UI.Yemek.stateChanged.connect(self.show_state)

        self.UI.Kitap.stateChanged.connect(self.show_state)


        self.UI.pushButton.clicked.connect(self.kontrol)

    def show_state(self,value):
        """
        print(value)
        print(self.UI.Film.isChecked())  # film butoonu seçilirse true ifadesi döndüürür
        print(self.UI.Film.text())  # Seçildiğinde text bilgisi geliyor.
        """

        cb=self.sender()  #Hangi check box ın çalıştığı bilgisini verir.
        #print(cb) #ilgili adres bilgisi
        print(cb.text()) #text bilgiisi

    def kontrol(self):
        result=''  # label a aktarmak için oluşturdugumuz boş bir string
        items=self.UI.groupBox.findChildren(QtWidgets.QCheckBox)  #dizayn uygulamasında centralwidget olan kısmı ve onun alt elemanlarını seçiyoruz ve findchildren metodu ile de qcheckbox ları seçiyoruz
        print(items)
        
        for i in items:
            

            if i.isChecked():
                """
                print("=======================")
                print(i.text())
                print(i.isChecked())
                """

                result+=i.text()+'\n'

        self.UI.lbl.setText("Seçilenler:\n"+result)



def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())


app()



