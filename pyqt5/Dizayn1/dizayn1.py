# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dizayn1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sayi1 = QtWidgets.QLabel(self.centralwidget)
        self.sayi1.setGeometry(QtCore.QRect(370, 250, 55, 16))
        self.sayi1.setObjectName("sayi1")
        self.sayi2 = QtWidgets.QLabel(self.centralwidget)
        self.sayi2.setGeometry(QtCore.QRect(370, 360, 55, 16))
        self.sayi2.setObjectName("sayi2")
        self.girdi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.girdi1.setGeometry(QtCore.QRect(420, 240, 191, 41))
        self.girdi1.setText("")
        self.girdi1.setObjectName("girdi1")
        self.girdi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.girdi2.setGeometry(QtCore.QRect(420, 360, 241, 31))
        self.girdi2.setObjectName("girdi2")
        self.buton = QtWidgets.QPushButton(self.centralwidget)
        self.buton.setGeometry(QtCore.QRect(450, 470, 93, 28))
        self.buton.setObjectName("buton")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(770, 70, 256, 192))
        self.columnView.setObjectName("columnView")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(270, 550, 135, 80))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1109, 26))
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
        self.sayi1.setText(_translate("MainWindow", "Sayi1"))
        self.sayi2.setText(_translate("MainWindow", "Sayi2"))
        self.buton.setText(_translate("MainWindow", "Ok"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
