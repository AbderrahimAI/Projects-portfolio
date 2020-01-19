#This class displays the startpage from where different algorithms can be chosen
import tkinter as tk
from tkinter import ttk
import config
import ressource

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Basic delaration of the elements on the startpage
        self.controller = controller
        self.controller.geometry("500x300")
        self.controller.title("Algorithmes Animes")
        label = ttk.Label(self, text="Menu Principal", font=controller.title_font)
        label.place(x=250, y=40, anchor="center")

        quicksortButton = ttk.Button(self, text="Quicksort Algorithm", command=self.openQuicksortdisplay, style='my.TButton')
        insertsortButton = ttk.Button(self, text="Insertionsort Algorithm", command=self.openInsertsortdisplay, style='my.TButton')
        bubblesortButton = ttk.Button(self, text="Bubblesort Algorithm", command=self.openBubblesortdisplay, style='my.TButton')
        quicksortButton.place(x=250, y=85, anchor="center")
        insertsortButton.place(x=250, y=118, anchor="center")
        bubblesortButton.place(x=250, y=151, anchor="center")

    #Methods that open the display page with the respective algorithm
    #the information texts are changed to match the selected algorithm
    def openQuicksortdisplay(self):
        config.algnum = 0
        self.controller.title("Quicksort")
        self.controller.state('zoomed')
        self.controller.show_frame("Display")
        self.controller.frames["Display"].messageLeft.config(text=ressource.quicksortExplain)
        self.controller.frames["Display"].messageRight.config(text=ressource.quicksortPseudo)

    def openInsertsortdisplay(self):
        config.algnum = 1
        self.controller.title("Insertionsort")
        self.controller.state('zoomed')
        self.controller.show_frame("Display")
        self.controller.frames["Display"].messageLeft.config(text=ressource.insertsortExplain)
        self.controller.frames["Display"].messageRight.config(text=ressource.insertsortPseudo)

    def openBubblesortdisplay(self):
        config.algnum = 2
        self.controller.title("Bubblesort")
        self.controller.state('zoomed')
        self.controller.show_frame("Display")
        #TODO Update Texts here
        self.controller.frames["Display"].messageLeft.config(text=ressource.bubblesortExplain)
        self.controller.frames["Display"].messageRight.config(text=ressource.bubblesortPseudo)