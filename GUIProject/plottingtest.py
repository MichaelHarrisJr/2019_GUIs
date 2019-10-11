import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon


import seaborn as sns
sns.set()
import matplotlib.pyplot as plt

import random

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0,0)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500,0)
        button.resize(140,100)

        self.show()


class PlotCanvas(sns):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = sns(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        sns.__init__(self, fig)
        self.setParent(parent)

        sns.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        sns.updateGeometry(self)
        self.plot()


    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('Matplotlib Example')
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
