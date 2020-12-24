import sys
from PyQt5 import QtWidgets
from comboboxx import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)
        """
        self.UI.comboBox.addItem("Ankara")  #combox a eleman yükler.
        self.UI.comboBox.addItem("Istanbul")
        self.UI.comboBox.addItem("Bursa") 
        self.UI.comboBox.addItem("Inegol")
        self.UI.comboBox.addItem("Konya")"""
        """
        combo=self.UI.comboBox
        combo.addItem("Ankara")
        combo.addItem("Istanbul")
        combo.addItem("Bursa")
        combo.addItem("Inegol")
        combo.addItem("Konya")
        """
        self.UI.Get_Item.clicked.connect(self.load_Items)

        self.UI.Load_Items.clicked.connect(self.get_Items)

        self.UI.comboBox.currentIndexChanged.connect(self.selected_Changed_Index) #index numarası getirir her seçtiğimizde index numarasını getirexekdir.
        self.UI.comboBox.currentIndexChanged[str].connect(self.selected_Changed_Text) #Text bilgisi gelcekdir str eklenmezse oto ındex bilgisi verir

        self.UI.clear_Item.clicked.connect(self.clear_Item)


    def load_Items(self):
        sehirler=(["Kocaeli","Artvin","Izmir","Ankara","Istanbul","Inegol","Bursa","Konya"])  #Çoklu item ekleme
        self.UI.comboBox.addItems(sehirler)


    def get_Items(self):
        print(self.UI.comboBox.currentText()) #ELEMANIN İSMİ GELİR currenttext() direk ismi getirir 
        print(self.UI.comboBox.currentIndex()) #İndex bilgisi gelir
        
        count=self.UI.comboBox.count() # Eleman sayısını verir

        for index in range(count): #For döngüsünün ne kadar döneceğini range ile sağlıyoruz 
            print(self.UI.comboBox.itemText(index)) #verdiğimiz index bilgisinin text kısmını gösterir


    def selected_Changed_Index(self,index):
        print(index)                            #Index bilgisi getirir
                                                
                                                
    def selected_Changed_Text(self,text):
        print(text)                             #Text Bilgisi getirir


    def clear_Item(self):
            self.UI.comboBox.clear()  #ComboBox daki bütün öğeleri siler



def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()