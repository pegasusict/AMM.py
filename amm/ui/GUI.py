from UI import *
from tkinter import Tk, ttk


class GUI(UI):
    """
    :version:
    :author:
    """

    def menu(self):
        pass

    def view(self, view: str = "dash"):
        pass

    root = Tk()
    ttk.label(root, text="test").pack()
    root.mainloop()
