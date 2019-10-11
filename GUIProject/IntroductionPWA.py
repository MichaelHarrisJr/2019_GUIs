import sys


from PyQt5.QtCore import (QFile, QPoint, QRect, QSize, QStandardPaths, Qt, QProcess, QSettings)
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QMainWindow, QLineEdit, QProgressBar
from PyQt5.QtWidgets import QMessageBox, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QMessageBox, QToolButton, QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets, QtGui


class IntroductionPWA(QWidget):

    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 400
        self.setWindowTitle('Welcome to PyPWA 3')
        self.__new_project_button()
        self.__open_project_button()
        self.__design()
        self.show()
    def __design(self):
        pwa = QLabel(self)
        pwa.setPixmap(QtGui.QPixmap('pypwa.png'))
        pwa.move(125, 50)

        local = QLabel('Thomas Jefferson National Accelerator Facility', self)
        local.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        local.move(250, 165)

        #self.__file_browser_bar()


    def __new_project_button(self):

        new = QPushButton('New Project', self)
        new.move(100, 300)
        #new.clicked.connect(self.MainPWA.py)




    #def __file_browser_bar(self):
      #  bar = QLineEdit(self)
       # bar.move(325, 200)

    def __open_project_button(self):
        open = QPushButton('Open Project', self)
        open.move(600, 300)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = IntroductionPWA()
    sys.exit(app.exec_())