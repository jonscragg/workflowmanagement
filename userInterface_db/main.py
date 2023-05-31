#Run this file to execute the program 

import sys

from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets

from router import Router

def main():
    # Create an instance of the QApplication
    app = QApplication(sys.argv)

    # Create an instance of the Router class to handle routing
    Router()

    # Start the application event loop
    app.exec()

# Check if the current module is the main module
if __name__ == "__main__":
    # Call the main function to start the application
    main()