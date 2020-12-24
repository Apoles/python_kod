import sys
from PyQt5 import QtWidgets
from RadioButonn import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)

        self.UI.Turkiye_buton.setChecked(True) # Varsayılan olarak seçili hale geliyor

        self.UI.Turkiye_buton.toggled.connect(self.on_Clicked_Ulke) #Radio buton için toggled kullandık
        self.UI.Azerbayca_Buton.toggled.connect(self.on_Clicked_Ulke)
        self.UI.Usa_Buton.toggled.connect(self.on_Clicked_Ulke)
        self.UI.Ingiltere_Buton.toggled.connect(self.on_Clicked_Ulke)

        self.UI.Ilk_Okul_Buton.toggled.connect(self.on_Clicked_Egitim)
        self.UI.Orta_Okul_Buton.toggled.connect(self.on_Clicked_Egitim)
        self.UI.Lise_Buton.toggled.connect(self.on_Clicked_Egitim)
        self.UI.Universte_Buton.toggled.connect(self.on_Clicked_Egitim)


        self.UI.Ulke_Secimi_buton.clicked.connect(self.get_Selected_Ulke)
        self.UI.Eitim_Secimi_Buton.clicked.connect(self.get_Selected_Egitim)



    def on_Clicked_Ulke(self):
        radio_buton=self.sender()
        if radio_buton.isChecked():
            print("Seçilen radyo..."+radio_buton.text())
    
    def on_Clicked_Egitim(self):
        radio_buton=self.sender()
        if radio_buton.isChecked():
            print("Seçilen eğitim..."+radio_buton.text())


    def get_Selected_Ulke(self):
        items=self.UI.groupBox_Ulke.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if i.isChecked():
                self.UI.lbl_ulke.setText("SeçilenÜlke: "+i.text())

    def get_Selected_Egitim(self):
        items=self.UI.groupBox_Egitim.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if i.isChecked():
                self.UI.lbl_egitim.setText("Seçilen eğitim:"+i.text())




def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()