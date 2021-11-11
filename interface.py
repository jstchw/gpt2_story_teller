import tkinter as tk


class Interface:

    def __init__(self, x_size, y_size, title):
        self.x_size = x_size
        self.y_size = y_size
        self.title = title
        self.window = tk.Tk()
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)

        # Frames
        self.leftFrame = tk.Frame(self.window, bg='red')
        self.leftFrame.pack_propagate(0)
        self.leftFrame.pack(fill='both', side='left', expand='True')

        self.rightFrame = tk.Frame(self.window, bg='green')
        self.rightFrame.pack_propagate(0)
        self.rightFrame.pack(fill='both', side='right', expand='True')

        # Buttons
        self.button_next = tk.Button(self.rightFrame, text='Next', width='20', relief=tk.GROOVE)
        self.button_prev = tk.Button(self.leftFrame, text='Previous', width='20', relief=tk.GROOVE)
        self.button_like = tk.Button(self.rightFrame, text='Like', width='10', relief=tk.GROOVE)

        self.button_next.pack(side=tk.BOTTOM, pady=20)
        self.button_prev.pack(side=tk.BOTTOM, pady=20)

        self.create_window()

    def create_window(self):
        self.window.geometry(str(self.x_size) + 'x' + str(self.y_size))
        self.window.title(self.title)

        self.window.mainloop()
