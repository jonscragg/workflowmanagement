"""
This main module is the entry point for the application. It contains the main window and the experiment window.
It has the steps for automation of the experiment. Some automation helper functions are also defined in this module.
Author: paarthsanhotra@gmail.com
Date: 29-05-2023
"""

import sys
import get_data
import automation_helper_functions as ahf
import automation
import time
from pywinauto import Desktop, Application, actionlogger, findbestmatch, findwindows

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    """This is the entry point for the application. It contains the main window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("BEA Controller")

        page_layout = QVBoxLayout()

        # Button to start Eklipse
        eklipse_button = QPushButton("Start Eklipse")
        eklipse_button.setCheckable(True)
        eklipse_button.clicked.connect(lambda: ahf.start_eklipse())
        page_layout.addWidget(eklipse_button)
        time.sleep(10)

        main_label = QLabel("List of Experiments")
        main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page_layout.addWidget(main_label)

        experiments = get_data.create_experiment()

        for experiment in zip(experiments, experiments.values()):
            experiment_layout = self.construct_experiment_layout(experiment)
            page_layout.addLayout(experiment_layout)

        mainwidget = QWidget()
        mainwidget.setLayout(page_layout)
        self.setCentralWidget(mainwidget)

    def show_state(self, s):
        """This function can be ignored. It was used to test the state of the checkbox."""
        print(s == Qt.CheckState)
        print(s)

    def construct_experiment_layout(self, experiment_name):
        """This function constructs the layout for each experiment. It reads
        the name of the experiment and creates a button to start the experiment."""
        layout = QHBoxLayout()
        #how to access data
        layout.addWidget(QLabel(experiment_name[1]["recipe_name"]))
        button = QPushButton("Start")
        delete_button = QPushButton("Delete")
        delete_button.hide()
        # TODO: Add functionality to delete button
        delete_button.clicked.connect(lambda: layout.deleteLater())
        layout.addWidget(delete_button)
        button.pressed.connect(lambda: self.perform_experiment(experiment_name[1]))
        layout.addWidget(button)
        return layout

    def perform_experiment(self, experiment):
        """This function is called when the user clicks on the start button for an
        experiment. It starts the experiment by constructing a new window."""
        self.new_window = ExperimentWindow(experiment)
        self.new_window.show()
        

class ExperimentWindow(QWidget):
    """This class creates a new window for each experiment. It contains the steps for
    automation of the experiment."""

    def __init__(self, experiment):
        super().__init__()

        self.setWindowTitle("My App")
        self.main_layout = QVBoxLayout()
        self.layout = QVBoxLayout()
        main_label = QLabel("Experiment: %s" % experiment["recipe_name"])
        main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(main_label)

        # Get Eklipse's window name
        self.window_name = ahf.get_eklipse_window_name()

        # user_response_layout = QHBoxLayout(self)

        # Ask user if the target conditioning is complete
        user_response_layout_1 = self.target_conditioning_user_response(
            "Wait till Eklipse starts and then login. Click 'yes' if/when the target conditioning complete?"
        )
        # user_response_layout.addLayout(user_response_layout_1)
        self.test_response = False
        self.layout.addLayout(user_response_layout_1)

        # Check the status of the machine
        # ss = pyautogui.screenshot("screenshoot.png", region=(0, 0, screen_dimensions[0]/2, screen_dimensions[1]/2))
        # print(pyautogui.locateOnScreen(Path("data/imagetofind.png")))
        # check = self.check_normal_operation(window_name) and self.check_recipe_running(window_name)
        # if not check:
        #     layout.addWidget(
        #         QLabel(
        #             "Machine is not running. Please start the experiment again after sometime."
        #         )
        #     )
        #     time.sleep(5)
        #     self.close()

        # Assign a RunId to the process

        # for parameter in experiment["parameters"]:
        #     parameter_layout = self.construct_parameter_layout(parameter)
        #     layout.addLayout(parameter_layout)
        next_button = QPushButton("Next")
        next_button.setCheckable(True)
        next_button.clicked.connect(lambda: self.clearLayout(self.layout))
        self.layout.addWidget(next_button)

        button = QPushButton("Mark as done")
        button.setCheckable(True)
        button.clicked.connect(self.close)
        button.clicked.connect(lambda: self.mark_as_done(experiment))

        
        self.layout.addWidget(button)
        self.main_layout.addLayout(self.layout)
        self.setLayout(self.main_layout)
        self.setLayout(self.main_layout)

    def test(self):
        """First function to lower the dependancy on the init function of the Experiment class."""
        window_name = self.window_name
        eklipse_instance = ahf.start_eklipse()
        # Go to operations tab
        self.go_to_operation_tab(window_name)
        time.sleep(2)

        # Go to the Vacuum tab
        self.go_to_vacuum_tab(window_name)
        time.sleep(2)

        # Read the pressure value
        self.pressure_value = self.get_pressure_value(window_name)
        time.sleep(2)

        # Display the pressure on the UI

        # Open the "LL Vent"
        self.open_LL_vent(window_name)
        time.sleep(2)

        # Display message to the user: "Load Lock Venting..." till the LL Vent dialog box opens

        # Check status of the machine repeatedly while this is loading

        # Ask the user to enter a substrate number
        substrate_layout = self.substrate_user_response()
        self.layout.addLayout(substrate_layout)

        # Ask the user to load the substrate and click "OK"
        load_substrate_layout = self.substrate_loaded_user_response()
        self.layout.addLayout(load_substrate_layout)

        # Ask the user if they are ready to start the experiment
        start_experiment_layout = self.start_after_load_substrate()
        self.layout.addLayout(start_experiment_layout)
        self.setLayout(self.layout)

    def test2(self):
        """Second function to lower the dependancy on the init function of the Experiment class."""
        window_name = self.window_name
        eklipse_instance = ahf.start_eklipse()
        # eklipse_instance.window(window_name).print_control_identifiers()
        # Click on the Run Recipe button
        self.click_run_recipe(window_name)
        time.sleep(2)

    def start_after_load_substrate(self):
        layout = QHBoxLayout()
        layout.addWidget(
            QLabel("Click 'Yes' when you're ready to start the experiment.")
        )
        button_yes = QPushButton("Yes")
        button_yes.clicked.connect(
            lambda: self.start_after_load_substrate_yes(button_yes)
        )
        button_no = QPushButton("No")
        button_no.clicked.connect(lambda: self.start_after_load_substrate_no(button_no))
        layout.addWidget(button_yes)
        layout.addWidget(button_no)
        return layout

    def start_after_load_substrate_yes(self, button):
        if button.clicked:
            self.test_response = True
            button.setEnabled(False)
            self.test2()

    def start_after_load_substrate_no(self, button):
        if button.clicked:
            self.test_response = False
            button.setEnabled(False)

            time.sleep(3)
            self.close()

    def substrate_user_response(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Enter a substrate number: "))
        self.substrate_user_input = QLineEdit(self)
        self.substrate_user_input.setPlaceholderText("Substrate number")
        layout.addWidget(self.substrate_user_input)
        substrate_button = QPushButton("Enter")
        substrate_button.setCheckable(True)
        substrate_button.clicked.connect(lambda: self.get_substrate_number(self))
        layout.addWidget(substrate_button)
        return layout

    def substrate_loaded_user_response(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Click 'Yes' when the substrate is loaded."))
        button_yes = QPushButton("Yes")
        button_yes.clicked.connect(lambda: self.substrate_response_yes(button_yes))
        button_no = QPushButton("No")
        button_no.clicked.connect(lambda: self.substrate_response_no(button_no))
        layout.addWidget(button_yes)
        layout.addWidget(button_no)
        return layout

    def substrate_response_yes(self, button):
        if button.clicked:
            self.test_response = True
            button.setEnabled(False)

    def substrate_response_no(self, button):
        if button.clicked:
            self.test_response = False
            button.setEnabled(False)

            time.sleep(3)
            self.close()

    def get_substrate_number(self):
        self.substrate_value = self.substrate_user_input.text()

    def click_run_recipe(self, window_name):
        eklipse_instance = Application().connect(title=window_name, backend="win32")
        eklipse_instance.window(title=window_name).child_window(
            title="Run Recipe", auto_id="Run Recipe"
        ).click_input()

    def open_LL_vent(self, window_name):
        eklipse_instance = Application().connect(title=window_name, backend="win32")
        eklipse_instance.window(title=window_name).child_window(
            title="LL Vent", auto_id="LL Vent"
        ).click_input()

    def check_normal_operation(self, window_name):
        eklipse_instance = Application().connect(title=window_name, backend="win32")
        return eklipse_instance.window(title=window_name).child_window(
            title="NormalOperation", auto_id="NormalOperationLabel"
        )

    def check_recipe_running(self, window_name):
        eklipse_instance = Application().connect(title=window_name, backend="win32")
        return eklipse_instance.window(title=window_name).child_window(
            title="RecipeRunning"
        )

    def go_to_vacuum_tab(self, window_name):
        eklipse_instance = Application().connect(title=window_name, backend="win32")
        eklipse_instance.window(title=window_name).child_window(
            title="Vacuum", auto_id="Vacuum"
        ).click_input()

    def go_to_operation_tab(self, window_name):
        eklipse_instance = Application().connect(title=window_name, backend="win32")
        eklipse_instance.window(title=window_name).child_window(
            title="Operation", auto_id="Operation"
        ).click_input()

    def get_pressure_value(self, window_name):
        eklipse_instance = Application().connect(title=window_name, backend="win32")
        pressure = eklipse_instance.window(title=window_name).child_window(
            auto_id="Label15"
        )
        return pressure.element_info.name

    #itarate through json file and find the experiment name
    #change the isDone value
    #save the json file
    def mark_as_done(self, experiments):
        for number in range(len(experiments)):
            if experiments[1]["recipe_name"] in experiments[number][0]:
                experiments["isDone"] = True
                with open("experiments.json", "w") as jsonFile:
                    json.dump(experiments, jsonFile)
                    jsonFile.close()
            else:
                print("Experiment not found")
            

    def construct_parameter_layout(self, parameter):
        """This function was used for testing purposes. The button triggered an automation
        script to start the notepad application. Does not seem to work anymore."""
        layout = QHBoxLayout()
        layout.addWidget(QLabel(parameter))
        button = QPushButton("Done")
        button.clicked.connect(lambda: button.setEnabled(False))
        # button.clicked.connect(lambda: self.clearLayout(layout))
        button.clicked.connect(lambda: automation.test_automation())
        layout.addWidget(button)
        return layout

    def target_conditioning_user_response(self, text):
        layout = QHBoxLayout()
        layout.addWidget(QLabel(text))
        button_yes = QPushButton("Yes")
        button_yes.clicked.connect(
            lambda: self.target_conditioning_response_yes(button_yes)
        )
        button_no = QPushButton("No")
        button_no.clicked.connect(
            lambda: self.target_conditioning_response_no(button_no)
        )
        layout.addWidget(button_yes)
        layout.addWidget(button_no)

        return layout

    def target_conditioning_response_yes(self, button):
        if button.clicked:
            self.test_response = True
            button.setEnabled(False)
            self.test()

    def target_conditioning_response_no(self, button):
        if button.clicked:
            self.test_response = False
            button.setEnabled(False)

            time.sleep(3)
            self.close()

    def clicked(self, s):
        """Prints the string s to the console."""
        print(s)

    def mark_as_done(self, experiment):
        """Designed to mark an experiment as done and then not show it on the list on the main UI. Not implemented yet."""
        experiment["isDone"] = True

    def clearLayout(self, layout):
        """Clears all the elements in a layout."""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())


if __name__ == "__main__":
    """Run the application."""
    # The commented code was used to write the contents of the console to
    # a file for debugging purposes
    # sys.stdout = open("logs.txt", "w")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    # sys.stdout.close()
