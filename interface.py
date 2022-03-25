import eel
import json
import os
import glob


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


@eel.expose
def count_files(path):
    # return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    return len(glob.glob1(path, "*.jpg"))


class Interface:

    def __init__(self):
        self.width = 550
        self.height = 570
        # For Mac
        # eel.browsers.set_path('electron', '/Applications/Electron.app/Contents/MacOS/Electron')
        # For Windows
        eel.browsers.set_path('electron', r'C:/Users/bobr7/AppData/Roaming/npm/node_modules/electron/dist/electron.exe')
        eel.init('www')

    def create_window(self):
        eel.start(mode='electron', size=(self.width, self.height))
