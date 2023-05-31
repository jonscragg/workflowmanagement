from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt

from db import DB

class StepsWindow(QMainWindow):
    rowIdx = -1

    def __init__(self, router):
        super().__init__()
        self.router = router
        self.db = DB()

        self.setWindowTitle("Steps")
        # Window size
        self.setFixedSize(QSize(800, 500))
        page_layout = QVBoxLayout()

        UI_label = QLabel("Steps")
        UI_label.setStyleSheet("font-weight: bold")

        UI_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        page_layout.addWidget(UI_label)

        UIwidget = QWidget()
        UIwidget.setLayout(page_layout)
        self.setCentralWidget(UIwidget)

        self.client = self.db.client["Data"]
        # Collection Name
        self.col = self.client["Step"]

        steps_widget = self.steps()
        page_layout.addWidget(steps_widget)

    def fill_table(self, table):
        cursor = self.col.find({})
        for i, document in enumerate(cursor):
            table.setRowCount(table.rowCount()+1)
            table.setItem(i,0, QTableWidgetItem(document["Step_ID"]))
            table.setItem(i,1, QTableWidgetItem(document["Type"]))
            table.setItem(i,2, QTableWidgetItem(document["Step_description"]))

    def select_next_step_id(self):
        # Retrieve all documents in collection -> sort descending with regards to Step_ID and choose the first document
        doc = self.col.find({}).sort("Step_ID",-1)[0]

        # Retrieve the number part of the step id by removing 's' with string manipulation
        num = doc["Step_ID"][1:]

        # Prepend 's' and increment the number by one and make the number on format 001 instead of 1.
        return "s" + str(int(num)+1).zfill(3)

    def getClickedCell(self, row, column):
        print('clicked!', row, column)
        self.rowIdx = row

    def steps(self):
        widget = QWidget()
        teststepButton = QPushButton("Test Step")

        teststepButton.setStyleSheet("""
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
        teststepButton.setGeometry(500,400,200,60)
        teststepButton.setParent(self)

        defButton = QPushButton("Define Sputter Step")
        defButton.setStyleSheet("""
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
        defButton.setGeometry(500,200,200,60)
        defButton.setParent(self)

        backButton = QPushButton("Back to Setup")
        backButton.pressed.connect(lambda: self.router.goto("setup"))

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

        # Scrollable table
        tableWidget = QTableWidget()
        # Row count
        tableWidget.setRowCount(0)  
        # Column count
        tableWidget.setColumnCount(3)  

        self.fill_table(tableWidget)

        # Table settings
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("StepID"))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Type"))
        tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Name"))
        tableWidget.setParent(self)
        tableWidget.setGeometry(70,70,300,200)
        tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        tableWidget.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        tableWidget.cellClicked.connect(self.getClickedCell)

        # Latest step label
        latest = self.select_next_step_id()
        latest_label = QLabel(latest, self)
        latest_label.setGeometry(510,100,40,30)
        latest_label.setStyleSheet("""
        background-color: #FFF9B0
        """)
        print(latest)

        # Scroll button
        s_type = QComboBox()
        s_type.addItem("Step Type")
        s_type.addItems(['Sputter'])
        s_type.setParent(self)
        s_type.setGeometry(500,120,200,60)

        teststepButton.pressed.connect(lambda: self.router.goto("testStepWindow", tableWidget.item(self.rowIdx,0).text() if self.rowIdx >= 0 else None))

        return widget