import pywinauto
import pyautogui
from pywinauto.application import Application
import pywinauto.findwindows as fw
import time
from pathlib import Path
import automation_helper_functions as ahf


def test_automation():
    time.sleep(2)
    app = Application(backend="uia").start("notepad.exe")
    # app.window().wait('visible')
    # app.UntitledNotepad.menu_select("Help->About Notepad")
    # app.window().type_keys("hello, hi")
    # app.WindowSpecification.wait('enabled')
    time.sleep(2)
    # for x in pyautogui.getAllWindows():
    #     if str(x).__contains__("Notepad"):
    #         break
    #     else:
    #         raise Exception("Window did not open or cannot focus on the it.")
    app = Application().connect(title="Untitled - Notepad")
    # spec = app.window(best_match="Notepad")
    # spec.set_focus()
    app.Notepad.type_keys("hello, this is a test sentence.")
    app.Notepad.move_window(0, 0)
    app.Notepad.maximize()
    pyautogui.typewrite("hello, this is a test sentence.")
    time.sleep(1)
    app.Notepad.set_focus()
    # ss = pyautogui.screenshot("screenshoot.png", region=(0, 0, screen_dimensions[0]/2, screen_dimensions[1]/2))
    # print(pyautogui.locateOnScreen(Path("data/imagetofind.png")))

    # time.sleep(2)
    # ss.save("/images/screenshot.jpg")

    pyautogui.typewrite(["alt"])
    pyautogui.typewrite(["F"])
    pyautogui.typewrite(["X"])
    pyautogui.typewrite(["alt"])
    pyautogui.typewrite(["N"])
    time.sleep(2)
    # take a screenshot


def automation():
    # check if logged into eklipse
    eklipse_instance = ahf.focus_on_eklipse()
    logged_in_bool = ahf.check_if_logged_in(eklipse_instance)

    # ask user if the target conditioning is complete

    # if yes, start the test else cancel
    # check the status of the machine
    # if the status for "recipe running" is not white and all others are white
    # else cancel and show the status to the user
    # Assign a run ID to the process
    # Go to operations tab
    # go to vacuum tab
    # read the value of PC pressure
    # Activate the "LL vent" button
    # wait till it loads
    # check the status repeatedly
    # o	If “Recipe Running” is blue: continue waiting
    # o	If “Error/Abort” is red: notify user of error and cancel
    # o	If “Interlock/warning” is yellow: notify user of this and cancel
    # o	If “Normal Operation” is green (after some time): continue to next step
    # o	Timeout after 30 mins – notify user and cancel.
    # Ask the user to enter the substrate number
    # Ask the user to load the substract and press ok
    # State ready to run process and press OK to proceed
    # Click the "Run Recipe" button
    # Select the recipe from the list
    # Click the "Run Recipe" button
    # Set the setpoint values according to the recipe
    # Click the "continue load" button
    # Wait till the recipe is complete
    # Check the status repeatedly
    # o	If blue: continue waiting
    # o	If red: notify user of error and cancel
    # o	If green (after some time): continue to next step
    # o	Timeout after 90 mins – notify user and cancel.
    # Wait for 10 seconds and then go to Vacuum tab and capture the value of pressure
    # Send instruction to user: "Sample finished - press OK to unload"
    # Click on the "LL vent" button
    # Check the status repeatedly
    # o	If “Recipe Running” is blue: continue waiting
    # o	If red: notify user of error and cancel
    # o	If green (after some time): continue to next step
    # o	Timeout after 30 mins – notify user and cancel.
    # Instruct the user to remove the sample
    # Close LL and confirm
    # User input: if okay, continue, else cancel
    # activate the LL pump button
    # "Run completed: save data?" User input: if okay, continue, else cancel
    # Process and store run data
    # Click on mark as done
    # Remove the experiment from the list of waiting runs


if __name__ == "__main__":
    test_automation()
