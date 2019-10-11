import sys
from pathlib import Path

from PyQt5 import QtCore, QtWidgets, QtGui
# from PyPWA.libs.file import processor

"""
Check List Wizard.py Fall 2019

1. Setup file dialog inside Wizard under "project_name_text"(change variable). 
Once the user is finished with the wizard then the project name will show up 
beside "Title" in Main_PyPWA.

2. Setup the connection between Wizard fitting
and simulation tab would work.

3. Have the Path file go to "Documents" ex: /C/Users/Michael(UserName)/documents. 
Set it up to link all file dialog variables. Also, try to see if you can find 
information to bypass user and get the correct path of the username.

4. Next step, see if it create the project folder inside the documents in the user's 
computer. If so, connect the file dialog in Introduction to Main_PyPWA. So, it can 
open up the project folder inside the Main_PyPWA.

5. Setup the connection from Wizard to Main_PyPWA for when the user chooses to do 
Simulation or Fitting.

"""

# Wizard GUI Window
class MagicWizard(QtWidgets.QWizard):

    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        self.addPage(Page1(self))
        self.addPage(Fitting(self))
        self.addPage(Simulation(self))
        self.addPage(BinSettings(self))
        self.setWindowTitle("PyPWA 3 Wizard ")


class Page1(QtWidgets.QWizardPage):

    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)
        print("Intialized Page 1")
        self.page_one_setup()
        self.page_one_layouts()
        self.toggle_fit()
        self.toggle_fit()

    def page_one_layouts(self):
        pwa = QtWidgets.QLabel(self)
        pwa.setPixmap(QtGui.QPixmap('pypwa.png'))
        information_layout = QtWidgets.QVBoxLayout()
        information_layout.addWidget(pwa)
        information_layout.addWidget(self.setup_box_one)
        self.setLayout(information_layout)

    def page_one_setup(self):
        self.setup_box_one = QtWidgets.QGroupBox()

        # Project Name area here
        project_layout = QtWidgets.QHBoxLayout()
        project_name_label = QtWidgets.QLabel('New Project Name:')
        project_name_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        project_name_text = QtWidgets.QLineEdit()
        project_layout.addWidget(project_name_label)
        project_layout.addWidget(project_name_text)

        # Basis area here
        basis_layout = QtWidgets.QHBoxLayout()
        basis_text = QtWidgets.QLabel('Basis')
        basis_text.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        basis_drop_box = QtWidgets.QComboBox()
        basis_drop_box.addItem("Basis Test 1")
        basis_drop_box.addItem("Basis Test 2")
        basis_layout.addWidget(basis_text)
        basis_layout.addWidget(basis_drop_box)

        # Frame area here
        frame_layout = QtWidgets.QHBoxLayout()
        frame_text = QtWidgets.QLabel('Frame')
        frame_text.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        frame_drop_box = QtWidgets.QComboBox()
        frame_drop_box.addItem("Frame Test 1")
        frame_drop_box.addItem("Frame Test 2")
        frame_layout.addWidget(frame_text)
        frame_layout.addWidget(frame_drop_box)

        # Project Types Area here
        project_type_layout = QtWidgets.QHBoxLayout()
        project_types_text = QtWidgets.QLabel('Project Types')
        project_types_text.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        project_types_drop_box = QtWidgets.QComboBox()
        project_types_drop_box.addItem("Fitting", self.toggle_fit)
        project_types_drop_box.addItem("Simulation", self.toggle_sim)
        project_type_layout.addWidget(project_types_text)
        project_type_layout.addWidget(project_types_drop_box)

        # Setup master Layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(project_layout)
        main_layout.addLayout(basis_layout)
        main_layout.addLayout(frame_layout)
        main_layout.addLayout(project_type_layout)

        self.setup_box_one.setLayout(main_layout)

    def toggle_fit(self):
        fit = Fitting()
        fit.show()

    def toggle_sim(self):
        sim = Simulation()
        sim.show()


class Fitting(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(Fitting, self).__init__(parent)
        self.fitting_setup()
        self.fitting_layout()

        # Simulation

    def fitting_layout(self):
        # pwa = QtWidgets.QLabel(self)
        # pwa.setPixmap(QtGui.QPixmap('pypwa.png'))
        information_layout = QtWidgets.QVBoxLayout()
        fitting_title = QtWidgets.QLabel("Fitting")
        fitting_title.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        information_layout.addWidget(fitting_title)
        # information_layout.addWidget(pwa)
        information_layout.addWidget(self.setup_box_two)
        self.setLayout(information_layout)

    def fitting_setup(self):
        self.setup_box_two = QtWidgets.QGroupBox()

        # Keyfiles
        keyfiles_layout = QtWidgets.QHBoxLayout()
        keyfiles_name_label = QtWidgets.QLabel('Keyfiles')
        keyfiles_name_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        keyfiles_folder = QtWidgets.QLineEdit()
        keyfiles_layout.addWidget(keyfiles_name_label)
        keyfiles_layout.addWidget(keyfiles_folder)

        # RAW
        fitting_raw_layout = QtWidgets.QHBoxLayout()
        fitting_raw_label = QtWidgets.QLabel('Raw:')
        fitting_raw_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        fitting_raw_files = QtWidgets.QLineEdit()
        fitting_raw_layout.addWidget(fitting_raw_label)
        fitting_raw_layout.addWidget(fitting_raw_files)

        # Data
        fitting_data_layout = QtWidgets.QHBoxLayout()
        fitting_data_label = QtWidgets.QLabel('Data:')
        fitting_data_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        fitting_data_file = QtWidgets.QLineEdit()
        fitting_data_layout.addWidget(fitting_data_label)
        fitting_data_layout.addWidget(fitting_data_file)

        # HCCMC

        # Minuit / Nestle
        minuit_nestle_layout = QtWidgets.QHBoxLayout()
        minuit_nestle_label = QtWidgets.QLabel("Minuit/Nestle:")
        minuit_nestle_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))

        # Setup master Layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(keyfiles_layout)
        main_layout.addLayout(fitting_raw_layout)

        self.setup_box_two.setLayout(main_layout)


class Simulation(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(Simulation, self).__init__(parent)
        self.simulation_setup()
        self.simulation_layout()

    # Simulation
    def simulation_layout(self):
        information_V_layout = QtWidgets.QVBoxLayout()
        simulation_title = QtWidgets.QLabel("Simulation")
        simulation_title.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Black))
        information_V_layout.addWidget(simulation_title)
        information_V_layout.addWidget(self.setup_box_two)
        self.setLayout(information_V_layout)

    def simulation_setup(self):
        self.setup_box_two = QtWidgets.QGroupBox()

        # Keyfiles
        keyfiles_name_layout = QtWidgets.QHBoxLayout()
        keyfiles_name_label = QtWidgets.QLabel('Keyfiles:')
        keyfiles_name_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        keyfiles_folders = QtWidgets.QLineEdit()
        keyfiles_name_layout.addWidget(keyfiles_name_label)
        keyfiles_name_layout.addWidget(keyfiles_folders)

        # RAW
        simulation_raw_layout = QtWidgets.QHBoxLayout()
        simulation_raw_label = QtWidgets.QLabel('Raw:')
        simulation_raw_label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        simulation_raw_files = QtWidgets.QLineEdit()
        simulation_raw_layout.addWidget(simulation_raw_label)
        simulation_raw_layout.addWidget(simulation_raw_files)

        # Use VS
        simulation_vs_layout = QtWidgets.QHBoxLayout()
        simulation_vs = QtWidgets.QLabel('Use VS:')  # Check Box would go beside it
        simulation_vs.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        simulation_vs_checkbox = QtWidgets.QCheckBox()
        simulation_vs_layout.addWidget(simulation_vs)
        simulation_vs_layout.addWidget(simulation_vs_checkbox)

        # VS Location
        simulation_vs_location_layout = QtWidgets.QHBoxLayout()
        simulation_vs_location = QtWidgets.QLabel('VS Location:')
        simulation_vs_location.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Black))
        simulation_vs_location_dict = QtWidgets.QLineEdit()
        simulation_vs_location_layout.addWidget(simulation_vs_location)
        simulation_vs_location_layout.addWidget(simulation_vs_location_dict)

        # Setup master Layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(keyfiles_name_layout)
        main_layout.addLayout(simulation_raw_layout)
        main_layout.addLayout(simulation_vs_layout)
        main_layout.addLayout(simulation_vs_location_layout)

        self.setup_box_two.setLayout(main_layout)

    #def VS_Checkbox(self):
     #   if state == QtCore.Qt.Checked:
     #       print('Checked')
     #   else:
     #       print('Unchecked')


class BinSettings(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(BinSettings, self).__init__(parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('pypwaicon1.png'))
    gui = MagicWizard()
    gui.show()
    app.exec_()