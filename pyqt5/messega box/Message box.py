import sys
from PyQt5 import QtWidgets
from message_Box import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox   #Mesaj box ile çalışacağım için importluyorum
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.UI=Ui_MainWindow()
        self.UI.setupUi(self)

        self.UI.exit_Buton.clicked.connect(self.show_Dialog)

        

    def show_Dialog(self):


        result=QMessageBox.question(self,'Close application',"Are you sure?",QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Ignore,QMessageBox.Cancel)
        if result==QMessageBox.Ok: #Kullanıcı ok tuşuna bastımı

            print('yes clicl')
            QtWidgets.qApp.quit()

        else:
            print("no clik")
             
            














        """ // UZUN YOL
        msg=QMessageBox()

        msg.setWindowTitle("Close apllication")
        msg.setText("Are you sure ?")  #Diyalog kutusu mesajı
        msg.setIcon(QMessageBox.Question) # Soru diyalogu  .Warning uyarı diyalogu
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Ignore)  # Diyalog kutusuna neler  gelsin
        msg.setDefaultButton(QMessageBox.Ok) # ok butonu seçili olrak gelsin
        msg.setDetailedText("çıkma ÖLÜRSÜN....") #detaylar iconu gelir

        msg.buttonClicked.connect(self.popup_Button)

        x=msg.exec_()  #Burdaki x iconlara bastığımızda sayısal değerler döndürüyor örneğin ok butonu 1024 değeri döndürür.

    def popup_Button(self,i): #i hangi butonu tıklandıysa o bilgiyi gönderir
        print(i.text())

        if i.text()=='OK':
            QtWidgets.qApp.quit()
        elif i=="cancel":
            print("Cancel")

        elif i=="ignore":
            print("ignore")


"""

       



def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()
