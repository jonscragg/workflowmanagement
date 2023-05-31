# solar-cell

**Installation Information**

- For exporting the program in an _.exe_ format, using the pyinstaller library. Pip install pyinstaller and then find the place where the python site-packages library is and put it in the SYSTEM environmental variables in PATH/Path. This should not be in the USER environmental variables.
- To setup mongoDB, make an account if does not exist already. Install MongoDB Compass for easy management of database. Install MongoDB server from (https://www.mongodb.com/try/download/community) and follow the installation wizard.
- Run the experiment executer by running ht main.py file.
- To run the UI for database management, run the main.py in the userInterface_db folder.

**Developers in this project:**

- Aishwarya Gupta (aishe.gupta@gmail.com)
- Paarth Sanhotra (paarthsanhotra@gmail.com)

**Libraries and versions used to develop this software:**

- Python 3.10.4
- PyQt6 6.5.0
- pywinauto 0.6.8
- pyinstaller 5.10.1
- Windows 11 (For automation and the experiment executer UI)
- pyautoGUI 0.9.53 (used for the screenshot function)
- VS Code (with copilot extension)
- GitHub (With Github Desktop)
- MacOS for the UI for database management

**Some tips while coding for automating along with Experiment Executer UI.**

- VS Code is used for development
- Use the _inspect.exe_ tool to identify the elements on the page.
- Use the `eklipse_instance.window(window_name).print_control_identifiers()` to identify the functions that can be used on the element. Will work with an object of the Application class.
- Use `time.sleep()` to wait for the page to load if you are not able to dynamically wait for the element to load.
- For checking the status of the machine, we were going to use the built in screenshot function and match it to a pre-stored image of how the status indicator was going to look like. Since the status indicator was on the top left side of the window, one can take a screenshot of the top left half and run a loop to check the status of the machine. This way might be a bit slow and prone to failure but it is a good way to start. We can also monitor a specific property of the status indicator using the _inspect.exe_ tool but since there are quite a few combinations, its challenging to find which property of the UI element is responsible for the status indicator for what status.
- For checking the status of the mahcine, there is a solution which was not tested. While using the locate_on_screen function by PyWinAuto, percentage of confidence can be set. This is helpful as if the status indicator is not in the same position, the program can still identify the status indicator and move on.
- The `test()` and `test_2()` functions were created to remove some code from the `init()` function of the `experimentwindow()` class and make the UI elements appear in a grouped iteration. If all the code is put into the `init()` function, all the UI functions appear at the same time which is not ideal. All the steps mentioned for executing the experiment must come one by one on the UI. If the software is waiting for a UI element to appear, it should show a loading message for the user.
- For the ease of coding, we had mentioned all the steps for automating the experiment in the automation.py file. The flow is also mentioned in the .pptx and .docx file which was shared by Jonathan Staaf Scragg.
- Preferably test the functions on the BEA software in the lab before finalizing.
- The UI is very bland and not very user friendly. It would be great if the UI can be made more user friendly and more appealing to the user. The UI theme from the other database application can be used for this UI as well.
- In the `get_data.py` file there is a validation function which checks each and every experiment in the experiments.csv and validates it according to the `recipes.csv` file. It checks if the experiment has the same steps as mentioned in the recipes file. If not, it will not show that particular experiment on the UI. New functionality can be implemented which shows the user which step is missing from which experiment.
- For the backend parameter in the window class, `win32` is for 32-bit program like the one we are dealing with. `uia` is for 64-bit programs. If the program is not working, try changing the backend.
- Try making the automation as robust as possible by showing the right error messages to the user and using error handling to keep the program running.
- Experiment with the `start_eklipse()` and `focus_on_eklipse()` functions. The first one does not start the program but it just shifts the focus to an already running instance of the program. Hence make sure to run the program before running the automation software and clicking on `start eklipse`.
- Develop functionality to maximize the eklipse window. When it is not full screen, the UI elements are not visible to the automation software.
- Avoid using UI element coordinates to interact with the UI elements. They can tend to be unstable and can change with different screen resolutions. Use the `child_window()` function to interact with the UI elements.
- To fetch the name of a UI element, you can use the UI_element.element_info.name parameter. This will return the name of the UI element which is being interacted with.
- The data folder has all the data one needs to deal with while working with this software.
  - column_headings is a list of all the column headings used in the experiments along with their datatypes
  - experiments.csv is the file which contains all the experiments which are to be executed
  - recipes.csv is the file which contains all the steps for the experiment
  - images which will be used to compare with the screenshot of the status indicator

**Some tips while coding for the database user interface.**

- To run the program run the `main.py` file.
- In the `db.py` file the mongoDB connection is established, include your own connection string there.
- The `mainWindow.py` file is the main window that pops up when running the code.
- The `operationsWindow.py` is not done yet but I have started to style the page.
- The `router.py` manages the navigation between different windows in a application using a QStackedWidget. It allows the user to switch between windows by calling the `goto()` method and specifying the desired window name.
- The `setupWindow.py` only includes `step` button right now and is just a intermediary between other pages.
- The `stepWindow.py` provides a graphical interface to display and interact with step data stored in a MongoDB collection, allowing users to view, select, and navigate to different stepIDs.
- The `testStepWindow.py` class represents a window where users can test a specific step. It allows users to input data, upload it to a CSV file, and navigate back to the `stepWindow.py` window. The input fields and data fetching are dynamically generated based on the selected step ID.
