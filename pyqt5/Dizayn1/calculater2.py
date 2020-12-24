from PyQt5 import QtWidgets
import sys
from dizayn1 import Ui_MainWindow

class Myapp(QtWidgets.QMainWindow):  #class tanılaması yaptık
    def __init__(self):
        super(Myapp,self).__init__()
        self.UI=Ui_MainWindow()   #Geçenki konularda UI oluşturuyorduk label,text falan. Burada biz UI'i dizayn ettiğimiz programdan alıyoruz 
        self.UI.setupUi(self) # app clasında oluşturdugumuz UI içersindeki elemanlarına tek tek ullaşabiliyoruz

   
def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Myapp()
    win.show()
    sys.exit(app.exec_())



app()
