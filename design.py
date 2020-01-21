# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.portSelect = QtWidgets.QComboBox(self.centralwidget)
        self.portSelect.setGeometry(QtCore.QRect(60, 70, 261, 25))
        self.portSelect.setObjectName("portSelect")
        self.speedSelect = QtWidgets.QComboBox(self.centralwidget)
        self.speedSelect.setGeometry(QtCore.QRect(60, 140, 261, 25))
        self.speedSelect.setObjectName("speedSelect")
        self.labelPort = QtWidgets.QLabel(self.centralwidget)
        self.labelPort.setGeometry(QtCore.QRect(60, 50, 67, 17))
        self.labelPort.setObjectName("labelPort")
        self.labelSpeed = QtWidgets.QLabel(self.centralwidget)
        self.labelSpeed.setGeometry(QtCore.QRect(60, 120, 67, 17))
        self.labelSpeed.setObjectName("labelSpeed")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 180, 261, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonOn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonOn.setObjectName("buttonOn")
        self.horizontalLayout.addWidget(self.buttonOn)
        self.buttonConect = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonConect.setObjectName("buttonConect")
        self.horizontalLayout.addWidget(self.buttonConect)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelPort.setText(_translate("MainWindow", "Порт"))
        self.labelSpeed.setText(_translate("MainWindow", "Швидкість"))
        self.buttonOn.setText(_translate("MainWindow", "Увімкнути"))
        self.buttonConect.setText(_translate("MainWindow", "Підключитись"))

