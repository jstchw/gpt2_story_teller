import tkinter as tk


class Interface:

    def __init__(self, x_size, y_size, title):
        self.x_size = x_size
        self.y_size = y_size
        self.title = title
        self.window = tk.Tk()
        self.window.resizable(width=tk.FALSE, height=tk.FALSE)

        # Left frame
        self.leftFrame = tk.Frame(self.window, bg='red')
        self.leftFrame.pack_propagate(0)
        self.leftFrame.pack(fill='both', side='left', expand='True')

        # Right frame
        self.rightFrame = tk.Frame(self.window, bg='green')
        self.rightFrame.pack_propagate(0)
        self.rightFrame.pack(fill='both', side='right', expand='True')

        # Buttons
        self.button_next = tk.Button(self.rightFrame, text='Next', width='20', relief=tk.GROOVE)
        self.button_prev = tk.Button(self.leftFrame, text='Previous', width='20', relief=tk.GROOVE)
        self.button_like = tk.Button(self.rightFrame, text='Like', width='10', relief=tk.GROOVE)

        self.button_next.pack(side=tk.BOTTOM, pady=20)
        self.button_prev.pack(side=tk.BOTTOM, pady=20)

        # Canvas and image
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack()

        img = tk.PhotoImage(file='img/test_img.gif')
        self.canvas.create_image((100, 100), image=img)

        # Draw window
        self.create_window()

    def create_window(self):
        self.window.geometry(str(self.x_size) + 'x' + str(self.y_size))
        self.window.title(self.title)

        self.window.mainloop()
