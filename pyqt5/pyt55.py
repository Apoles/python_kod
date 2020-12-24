import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow #satır 5 deki yazımı kısaltmak için import edildi
from PyQt5.QtGui import QIcon #Varsayılan ikonu değiştirmek için importlama işemi
from PyQt5.QtWidgets import QToolTip #tooltip değiştimek için import edildi


class MyWindow(QMainWindow): #Nesnemizi QmainWindow dan türettik
    def __init__(self):
        
        super(MyWindow,self).__init__()

        self.setWindowTitle("Fist Application")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("aa.jpg")) 
        self.setToolTip('my tooltip') 
        self.initUI()

    def initUI(self):
        
        
        self.lbl_name=QtWidgets.QLabel(self)  
        self.lbl_name.setText("Adınız:")
        self.lbl_name.move(50,30)
         

        self.lbl_surname=QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadnız")
        self.lbl_surname.move(50,70)


        self.lbl_result=QtWidgets.QLabel(self)
        self.lbl_result.setText("SONUÇ")
        self.lbl_result.resize(200,40)
        self.lbl_result.move(150,150)
        



        self.txt_name=QtWidgets.QLineEdit(self) 
        self.txt_name.move(150,30)
        self.txt_name.resize(230,32) # text box un boyutunu değiştirdik

        self.txt_surnam=QtWidgets.QLineEdit(self)
        self.txt_surnam.move(150,70)
        self.txt_surnam.resize(230,32)

        self.btn_save=QtWidgets.QPushButton(self)  
        self.btn_save.setText('GİRİŞ') 
        self.btn_save.move(150,110)  
        self.btn_save.clicked.connect(self.tiklama)

    def tiklama(self):
        self.lbl_result.setText("bı bir örnekdir") #Yukarıdaki oluşturduğumuz lbl_result ile bağlantı kurduk

def window(): 
   
    app=QApplication(sys.argv) 
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())



window()





"""
win1=MyWindow()  #tanımlana win1 ve win2 yukarıdaki self yerine geçicek
win2=MyWindow()

"""
















#############
#############
# İŞİMİZİ CLASS LA YAPMAK DAHA KOLAY OLDUGU İÇİN YUKARIDA CLASS KULLANDIK AŞŞAĞIDAKİ İLE BİRİBİR AYNIDIR#

"""
def window(): #pencere window objesi oluşturucaz
    #app = QtWidgets.QApplication #QtWidgets den QApplication alabiliriz yada yukarda import edip direk QApplication yazabılırız aşşağıdaki örnekde oldugu gibi
    app=QApplication(sys.argv) #Satır 5 in kısa yazılımı
    win=QMainWindow() #pencere oluşturduk

  

    win.setWindowTitle("Fist Application") #Uygulama title değiştirdi
    win.setGeometry(200,200,500,500) #200 x 200 y de açar ve boyur olarak 500 e 500 bir pencere oluşturur
    win.setWindowIcon(QIcon("aa.jpg")) # icon resimi değiştirme
    win.setToolTip('my tooltip') #tooltip değiştimel için kullanıldı
    


    lbl_name=QtWidgets.QLabel(win) #label win(yani penceremizin) objesine ekleniyor 
    lbl_name.setText("Adınız:") #Adınız: yazan bir label eklenecekdir
    lbl_name.move(50,30) # x de 50 y de 30 kaydırırz

    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadnız")
    lbl_surname.move(50,70)

    txt_name=QtWidgets.QLineEdit(win) #yazma editörü kullanır
    txt_name.move(150,30)

    txt_surnam=QtWidgets.QLineEdit(win)
    txt_surnam.move(150,70)
      
    def tıklama(self):
        print("Butona tıklandı...\nName:"+txt_name.text()+"\nSurname:"+txt_surnam.text()) #txt_name ve txt_surname in text özellikleri alındı

    btn_save=QtWidgets.QPushButton(win)  #Buton oluşturma
    btn_save.setText('GİRİŞ') #Buton üzerine yazı yazıyoruz
    btn_save.move(150,110)  
    btn_save.clicked.connect(tıklama) # Yukarda oluşturdugumuz tıklama fonksiyonunu çağırdık.Butona tıklandıgında çağırılacak


   




    
    win.show() #Ekranda göstericez
    sys.exit(app.exec_()) #Çarpı ikonu oluşturup programı bitirmeye yarıyor




window()
"""