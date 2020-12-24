# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RadioButon.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_ulke = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ulke.setGeometry(QtCore.QRect(100, 370, 191, 16))
        self.lbl_ulke.setObjectName("lbl_ulke")
        self.Ulke_Secimi_buton = QtWidgets.QPushButton(self.centralwidget)
        self.Ulke_Secimi_buton.setGeometry(QtCore.QRect(90, 290, 131, 41))
        self.Ulke_Secimi_buton.setObjectName("Ulke_Secimi_buton")
        self.lbl_egitim = QtWidgets.QLabel(self.centralwidget)
        self.lbl_egitim.setGeometry(QtCore.QRect(400, 370, 201, 16))
        self.lbl_egitim.setObjectName("lbl_egitim")
        self.Eitim_Secimi_Buton = QtWidgets.QPushButton(self.centralwidget)
        self.Eitim_Secimi_Buton.setGeometry(QtCore.QRect(390, 290, 131, 41))
        self.Eitim_Secimi_Buton.setObjectName("Eitim_Secimi_Buton")
        self.groupBox_Ulke = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Ulke.setGeometry(QtCore.QRect(40, 60, 271, 211))
        self.groupBox_Ulke.setObjectName("groupBox_Ulke")
        self.Ingiltere_Buton = QtWidgets.QRadioButton(self.groupBox_Ulke)
        self.Ingiltere_Buton.setGeometry(QtCore.QRect(41, 144, 74, 20))
        self.Ingiltere_Buton.setObjectName("Ingiltere_Buton")
        self.Turkiye_buton = QtWidgets.QRadioButton(self.groupBox_Ulke)
        self.Turkiye_buton.setGeometry(QtCore.QRect(41, 48, 69, 20))
        self.Turkiye_buton.setObjectName("Turkiye_buton")
        self.Azerbayca_Buton = QtWidgets.QRadioButton(self.groupBox_Ulke)
        self.Azerbayca_Buton.setGeometry(QtCore.QRect(41, 112, 93, 20))
        self.Azerbayca_Buton.setObjectName("Azerbayca_Buton")
        self.Usa_Buton = QtWidgets.QRadioButton(self.groupBox_Ulke)
        self.Usa_Buton.setGeometry(QtCore.QRect(41, 80, 51, 20))
        self.Usa_Buton.setObjectName("Usa_Buton")
        self.groupBox_Egitim = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Egitim.setGeometry(QtCore.QRect(330, 60, 261, 211))
        self.groupBox_Egitim.setObjectName("groupBox_Egitim")
        self.Lise_Buton = QtWidgets.QRadioButton(self.groupBox_Egitim)
        self.Lise_Buton.setGeometry(QtCore.QRect(51, 78, 50, 20))
        self.Lise_Buton.setObjectName("Lise_Buton")
        self.Universte_Buton = QtWidgets.QRadioButton(self.groupBox_Egitim)
        self.Universte_Buton.setGeometry(QtCore.QRect(51, 142, 80, 20))
        self.Universte_Buton.setObjectName("Universte_Buton")
        self.Ilk_Okul_Buton = QtWidgets.QRadioButton(self.groupBox_Egitim)
        self.Ilk_Okul_Buton.setGeometry(QtCore.QRect(51, 46, 67, 20))
        self.Ilk_Okul_Buton.setObjectName("Ilk_Okul_Buton")
        self.Orta_Okul_Buton = QtWidgets.QRadioButton(self.groupBox_Egitim)
        self.Orta_Okul_Buton.setGeometry(QtCore.QRect(51, 110, 79, 20))
        self.Orta_Okul_Buton.setObjectName("Orta_Okul_Buton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_ulke.setText(_translate("MainWindow", "SECİM"))
        self.Ulke_Secimi_buton.setText(_translate("MainWindow", "Ülke seçimi"))
        self.lbl_egitim.setText(_translate("MainWindow", "SECİM"))
        self.Eitim_Secimi_Buton.setText(_translate("MainWindow", "Eğitim seiçimi"))
        self.groupBox_Ulke.setTitle(_translate("MainWindow", "Ulke"))
        self.Ingiltere_Buton.setText(_translate("MainWindow", "Ingiltere"))
        self.Turkiye_buton.setText(_translate("MainWindow", "Türkiye"))
        self.Azerbayca_Buton.setText(_translate("MainWindow", "Azerbeycan"))
        self.Usa_Buton.setText(_translate("MainWindow", "USA"))
        self.groupBox_Egitim.setTitle(_translate("MainWindow", "Egitim"))
        self.Lise_Buton.setText(_translate("MainWindow", "Lİse"))
        self.Universte_Buton.setText(_translate("MainWindow", "Universte"))
        self.Ilk_Okul_Buton.setText(_translate("MainWindow", "Ilk okul"))
        self.Orta_Okul_Buton.setText(_translate("MainWindow", "Orta okul"))
