#Main file
import tkinter as tk
from tkinter import font as tkfont
from startpage import StartPage
from display import Display
from compare import Compare
import tkinter.font as tkFont
from tkinter import ttk

#Class implements the basic architecture of the app
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Declaration of fonts
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        s = ttk.Style()
        buttonFont = tkFont.Font(family='Arial', size=12)
        s.configure('my.TButton', font=buttonFont)

        self.restFont = tkFont.Font(family="Arial", size=12)
        s.configure("TMenubutton", font=self.restFont)

        # the container is where a bunch of frames are stacked
        # on top of each other, then the one to be visible
        # will be raised above the others

        container = tk.Frame(self)
        self.iconbitmap("icon.ico")
        container.grid(row=1, column=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Display, Compare):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        #Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()

