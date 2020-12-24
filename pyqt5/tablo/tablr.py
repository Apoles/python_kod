import sys
from PyQt5 import QtWidgets
from table import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)

        self.load_Products()

        self.UI.pushButton.clicked.connect(self.save_Products)


    def save_Products(self):
        name=self.UI.name_Edit.text()
        fiyat=self.UI.price_Edit.text()

        if name and fiyat is not None:
            row_Count=self.UI.tableWidget.rowCount()  #Tablodaki eleman sayısını öğreniyoruz
            print(row_Count)
            self.UI.tableWidget.insertRow(row_Count) #Bu kod ile satır ekleme işlemi gerçekleştirioyuz row_Count ile kaçıncı satırı ekliceğimizi görüyorz
            self.UI.tableWidget.setItem(row_Count,0,QTableWidgetItem(name)) 
            self.UI.tableWidget.setItem(row_Count,1,QTableWidgetItem(fiyat))





    def load_Products(self):
        # DİNAMİK BİR VERİ OLDUGUNDA NASIL YUKLICEZ GÖRELİM
        products=[
                {'Name':"SamsungS5","Price":2000},
                {'Name':"SamsungS6","Price":3000}, 
                {'Name':"SamsungS7","Price":4000},  
                {'Name':"SamsungS8","Price":5000}, 
        ]




        self.UI.tableWidget.setRowCount(len(products))
        self.UI.tableWidget.setColumnCount(2)
        self.UI.tableWidget.setHorizontalHeaderLabels(("name","Fiyat")) #Başlık değiştime
        self.UI.tableWidget.setColumnWidth(0,120)  #kolon genişlikleri
        self.UI.tableWidget.setColumnWidth(1,120)
    
        row_Index=0
        # BİLGİLERİ DİNAMİK BİR ŞEKİLDE DATA BASE DEN ALMA
        for product in products:
            self.UI.tableWidget.setItem(row_Index,0,QTableWidgetItem(product["Name"]))
            self.UI.tableWidget.setItem(row_Index,1,QTableWidgetItem(str(product["Price"]))) #int değerinde geldiği için str içine aldık
            row_Index+=1






        """
        self.UI.tableWidget.setItem(0,0,QTableWidgetItem("Samsung s5"))
        self.UI.tableWidget.setItem(0,1,QTableWidgetItem("2000"))
        self.UI.tableWidget.setItem(1,0,QTableWidgetItem("Samsung s6"))
        self.UI.tableWidget.setItem(1,1,QTableWidgetItem("3000"))
        self.UI.tableWidget.setItem(2,0,QTableWidgetItem("Samsung s7"))
        self.UI.tableWidget.setItem(2,1,QTableWidgetItem("4000"))"""

def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()