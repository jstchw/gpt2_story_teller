import eel
import json
import os
import glob

app_version = 1.0


# Function to save reactions in a JSON file
@eel.expose
def react(post_id, value, topic, post_text):
    with open('base/reaction.json', 'r+') as json_file:
        reaction_file = json.load(json_file)
        array = {
            "appVer": app_version,
            "id": reaction_file['posts'][-1]['id'] + 1,
            "postID": post_id,
            "postReaction": value,
            "postText": post_text,
            "topic": topic
        }
        reaction_file['posts'].append(array)
        json_file.seek(0)
        json.dump(reaction_file, json_file, indent=4, sort_keys=True)


@eel.expose
def unreact(post_id):
    with open('base/reaction.json', 'r+') as json_file:
        reaction_file = json.load(json_file)
        for i in reversed(range(len(reaction_file['posts']))):
            if reaction_file['posts'][i]["postID"] == post_id:
                # This just doesn't work
                print(reaction_file['posts'][i])
                # reaction_file['posts'].pop(i)
                del reaction_file['posts'][i]
                json_file.seek(0)
                json.dump(reaction_file, json_file, indent=4, sort_keys=True)
                json_file.truncate()
                # reaction_file['posts'].remove(i-1)
                break


# Function to retrieve JSON string from the file and use it
@eel.expose
def get_settings(filename):
    with open(filename) as json_file:
        settings = json.load(json_file)
        return settings


# Function to set any setting to a JSON file
@eel.expose
def set_settings(key, value):
    settings = get_settings('base/settings.json')
    settings[key] = value

    with open('base/settings.json', 'w') as json_file:
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
