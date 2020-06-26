from tkinter import *

class View(Tk):
    def __init__(self):
        Tk.__init__(self)

    def _quit(self):
        self.destroy()
