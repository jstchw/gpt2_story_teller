import eel


@eel.expose
def cycle_image():
    print("test")


class Interface:

    def __init__(self):
        eel.init('www')
        eel.start('index.html', size=(1024, 768))
