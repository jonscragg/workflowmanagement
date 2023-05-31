from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets

from mainWindow import MainWindow
from setupWindow import SetupWindow
from stepWindow import StepsWindow
from operationsWindow import OperationsWindow
from testStepWindow import TestStepWindow

class Router():
    def __init__(self):
        # Create a QStackedWidget to hold the different windows
        self.widget = QtWidgets.QStackedWidget()

        # Create an instance of the MainWindow and add it to the QStackedWidget
        w_dbWindow = MainWindow(self)
        self.widget.addWidget(w_dbWindow)

        # Show the QStackedWidget
        self.widget.show()

    def goto(self, window, stepID=None):
        # Create a new window based on the given window parameter
        w = MainWindow(self)
        if window == "setup":
            w = SetupWindow(self)
        elif window == "op":
            w = OperationsWindow(self)
        elif window == "steps":
            w = StepsWindow(self)
        elif window == "testStepWindow":
            # Check if stepID is a string, otherwise return
            if not isinstance(stepID, str):
                return
            w = TestStepWindow(self, stepID)

        # Add the new window to the QStackedWidget
        self.widget.addWidget(w)
        # Set the current index of the QStackedWidget to the new window
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
