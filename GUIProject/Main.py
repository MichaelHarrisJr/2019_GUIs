import sys
from pathlib import Path

from PyQt5 import QtCore, QtWidgets, QtGui
# from PyPWA.libs.file import processor

"""
 Check list Main.py Fall 2019

1. Setup History Log

2. Setup Status Bar: "Running, Processing, Error, and Stop". 
Maybe look at percentage processing.

3.  Create window boxes for "Restore" and "Save". Setup the connections and file dialog

4. 

"""

# Main GUI Window
class MainPWA(QtWidgets.QMainWindow, QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # Set the size of window box
        self.Width = 1060
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)
        self.setWindowTitle("PyPWA")
        self.__menu_bar = self.menuBar()
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        table = TableWidget(self, True)
        grid_layout = QtWidgets.QGridLayout(self)
        grid_layout.addWidget(table)
        central_widget.setLayout(grid_layout)

        self.__file_menu()
        self.__edit_menu()

    def __file_menu(self):
        file_menu = self.__menu_bar.addMenu("File")
        new_project = QtWidgets.QAction(QtGui.QIcon(), 'New Project', self)
        new_project.setStatusTip('Created A New Project name: ')
        # Need works for saving project
        new_project.triggered.connect(self.saveState)
        file_menu.addAction(new_project)

        # Create New File
        new_file = QtWidgets.QAction(QtGui.QIcon(), 'New File', self)
        new_file.setStatusTip('Created A New File: ')
        file_menu.addAction(new_file)

        # Save Files
        save_file_buttom = QtWidgets.QAction(QtGui.QIcon(), 'Save', self)
        save_file_buttom.setShortcut('Ctrl+S')
        # Note: Make sure to link File Path to status bar!!!!
        save_file_buttom.setStatusTip('File Saved: ')
        save_file_buttom.triggered.connect(self.close)
        file_menu.addAction(save_file_buttom)
        # Set an algorithm to Save files and SaveAs

        # Save As Files
        save_as_file_file_button = QtWidgets.QAction(QtGui.QIcon(), 'Save As', self)
        save_as_file_file_button.setShortcut('Ctrl+Shift+S')
        # Note: Make sure to link File Path to status bar!!!!
        save_as_file_file_button.setStatusTip('File Save As: ')
        save_as_file_file_button.triggered.connect(self.close)
        file_menu.addAction(save_as_file_file_button)

        # Exit Out from the program
        exit_button = QtWidgets.QAction(QtGui.QIcon(), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

    def __edit_menu(self):
        edit_menu = self.__menu_bar.addMenu("Edit")
        # Undo
        undo = QtWidgets.QAction(QtGui.QIcon(), 'Undo', self)
        undo.setShortcut('Ctrl+Z')
        undo.setStatusTip('Undo')
        edit_menu.addAction(undo)

        # Redo
        redo = QtWidgets.QAction(QtGui.QIcon(), 'Redo', self)
        redo.setShortcut('Ctrl+X')
        redo.setStatusTip('Redo')
        edit_menu.addAction(redo)

        self.__view_menu()

    def __view_menu(self):
        view_menu = self.__menu_bar.addMenu("View")

        # Maximize Screen
        maximize_screen = QtWidgets.QAction(QtGui.QIcon(), 'Maximize Screen', self)
        maximize_screen.setShortcut('Shift+F9')
        maximize_screen.setStatusTip('Minimize Screen')
        maximize_screen.triggered.connect(self.showMaximized)
        view_menu.addAction(maximize_screen)

        # Minimize Screen
        minimize_screen = QtWidgets.QAction(QtGui.QIcon(), 'Minimize Screen', self)
        minimize_screen.setShortcut('Shift+F9')
        minimize_screen.setStatusTip('Minimize Screen')
        minimize_screen.triggered.connect(self.showMinimized)
        view_menu.addAction(minimize_screen)

        # FullScreen
        fullscreen = QtWidgets.QAction(QtGui.QIcon(), 'FullScreen', self)
        fullscreen.setShortcut('Shift+F10')
        fullscreen.setStatusTip('Enabled Fullscreen Window')
        fullscreen.triggered.connect(self.showFullScreen)
        view_menu.addAction(fullscreen)

        self.__help_menu()

    def __help_menu(self):
        help_menu = self.__menu_bar.addMenu("Help")
        _help = QtWidgets.QAction(QtGui.QIcon(), 'Help', self)
        _help.setStatusTip('Help')
        # Help.triggered.connect(self.)
        help_menu.addAction(_help)

        report = QtWidgets.QAction(QtGui.QIcon(), 'Report', self)
        report.setStatusTip('Enabled Fullscreen Window')
        # Report.triggered.connect(self.)
        help_menu.addAction(report)

        about = QtWidgets.QAction(QtGui.QIcon(), 'About', self)
        about.setStatusTip('About')
        # About.triggered.connect(self.)
        help_menu.addAction(about)

        self.__subproject_menu()

    def __subproject_menu(self):
        subproject_menu = self.__menu_bar.addMenu("Subproject")
        mc = QtWidgets.QAction(QtGui.QIcon(), 'MC', self)
        mc.setStatusTip('MC')
        subproject_menu.addAction(mc)

        cha = QtWidgets.QAction(QtGui.QIcon(), 'CHA', self)
        cha.setStatusTip('CHA')
        subproject_menu.addAction(cha)

        new_subproject = QtWidgets.QAction(QtGui.QIcon(), 'New Subproject', self)
        new_subproject.setStatusTip('New Subproject')
        subproject_menu.addAction(new_subproject)

        self.status_bar()

    def status_bar(self):
        # Set the status bar
        self.statusBar().showMessage("Status Bar: ")

        self.__file_browser_side_bar()

        self.__jobs_side_bar()

    def __jobs_side_bar(self):
        # Set the Filling SideBar layout
        self.job_bar = QtWidgets.QDockWidget("Jobs", self)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.job_bar)
        self.dockedWidget = QtWidgets.QWidget(self)
        self.job_bar.setWidget(self.dockedWidget)
        self.dockedWidget.setLayout(QtWidgets.QVBoxLayout())

        self.__project_side_bar()

    def __project_side_bar(self):
        # Set the Filling SideBar layout
        self.project_side_bar = QtWidgets.QDockWidget("Projects", self)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.project_side_bar)
        self.dockedWidget = QtWidgets.QWidget(self)
        self.project_side_bar.setWidget(self.dockedWidget)
        self.dockedWidget.setLayout(QtWidgets.QVBoxLayout())

        self.__log_side_bar()

    def __log_side_bar(self):
        # Set the Bottom SideBar layout
        self.log_side_bar = QtWidgets.QDockWidget("Log", self)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.log_side_bar)
        self.dockedWidget = QtWidgets.QWidget(self)
        self.log_side_bar.setWidget(self.dockedWidget)

    def __file_browser_side_bar(self):
        self.file_browser_side_bar = QtWidgets.QDockWidget("File Browser", self)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.file_browser_side_bar)
        self.dockedWidget = FileBrowser()
        self.file_browser_side_bar.setWidget(self.dockedWidget)


# class MyDialog(QtWidgets.QPlainTextEdit):
#   def __init__(self, parent=None):
#      super(MyDialog, self).__init__(parent)
#
#       log_text_box = QPlainTextEdit()
# You can format what is printed to text box
#   log_text_box.setFormatter(
#        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
#   logging.getLogger().addHandler(log_text_box)
# You can control the logging level
#  logging.getLogger().setLevel(logging.DEBUG)

# l = logging.getLogger()

# for index in range(0, 10):
#   l.info(f"At place{index}")
#    def test(self):
#       logging.debug('damn, a bug')
#      logging.info('something to remember')
#     logging.warning('that\'s not right')
#    logging.error('foobar')


class FileBrowser(QtWidgets.QTreeWidget):

    def __init__(self, dir: Path = Path("."), include_hidden: bool = False):
        super(FileBrowser, self).__init__()
        self.__root_dir = dir
        self.__include_hidden = include_hidden
        self.__populate_directory_tree(dir, self)

    def __repr__(self):
        return f"FileBrowser({self.__root_dir}, {self.__include_hidden})"

    def __populate_directory_tree(self, root_folder, parent):
        for element in root_folder.glob("*"):
            if not str(element.stem)[0] == "." or self.__include_hidden:

                new_parent = QtWidgets.QTreeWidgetItem(parent, [str(element.stem)])
                if element.is_dir():
                    self.__populate_directory_tree(element, new_parent)
                    new_parent.setIcon(0, QtGui.QIcon().fromTheme("folder"))
                else:
                    new_parent.setIcon(0, QtGui.QIcon().fromTheme("text-x-generic"))


class TableWidget(QtWidgets.QWidget):

    def __init__(self, parent, is_simulation=False):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QtWidgets.QTabWidget()
        self.simulation = QtWidgets.QWidget()
        self.fitting = QtWidgets.QWidget()
        self.resonance = Resonance(self)
        self.data = QtWidgets.QWidget()
        self.data_box()
        self.grid = QtWidgets.QGridLayout()
        self.plots = QtWidgets.QWidget()
        self.tabs.resize(300, 200)
        self.lbl = QtWidgets.QLabel("", self)

        # Add tabs
        if is_simulation:
            self.tabs.addTab(self.simulation, "Simulation")
        else:
            self.tabs.addTab(self.fitting, "Fitting")
        self.tabs.addTab(self.resonance, "Resonance")
        self.tabs.addTab(self.data, "Data")
        self.tabs.addTab(self.plots, "Plots")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def data_box(self):
        self.data_table = QtWidgets.QTableWidget()
        self.data_table.setRowCount(4)
        self.data_table.setColumnCount(3)
        self.data_table.setHorizontalHeaderLabels(["X", "Y", "Z"])
        self.data_table.setItem(0, 0, QtWidgets.QTableWidgetItem("TEST"))
        self.data_table.setItem(0, 1, QtWidgets.QTableWidgetItem("TEST"))
        self.data_table.setItem(1, 0, QtWidgets.QTableWidgetItem())
        self.data_table.setItem(1, 1, QtWidgets.QTableWidgetItem())
        self.data_table.setItem(2, 0, QtWidgets.QTableWidgetItem())
        self.data_table.setItem(2, 1, QtWidgets.QTableWidgetItem())
        self.data_table.setItem(3, 0, QtWidgets.QTableWidgetItem())
        self.data_table.setItem(3, 1, QtWidgets.QTableWidgetItem())

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.data_table)
        self.data.setLayout(layout)


class Controls(QtWidgets.QWidget):

    def __int__(self, parent=None):
        super(Controls, self).__int__(parent)


class Resonance(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Resonance, self).__init__(parent)
        self.__create_layouts()

    def __create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(self.__create_main_layout())
        main_layout.addLayout(self.__create_button_layout())
        self.setLayout(main_layout)

    def __create_main_layout(self):
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.__check_list())
        layout.addWidget(self.__resonance_table())
        return layout

    @staticmethod
    def __check_list():
        check_list = QtWidgets.QListWidget()
        str_list = ["Test", "Test", "Test"]
        check_list.addItems(str_list)

        for index in range(check_list.count()):
            item = check_list.item(index)
            item.setFlags(
                QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
            )
            item.setCheckState(QtCore.Qt.Unchecked)

        return check_list

    @staticmethod
    def __resonance_table():
        table = QtWidgets.QTableWidget()
        table.setRowCount(4)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["X", "Y", "Z"])
        table.setItem(0, 0, QtWidgets.QTableWidgetItem("TEST"))
        table.setItem(0, 1, QtWidgets.QTableWidgetItem("TEST"))
        table.setItem(1, 0, QtWidgets.QTableWidgetItem())
        table.setItem(1, 1, QtWidgets.QTableWidgetItem())
        table.setItem(2, 0, QtWidgets.QTableWidgetItem())
        table.setItem(2, 1, QtWidgets.QTableWidgetItem())
        table.setItem(3, 0, QtWidgets.QTableWidgetItem())
        table.setItem(3, 1, QtWidgets.QTableWidgetItem())
        return table

    def __create_button_layout(self):
        save_button = QtWidgets.QPushButton("SAVE")
        restore_button = QtWidgets.QPushButton("Restore")
        save_button.clicked.connect(self.__save_toggle_resonance_window)
        restore_button.clicked.connect(self.__restore_toggle_resonance_window)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(save_button)
        layout.addWidget(restore_button)
        layout.setAlignment(QtCore.Qt.AlignRight)
        return layout

    def __save_toggle_resonance_window(self):
        new_window = ResonanceSaveWindow(self)
        new_window.show()

    def __restore_toggle_resonance_window(self):
        new_window = ResonanceRestoreWindow(self)
        new_window.show()


class ResonanceSaveWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ResonanceSaveWindow, self).__init__(parent)

        options = QtWidgets.QFileDialog.Option()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", "", "All Files (*);;Text Files (*.txt)", options=options
        )
        if fileName:
            print(fileName)


class ResonanceRestoreWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ResonanceRestoreWindow, self).__init__(parent)
        # ISSUE: whenever file dialog is open, if you push cancel it'll close out the whole window
        options = QtWidgets.QFileDialog.Option()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, = QtWidgets.QFileDialog.getSaveFileName(
            self, "Restore File", "", "All Files (*);;Text Files (*.txt)", options=options
        )
        if filename:
            print(filename)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('pypwaicon1.png'))
    gui = MainPWA()
    gui.show()
    app.exec_()