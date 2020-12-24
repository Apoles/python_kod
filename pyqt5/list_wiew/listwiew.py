# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listwiew.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 40, 351, 361))
        self.listWidget.setObjectName("listWidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(410, 50, 351, 351))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_buton = QtWidgets.QPushButton(self.widget)
        self.add_buton.setObjectName("add_buton")
        self.verticalLayout.addWidget(self.add_buton)
        self.edit_buton = QtWidgets.QPushButton(self.widget)
        self.edit_buton.setObjectName("edit_buton")
        self.verticalLayout.addWidget(self.edit_buton)
        self.remove_buton = QtWidgets.QPushButton(self.widget)
        self.remove_buton.setObjectName("remove_buton")
        self.verticalLayout.addWidget(self.remove_buton)
        self.up_button = QtWidgets.QPushButton(self.widget)
        self.up_button.setObjectName("up_button")
        self.verticalLayout.addWidget(self.up_button)
        self.down_button = QtWidgets.QPushButton(self.widget)
        self.down_button.setObjectName("down_button")
        self.verticalLayout.addWidget(self.down_button)
        self.sort_buton = QtWidgets.QPushButton(self.widget)
        self.sort_buton.setObjectName("sort_buton")
        self.verticalLayout.addWidget(self.sort_buton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.exit_buton = QtWidgets.QPushButton(self.widget)
        self.exit_buton.setObjectName("exit_buton")
        self.verticalLayout.addWidget(self.exit_buton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 26))
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
        self.add_buton.setText(_translate("MainWindow", "Add"))
        self.edit_buton.setText(_translate("MainWindow", "Edit"))
        self.remove_buton.setText(_translate("MainWindow", "Remove"))
        self.up_button.setText(_translate("MainWindow", "Up"))
        self.down_button.setText(_translate("MainWindow", "Down"))
        self.sort_buton.setText(_translate("MainWindow", "sort"))
        self.exit_buton.setText(_translate("MainWindow", "Exiyt"))
