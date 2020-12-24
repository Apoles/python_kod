import sys
from PyQt5 import QtWidgets
from projem import Ui_MainWindow
import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)
        self.load_Data_Base()


    def load_Data_Base(self): #Data base bağlantısı yapıldı
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoles123...",
        database="okul"
    )

        cursor=connection.cursor()

        cursor.execute("SELECT KitapIsmi,Yazar,Sayfa,Tür,Durum From okul ")
        result=cursor.fetchall()

        
        
        
        self.UI.tableWidget.setRowCount(len(result))
        self.UI.tableWidget.setColumnCount(5)
        self.UI.tableWidget.setHorizontalHeaderLabels(("Kitap ismi","Yazar","Sayfa","Tür","Durum")) #Başlık değiştime
        self.UI.tableWidget.setColumnWidth(0,120)  #kolon genişlikleri
        self.UI.tableWidget.setColumnWidth(1,120)

        row_Index=0

        for i in result:
            
    
            self.UI.tableWidget.setItem(row_Index,0,QTableWidgetItem(str(i[0])))
            self.UI.tableWidget.setItem(row_Index,1,QTableWidgetItem(str(i[1])))
            self.UI.tableWidget.setItem(row_Index,2,QTableWidgetItem(str(i[2])))
            self.UI.tableWidget.setItem(row_Index,3,QTableWidgetItem(str(i[3])))
            self.UI.tableWidget.setItem(row_Index,4,QTableWidgetItem(str(i[4])))
            
            row_Index+=1










def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()