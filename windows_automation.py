import os
import webbrowser
from voice import speak

def open_application(app_name):
    try:
        if app_name == "chrome":
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif app_name == "calculator":
            os.system("calc")
        elif app_name == "music":
            os.startfile("C:\\Path\\To\\Your\\Music\\Player.exe")
        elif app_name == "alarm":
            os.startfile("C:\\Path\\To\\Your\\Alarm\\App.exe")
        elif app_name == "notepad":
            os.system("notepad")
        elif app_name == "word":
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        elif app_name == "excel":
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        elif app_name == "powerpoint":
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
        elif app_name == "paint":
            os.system("mspaint")
        elif app_name == "cmd":
            os.system("cmd")
        elif app_name.startswith("website "):
            url = app_name.replace("website ", "")
            webbrowser.open(url)
        else:
            speak("Sorry, I can't open that application.")
    except Exception as e:
        speak(f"An error occurred while trying to open {app_name}: {str(e)}")