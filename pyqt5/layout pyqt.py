import sys 
from PyQt5  import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QPalette,QColor  #zemin rengi ve palet için gerekli sınıf

class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)  #  Arka Planı otomatik olarak boyar
        self.setGeometry(300,300,500,500)

     


        palette=self.palette() #Palet oluşturduk
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()


        #layout=QtWidgets.QVBoxLayout() #alt alta renkleri sıralandırdı

        #layout.addWidget(Color("red"))
        #layout.addWidget(Color("green"))
        #layout.addWidget(Color("blue"))

        layout=QtWidgets.QGridLayout()
        layout.addWidget(Color('red'),0,0)
        layout.addWidget(Color('blue'),1,0)
        layout.addWidget(Color('green'),0,2)
        layout.addWidget(Color('yellow'),3,1)

        widget=QWidget()
        widget.setLayout(layout)

        
        self.setCentralWidget(widget)


def app():
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())

app()


