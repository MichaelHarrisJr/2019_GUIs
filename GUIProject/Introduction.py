import sys

from pathlib import Path

from PyQt5 import QtCore, QtWidgets, QtGui
# from PyPWA.libs.file import processor
"""
 Check list Introduction.py Fall 2019

1. Have Introdution, Wizard, and Main link up together+


2. Get Introduction window to exit out after entering Main from "New Project" 
and "Open Project".

3. Setup file dialog connection in Intro "Open Project"

4. Add Jefferson Lab and NSU logo into Introduction

"""
# Introduction GUI Window
class IntroductionPWA(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # Locks Introduction PWA window
        self.setFixedSize(800, 400)
        self.setWindowTitle('PyPWA 3')
        self.open_project_button()
        self.__new_project_button()
        self.__design()

    def __new_project_button(self):
        self.new = QtWidgets.QPushButton('New Project', self)
        self.new.clicked.connect(self.toggle_new_project)
        self.new.move(100, 300)

    def open_project_button(self):
        self.open = QtWidgets.QPushButton('Open Project', self)
        self.open.clicked.connect(self.toggle_open_project)
        self.open.move(600, 300)

    def __design(self):
        pwa = QtWidgets.QLabel(self)
        pwa.setPixmap(QtGui.QPixmap('pypwa.png'))
        pwa.move(125, 50)

        jlab = QtWidgets.QLabel('Thomas Jefferson National Accelerator Facility', self)
        jlab.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Black))
        jlab.move(160, 175)

        nsu = QtWidgets.QLabel('Norfolk State University', self)
        nsu.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Black))
        nsu.move(280, 215)

    def toggle_new_project(self):
        new_project = MagicWizard(self)
        new_project.show()

    def toggle_open_project(self):
        open_project = MainPWA()
        open_project.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('pypwaicon1.png'))
    gui = IntroductionPWA()
    gui.show()
    app.exec_()