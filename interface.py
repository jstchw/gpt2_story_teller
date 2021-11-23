import eel


class Interface:

    def __init__(self):
        eel.init('www')
        eel.start('index.html', size=(1024, 768))
