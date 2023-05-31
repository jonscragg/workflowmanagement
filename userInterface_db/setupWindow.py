from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt

class SetupWindow(QMainWindow):
    def __init__(self, router):
        super().__init__()
        self.router = router

        # Set the window title
        self.setWindowTitle("Setup")
        # Set the fixed window size
        self.setFixedSize(QSize(800, 500))
        
        # Create a vertical layout for the main window
        page_layout = QVBoxLayout()

        # Create a label widget for the UI
        UI_label = QLabel("Setup")
        UI_label.setStyleSheet("font-weight: bold")

        # Align the UI label to the left
        UI_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        page_layout.addWidget(UI_label)

        # Create a widget for the main UI
        UIwidget = QWidget()
        UIwidget.setLayout(page_layout)
        self.setCentralWidget(UIwidget)
        
        # Create the setup menu
        setup_widget = self.setup_menu()
        page_layout.addWidget(setup_widget)

    def setup_menu(self):
        widget = QWidget()
        
        # Create a "Steps" button for navigating to the steps window
        stepsButton = QPushButton("Steps")
        stepsButton.pressed.connect(lambda: self.router.goto("steps"))
        
        # Set the style sheet for the "Steps" button
        stepsButton.setStyleSheet("""
        QPushButton {  
            background-color: #F7D060;
            color: black;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        """)
        
        # Set the geometry (position and size) of the "Steps" button
        stepsButton.setGeometry(160, 150, 200, 60)
        stepsButton.setParent(self)

        # Create a "Back to Home" button for navigating back to the home window
        backButton = QPushButton("Back to Home")
        backButton.pressed.connect(lambda: self.router.goto(""))

        # Set the style sheet for the "Back to Home" button
        backButton.setStyleSheet("""
        QPushButton {  
            background-color: #F7D060;
            color: black;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        """)
        
        # Set the geometry (position and size) of the "Back to Home" button
        backButton.setGeometry(580, 10, 200, 50)
        backButton.setParent(self)

        return widget