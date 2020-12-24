# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 40, 411, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(500, 50, 231, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_Name = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_Name.setObjectName("label_Name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_Name)
        self.name_Edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_Edit.setObjectName("name_Edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.name_Edit)
        self.price_Edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.price_Edit.setObjectName("price_Edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.price_Edit)
        self.label_Price = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_Price.setObjectName("label_Price")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_Price)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 26))
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
        self.label_Name.setText(_translate("MainWindow", "Name"))
        self.label_Price.setText(_translate("MainWindow", "Price"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
