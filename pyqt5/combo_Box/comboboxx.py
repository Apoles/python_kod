# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combobox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 70, 221, 91))
        self.comboBox.setObjectName("comboBox")
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(430, 80, 101, 31))
        self.lbl_result.setObjectName("lbl_result")
        self.Get_Item = QtWidgets.QPushButton(self.centralwidget)
        self.Get_Item.setGeometry(QtCore.QRect(130, 200, 161, 61))
        self.Get_Item.setObjectName("Get_Item")
        self.Load_Items = QtWidgets.QPushButton(self.centralwidget)
        self.Load_Items.setGeometry(QtCore.QRect(360, 200, 161, 61))
        self.Load_Items.setObjectName("Load_Items")
        self.clear_Item = QtWidgets.QPushButton(self.centralwidget)
        self.clear_Item.setGeometry(QtCore.QRect(230, 320, 161, 91))
        self.clear_Item.setObjectName("clear_Item")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.lbl_result.setText(_translate("MainWindow", "TextLabel"))
        self.Get_Item.setText(_translate("MainWindow", "Get İtem"))
        self.Load_Items.setText(_translate("MainWindow", "Load Items"))
        self.clear_Item.setText(_translate("MainWindow", "Clear Items"))
