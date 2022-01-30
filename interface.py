import eel


class Interface:

    def __init__(self):
        eel.browsers.set_path('electron', '/Applications/Electron.app/Contents/MacOS/Electron')

        eel.init('www')
        eel.start(mode='electron', size=(550, 570))
