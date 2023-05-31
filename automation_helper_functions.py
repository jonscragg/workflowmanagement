"""

"""

from pywinauto.application import Application
from pywinauto import Desktop
import time
from pathlib import Path
import os


def get_all_open_windows():
    """Returns a list of all open windows titles"""
    windows = []
    windows.append([w.window_text() for w in Desktop(backend="win32").windows()])
    return windows[0]


def get_eklipse_window_name():
    """Returns the name of the eklipse window"""
    windows = get_all_open_windows()
    for window in windows:
        if "eklipse" in window.lower() and "host" not in window.lower():
            window_name = window
            break

    return window_name


def remove_zero_width_space(string):
    """Removes zero width space from a string"""
    return string.replace("\u200b", "")


def start_eklipse():
    """Starts the eklipse application"""
    eklipse_path = r"C:\\Program Files (x86)\\KJLC\\eKLipse\\eKlipse.exe"
    eklipse_instance = Application(backend="win32").start(eklipse_path)
    return eklipse_instance


def focus_on_eklipse(window_name):
    """Focuses on the eklipse window"""
    eklipse_instance = Application().connect(title=window_name, backend="win32")
    # eklipse_instance.SetFocus()
    eklipse_instance.window.maximize()
    return eklipse_instance


def check_if_logged_in(eklipse_instance):
    """Place holder for the function that checks if the user is logged in"""
    return True
