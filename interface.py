import eel
import json


# Function to retrieve JSON string from the file and use it
@eel.expose
def get_settings():
    with open('www/settings.json') as json_file:
        settings = json.load(json_file)
        return settings


# Function to set any setting to a JSON file
@eel.expose
def set_settings(key, value):
    settings = get_settings()
    settings[key] = value

    with open('www/settings.json', 'w') as json_file:
        json.dump(settings, json_file)


class Interface:

    def __init__(self):
        eel.browsers.set_path('electron', '/Applications/Electron.app/Contents/MacOS/Electron')

        eel.init('www')
        eel.start(mode='electron', size=(550, 570))
