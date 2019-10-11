from PyQt5 import QtCore, QtGui, QtWidgets
import os

def load_project_structure(startpath, tree):
    # cc: https://stackoverflow.com/questions/5144830
    """
    Load Project structure tree
    :param startpath:
    :param tree:
    :return:
    """
    from PyQt5.QtWidgets import QTreeWidgetItem
    from PyQt5.QtGui import QIcon
    for element in os.listdir(startpath):
        path_info = startpath + "/" + element
        parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
        if os.path.isdir(path_info):
            load_project_structure(path_info, parent_itm)
            parent_itm.setIcon(0, QIcon('folder.png'))
        else:
            parent_itm.setIcon(0, QIcon('file.png'))

#@QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
def getItemFullPath(item):
    out = item.text(0)

    if item.parent():
        out = getItemFullPath(item.parent()) + "/" + out
    else:
        out =  "../content/" + out
    return out;


def onItemClicked(it, col):
    print(it, col, it.text(col))
    # print(it, col, it.text(col))
    print(getItemFullPath(it))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.show()
sys.exit(app.exec_())