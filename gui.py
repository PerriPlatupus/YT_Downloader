        # -*- coding: utf-8 -*-

        # Form implementation generated from reading ui file 'name.ui'
        #
        # Created by: PyQt5 UI code generator 5.15.9
        #
        # WARNING: Any manual changes made to this file will be lost when pyuic5 is
        # run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("YTDownloader")
        Dialog.resize(400, 300)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 270, 371, 23))
        self.progressBar.setValue(0)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 281, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 90, 281, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 140, 160, 22))
        self.comboBox.setObjectName("comboBox")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 221, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 71, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 61, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(26, 210, 51, 20))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 141, 16))
        self.label_6.setObjectName("label_6")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 180, 69, 22))
        self.pushButton_3.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("YTDownloader", "YTDownloader"))
        self.pushButton.setText(_translate("YTDownloader", "Обзор..."))
        self.label.setText(_translate("YTDownloader", "Ссылка на ютуб:"))
        self.label_2.setText(_translate("YTDownloader", "Место сохранения:"))
        self.label_3.setText(_translate("YTDownloader", "Разрешение"))
        self.label_6.setText(_translate("YTDownloader", "Прогресс скачивания"))
        self.pushButton_2.setText(_translate("YTDownloader", "Скан"))
        self.pushButton_3.setText(_translate("YTDownloader", "Скачать"))
