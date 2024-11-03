from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import gui
import sys
import downloader
from downloader import Resolution


class Example(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clickMethod)
        self.pushButton_2.clicked.connect(self.scan)
        self.pushButton_3.clicked.connect(self.down)
    def scan(self):
        value = self.lineEdit.text()
        Resolution(value)
        Resolution
        for i in range(0, len(downloader.keylist)):
            self.comboBox.addItem(downloader.keylist[i])
    def clickMethod(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lineEdit_2.setText(folderpath)
    def down(self):
        downloader.Download(int(downloader.dict[self.comboBox.currentText()]),str(self.lineEdit.text()),str(self.lineEdit_2.text()))
        self.progressBar.setValue(100)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Example()
    form.show()
    app.exec()

      