from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt

class OperationsWindow(QMainWindow):
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
        
        # Create the operations menu
        operations_menu_widget = self.operations_menu()
        page_layout.addWidget(operations_menu_widget)

    def operations_menu(self):
        widget = QWidget()

        #create back button
        backButton = QPushButton("Back to Home")
        backButton.pressed.connect(lambda: self.router.goto(""))

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
        # Set the size and parent for the button
        backButton.setGeometry(580,10,200,50)
        backButton.setParent(self)
        # Create buttons for different operations
        opcampButton = QPushButton("Open Campaign")
        addButton = QPushButton("Add data")
        newcampButton = QPushButton("New Campaign")

        # Set the style sheet for the "Open Campaign" button
        opcampButton.setStyleSheet("""
        QPushButton {  
            background-color: #F7D060;
            color: black;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        """)
        
        # Set the geometry (position and size) of the "Open Campaign" button
        opcampButton.setGeometry(160, 150, 200, 60)
        opcampButton.setParent(self)

        # Set the style sheet for the "Add data" button
        addButton.setStyleSheet("""
        QPushButton {  
            background-color: #F7D060;
            color: black;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        """)
        
        # Set the geometry (position and size) of the "Add data" button
        addButton.setGeometry(450, 150, 200, 60)
        addButton.setParent(self)

        # Set the style sheet for the "New Campaign" button
        newcampButton.setStyleSheet("""
        QPushButton {  
            background-color: #F7D060;
            color: black;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        """)
        
        # Set the geometry (position and size) of the "New Campaign" button
        newcampButton.setGeometry(160, 250, 200, 60)
        newcampButton.setParent(self)

        return widget