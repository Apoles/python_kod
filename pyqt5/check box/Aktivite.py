# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Aktivite.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 360, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setGeometry(QtCore.QRect(340, 370, 261, 121))
        self.lbl.setObjectName("lbl")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 361, 221))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 281, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Film = QtWidgets.QCheckBox(self.layoutWidget)
        self.Film.setObjectName("Film")
        self.verticalLayout.addWidget(self.Film)
        self.Kitap = QtWidgets.QCheckBox(self.layoutWidget)
        self.Kitap.setMinimumSize(QtCore.QSize(0, 20))
        self.Kitap.setObjectName("Kitap")
        self.verticalLayout.addWidget(self.Kitap)
        self.Yemek = QtWidgets.QCheckBox(self.layoutWidget)
        self.Yemek.setObjectName("Yemek")
        self.verticalLayout.addWidget(self.Yemek)
        self.Spor = QtWidgets.QCheckBox(self.layoutWidget)
        self.Spor.setMinimumSize(QtCore.QSize(20, 20))
        self.Spor.setObjectName("Spor")
        self.verticalLayout.addWidget(self.Spor)
        self.groupBoxx = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxx.setGeometry(QtCore.QRect(390, 80, 361, 221))
        self.groupBoxx.setObjectName("groupBoxx")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBoxx)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 40, 281, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Film_2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.Film_2.setObjectName("Film_2")
        self.verticalLayout_2.addWidget(self.Film_2)
        self.Kitap_2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.Kitap_2.setMinimumSize(QtCore.QSize(0, 20))
        self.Kitap_2.setObjectName("Kitap_2")
        self.verticalLayout_2.addWidget(self.Kitap_2)
        self.Yemek_2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.Yemek_2.setObjectName("Yemek_2")
        self.verticalLayout_2.addWidget(self.Yemek_2)
        self.Spor_2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.Spor_2.setMinimumSize(QtCore.QSize(20, 20))
        self.Spor_2.setObjectName("Spor_2")
        self.verticalLayout_2.addWidget(self.Spor_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 26))
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
        self.pushButton.setText(_translate("MainWindow", "ONAYLA"))
        self.lbl.setText(_translate("MainWindow", "Sonuç"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.Film.setText(_translate("MainWindow", "Film izleme"))
        self.Kitap.setText(_translate("MainWindow", "Kitap okuma"))
        self.Yemek.setText(_translate("MainWindow", "Spor"))
        self.Spor.setText(_translate("MainWindow", "Yemek yapma"))
        self.groupBoxx.setTitle(_translate("MainWindow", "GroupBox"))
        self.Film_2.setText(_translate("MainWindow", "Film izleme"))
        self.Kitap_2.setText(_translate("MainWindow", "Kitap okuma"))
        self.Yemek_2.setText(_translate("MainWindow", "Spor"))
        self.Spor_2.setText(_translate("MainWindow", "Yemek yapma"))
