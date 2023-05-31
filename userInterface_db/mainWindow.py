from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self, router):
        super().__init__()

        self.router = router

        # Set the window title
        self.setWindowTitle("Database controller")
        # Set the fixed window size
        self.setFixedSize(QSize(800, 500))
        
        # Create a vertical layout for the main window
        page_layout = QVBoxLayout()

        # Create a label widget for the UI
        UI_label = QLabel("Workflow Control - Home")
        UI_label.setStyleSheet("font-weight: bold")

        # Align the UI label to the left
        UI_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        page_layout.addWidget(UI_label)

        # Create a widget for the main UI
        UIwidget = QWidget()
        UIwidget.setLayout(page_layout)
        self.setCentralWidget(UIwidget)
        
        # Create the main menu
        main_menu_widget = self.main_menu()
        page_layout.addWidget(main_menu_widget)
        

    def main_menu(self):
        widget = QWidget()

        # Create a button for operations
        opButton = QPushButton("Operations")
        # Connect the button to a lambda function to handle the "op" route
        opButton.pressed.connect(lambda: self.router.goto("op"))

        # Create a button for the database
        dbButton = QPushButton("Database")

        # Create a button for setup
        setupButton = QPushButton("Setup")
        # Connect the button to a lambda function to handle the "setup" route
        setupButton.pressed.connect(lambda: self.router.goto("setup"))

        # Set the style sheet for the operations button
        opButton.setStyleSheet("""
        QPushButton {  
            background-color: #F7D060;
            color: black;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        """)
        
        # Set the geometry (position and size) of the operations button
        opButton.setGeometry(160, 150, 200, 60)
        opButton.setParent(self)

        # Set the style sheet for the database button
        dbButton.setStyleSheet("""
        QPushButton {  
            background-color: #F7D060;
            color: black;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        """)
        
        # Set the geometry (position and size) of the database button
        dbButton.setGeometry(450, 150, 200, 60)
        dbButton.setParent(self)

        # Set the style sheet for the setup button
        setupButton.setStyleSheet("""
        QPushButton {  
            background-color: #F7D060;
            color: black;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        """)
        
        # Set the geometry (position and size) of the setup button
        setupButton.setGeometry(160, 250, 200, 60)
        setupButton.setParent(self)
 
        return widget