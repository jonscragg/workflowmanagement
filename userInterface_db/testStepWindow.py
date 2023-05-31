import uuid
import csv
from csv import writer
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt

# Importing the DB class from the db module
from db import DB

class TestStepWindow(QMainWindow):
    stepId = ""
    def __init__(self, router, incomingStepID):
        super().__init__()
        self.router = router
        self.db = DB()
        self.step = self.db.client["Data"]["Step"]
        self.recipe = self.db.client["Data"]["Recipe"]

        self.setWindowTitle("Test Step")
        # Window size
        self.setFixedSize(QSize(800, 500))
        page_layout = QVBoxLayout()

        UI_label = QLabel("Test Step")
        UI_label.setStyleSheet("font-weight: bold")

        UI_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        page_layout.addWidget(UI_label)

        UIwidget = QWidget()
        UIwidget.setLayout(page_layout)
        self.setCentralWidget(UIwidget)

        # Retrieve the incomingStepID
        stepID = incomingStepID
        print(stepID)

        # Create the testStep_widget
        testStep_widget = self.testWindow(incomingStepID)
        page_layout.addWidget(testStep_widget)

    def uploadData(self):
        document = {}
        for field_name, input_field in self.input_fields.items():
            if (field_name == "StepID"):
                value = input_field
            else:
                value = input_field.text()
            # Check if the value is not blank or contains only whitespace
            if value.strip():  
                document[field_name] = value
        
        # Generate and add the "setpointID" field
        document["setpointID"] = str(uuid.uuid4())

        # Insert the document into the collection if there are non-blank values
        if document:
            with open('test.csv', 'a', newline='') as file_object:
                writer = csv.writer(file_object)

                #if file_object.tell() == 0:
                header_row = [f"{key}={value}" for key, value in document.items()]
                writer.writerow(header_row)
                #writer.writerow(document.values())

        variable_names_str = ",".join([f"{key}={value}" for key, value in document.items()])
        print(variable_names_str)

        self.router.goto("steps")

    def testWindow(self, incomingStepID):
        widget = QWidget()
        layout = QVBoxLayout()
        self.input_fields = {"StepID": incomingStepID} 

        backButton = QPushButton("Back to Steps")
        backButton.pressed.connect(lambda: self.router.goto("steps"))

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

        selectedStepID = QLabel(("Step ID: " + incomingStepID))
        selectedStepID.setGeometry(14,40,90,30)
        selectedStepID.setStyleSheet("""
        background-color: #FFF9B0
        """)
        selectedStepID.setParent(self)
        print(selectedStepID)

        # List with Variables
        inputLayout = QVBoxLayout()

        step_fetched = self.step.find_one({"Step_ID": incomingStepID})
        recipe_fetched = self.recipe.find_one({"RecipeID": step_fetched["RecipeID"]})

        for field in recipe_fetched:
            if (field == "_id" or field == "RecipeName" or field == "RecipeID"):
                continue
        
            hbox = QHBoxLayout()

            label = QLabel(field)
            input_button = QLineEdit()
            # Set maximum width for input button
            input_button.setMaximumWidth(300)  

            hbox.addWidget(label, alignment=Qt.AlignmentFlag.AlignLeft)
            # Add stretchable space
            hbox.addStretch(1)  
            hbox.addWidget(input_button, alignment=Qt.AlignmentFlag.AlignRight)
            hbox.addStretch(10)
            inputLayout.addLayout(hbox)
            self.input_fields[field] = input_button
    
        # Add a stretchable space to center-align the content vertically
        layout.addStretch(1)  
        layout.addLayout(inputLayout)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addStretch(4)
        widget.setLayout(layout)
        
        uploadButton = QPushButton("Upload")
        uploadButton.setStyleSheet("""
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
        uploadButton.setGeometry(580,400,200,50)  
        uploadButton.setParent(self)  
        uploadButton.clicked.connect(lambda: self.uploadData())

        return widget