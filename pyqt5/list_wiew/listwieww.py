import sys
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QMessageBox  # Bir seçim yaptıgımızda karşımıza diyalog kutusu çıkartan sınıf.
from PyQt5 import QtWidgets
from listwiew import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)

        # öğrenci yükleme fonk u oluşturuyoruz
        self.load_students()

        # Yeni öğrenci ekleme
        self.UI.add_buton.clicked.connect(self.add_Student)

        # Öğrenci düzenleme

        self.UI.edit_buton.clicked.connect(self.edit_student)

        # Öğrenci silme
        self.UI.remove_buton.clicked.connect(self.remove_student)




    def load_students(self):
        self.UI.listWidget.addItems(["Abdullah","Ali","Aysenur","Zeynep"])  # list_items dan addItems özelliği ile bir liste ekliyoruz
        self.UI.listWidget.setCurrentRow(0)  # 0. eleman seçili olarak gelir

    def add_Student(self):
        text,ok=QInputDialog.getText(self,"NEW STUDENT","Student Name") # Diyalog kutsu bize text yazmamazı sağlar. GETİNT, GETDOUBLE tipleride vardır

        if ok and text is not None:
            self.UI.listWidget.insertItem(0,text)  # bize dönen text bilgisi ve ok bilgisi eğer bir değer içeriyorsa insertitem ile 0. indextden text bilgisini ekliyor
             
    def edit_student(self):
        index =self.UI.listWidget.currentRow()  # Düzenleme işemi yapmak için seçili olan kişinin indexsini currentrow methodu ile yapıyorz  
        item=self.UI.listWidget.item(index)     #Seçtiğimiz eleman alındı

        if item is not None:  #Seçtiğimiz eleman boş değilse
            text,ok =QInputDialog.getText(self,"Edit Student","Student name",QLineEdit.Normal,item.text()) # Qlineedit.normal ile düzenleme aktif edilir ver düzenlence text bilgisi girilir
            if text and ok is not None:   #eğer bizze dönen bilgiler gerçekden doldurulmuşsa 
                item.setText(text)

    def remove_student(self):
        index =self.UI.listWidget.currentRow()  
        item=self.UI.listWidget.item(index)     

        if item is None:
            return

        q=QMessageBox.question(self,"remove student???","Do you want to student????"+item.text(),QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item=self.UI.listWidget.takeItem(index)
            del item





def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()