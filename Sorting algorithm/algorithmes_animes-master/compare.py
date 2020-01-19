#This class displays the startpage from where different algorithms can be chosen
import tkinter as tk
from tkinter import ttk
import config
import random
from quicksort import Quicksort
from insertionsort import Insertionsort
from bubblesort import Bubblesort

class Compare(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Declaration of the elements on the Page
        self.label = ttk.Label(self, text=config.algorithms[config.algnum]+ " vs " + config.algorithms[config.comparealg], font=controller.title_font)
        print(config.algnum)
        print(config.comparealg)
        self.label.grid(row=1, column=1, padx=5, pady=20)

        self.canvasWidth = 500
        self.canvasHeight = 286
        self.canvas1 = tk.Canvas(self, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas1.grid(row=2, column=1, padx=12, pady=20)
        self.canvas2 = tk.Canvas(self, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas2.grid(row=2, column=2, padx=5, pady=20)

        self.gridframe = tk.Frame(self)
        self.sortButton = ttk.Button(self.gridframe, text="Lancer", command=self.runAlgo, style='my.TButton')
        self.sortButton.grid(row=1, column=1, padx=10)
        self.generateButton = ttk.Button(self.gridframe, text="Nouvelles ", command= self.generateNew, style='my.TButton')
        self.generateButton.grid(row=1, column=2, padx=10)
        self.backButton = ttk.Button(self.gridframe, text="Retour", command=self.returnCommand, style='my.TButton')
        self.backButton.grid(row=1, column=3, padx=10)
        self.gridframe.grid(row=3, column=1, padx=10, pady=20, columnspan=2)

        config.A = [random.randrange(6, 101, 1) for _ in range(20)]
        config.copyA = config.A[:]

        self.draw()

    # Canvas draw
    def draw(self):
        if config.runvar==1:
            self.sortButton.config(state="disabled")
            self.generateButton.config(state="disabled")
            self.backButton.config(state="disabled")
        else:
            self.sortButton.config(state="normal")
            self.generateButton.config(state="normal")
            self.backButton.config(state="normal")
        text = config.algorithms[config.algnum] + " vs " + config.algorithms[config.comparealg]
        self.label.config(text=text)
        # clear the canvas
        self.canvas1.delete("all")
        self.canvas2.delete("all")
        # Give the canvas a white background
        self.canvas1.create_rectangle(0, 0, self.canvasWidth, self.canvasHeight, width=0, fill="white")
        self.canvas2.create_rectangle(0, 0, self.canvasWidth, self.canvasHeight, width=0, fill="white")
        # Algorithm for painting the diagram
        distance = 3
        elementWidth = (self.canvasWidth - (len(config.A) * distance)) / (len(config.A))

        #Draw the rectangles on canvas1 and canvas2
        for i in range(0, len(config.A)):
            if i==config.currentPos and config.algnum==0:
                color = "red"
            elif i == config.pivot and config.algnum==0:
                color = "green"
            elif i==config.currentElement and config.algnum==1:
                color = "red"
            elif i==config.bubbleElement and config.algnum==2:
                color = "red"
            else:
                color = "black"
            posElement1 = i * elementWidth + i * distance
            elementHeight1 = config.A[i] * (self.canvasHeight / 100)
            self.canvas1.create_rectangle(posElement1, self.canvasHeight - elementHeight1, posElement1 + elementWidth,
                                         self.canvasHeight, width=0, fill=color)
            self.canvas1.create_text(posElement1 + 11, self.canvasHeight - 10, fill="white", font="Arial 13 bold",
                                    text=config.A[i])

        for i in range(0, len(config.copyA)):
            if i==config.currentPos and config.comparealg==0:
                color = "red"
            elif i == config.pivot and config.comparealg==0:
                color = "green"
            elif i==config.currentElement and config.comparealg==1:
                color = "red"
            elif i==config.bubbleElement and config.comparealg==2:
                color = "red"
            else:
                color = "black"
            posElement2 = i * elementWidth + i * distance
            elementHeight2 = config.copyA[i] * (self.canvasHeight / 100)
            self.canvas2.create_rectangle(posElement2, self.canvasHeight - elementHeight2, posElement2 + elementWidth,
                                          self.canvasHeight, width=0, fill=color)
            self.canvas2.create_text(posElement2 + 11, self.canvasHeight - 10, fill="white", font="Arial 13 bold",
                                     text=config.copyA[i])
        # Delay before redrawing the canvas
        self.canvas1.after(15, self.draw)

    #Starting the Threads for the algorithm when the command is given
    def runAlgo(self):
        if config.algnum == 0:
            self.Algorithm1 = Quicksort(self, config.A)
        if config.algnum == 1:
            self.Algorithm1 = Insertionsort(self, config.A)
        if config.algnum == 2:
            self.Algorithm1 = Bubblesort(self, config.A)
        if config.comparealg == 0:
            self.Algorithm2 = Quicksort(self, config.copyA)
        if config.comparealg == 1:
            self.Algorithm2 = Insertionsort(self, config.copyA)
        if config.comparealg == 2:
            self.Algorithm2 = Bubblesort(self, config.copyA)

    # Used to return to the page of the algorithm
    def returnCommand(self):
        if config.algnum == 0:
            self.controller.title("Quicksort")
            self.controller.state('zoomed')
            self.controller.show_frame("Display")
        if config.algnum == 1:
            self.controller.title("Insertionsort")
            self.controller.state('zoomed')
            self.controller.show_frame("Display")
        if config.algnum == 2:
            self.controller.title("Bubblesort")
            self.controller.state('zoomed')
            self.controller.show_frame("Display")

    # Randomly generates a new List
    def generateNew(self):
        config.A = [random.randrange(6, 101, 1) for _ in range(20)]
        config.copyA = config.A[:]
