import eel
import json


# Function to retrieve JSON string from the file and use it
@eel.expose
def get_settings(filename):
    with open(filename) as json_file:
        settings = json.load(json_file)
        return settings


# Function to set any setting to a JSON file
@eel.expose
def set_settings(key, value):
    settings = get_settings('settings.json')
    settings[key] = value

    with open('settings.json', 'w') as json_file:
        json.dump(settings, json_file)


class Interface:

    def __init__(self):
        self.width = 550
        self.height = 570
        self.credentials = get_settings('credentials.json')
        eel.browsers.set_path('electron', '/Applications/Electron.app/Contents/MacOS/Electron')
        eel.init('www')

    def create_window(self):
        eel.start(mode='electron', size=(self.width, self.height))
