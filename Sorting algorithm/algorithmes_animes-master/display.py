#This class displays the quicksort algorithm
import tkinter as tk
from tkinter import ttk
import random
import config
from quicksort import Quicksort
from insertionsort import Insertionsort
from bubblesort import Bubblesort
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pandas as pd
import math
import ressource

class Display(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ##----------
        ##Section for declaration of GUI elements
        ##----------

        ##Notebook Area
        self.notebook = ttk.Notebook(self, width=700, height=300)
        self.randomFrame = ttk.Frame(self.notebook)
        self.excelFrame = ttk.Frame(self.notebook)
        self.compareFrame = ttk.Frame(self.notebook)
        self.speedFrame = ttk.Frame(self.notebook)
        self.notebook.add(self.randomFrame, text='Liste au hasard')
        self.notebook.add(self.excelFrame, text='Liste Excel')
        self.notebook.add(self.compareFrame, text="Faire une comparison")
        self.notebook.add(self.speedFrame, text="Vitesse d'animation")
        self.notebook.grid(row=1, column=1, padx = 40, pady= 10)

        ##RANDOM FRAME ELEMENTS
        self.newData = ttk.Button(self.randomFrame, text="Nouvelles ", command= self.generateNew, style='my.TButton')
        self.newData.pack(padx=50, pady=30)

        self.runAlgorithm1 = ttk.Button(self.randomFrame, text="Lancer", command=self.runCommand, style='my.TButton')
        self.runAlgorithm1.pack(padx=50, pady=30)

        self.buttonReturn1 = ttk.Button(self.randomFrame, text="Retour", command=self.returnCommand, style='my.TButton')
        self.buttonReturn1.pack(padx=50, pady=30)
        ##END OF RANDOM FRAME ELEMENTS

        ##EXCEL FRAME ELEMENTS
        self.importData = ttk.Button(self.excelFrame, text="Fichier Excel", command=self.load, style='my.TButton')
        self.importData.pack(padx=50, pady=30)

        self.runAlgorithm2 = ttk.Button(self.excelFrame, text="Lancer", command=self.runCommand, style='my.TButton')
        self.runAlgorithm2.pack(padx=50, pady=30)

        self.buttonReturn2 = ttk.Button(self.excelFrame, text="Retour", command=self.returnCommand, style='my.TButton')
        self.buttonReturn2.pack(padx=60, pady=30)
        ##END OF EXCEL FRAME ELEMENTS

        ##COMPARE FRAME ELEMENTS
        self.var = tk.StringVar(self.compareFrame)
        self.var.set("Choisir un comparison")  # initial value

        self.option = ttk.OptionMenu(self.compareFrame, self.var, "Choisir un comparison", "Quicksort", "Insertionsort", "Bubblesort", style="TMenubutton")
        self.option.pack(pady=30)

        self.compareButton = ttk.Button(self.compareFrame, text="Lancer", command=self.compareAlgorithms, style='my.TButton')
        self.compareButton.pack(padx=50, pady=30)

        self.buttonReturn3 = ttk.Button(self.compareFrame, text="Retour", command=self.returnCommand,
                                        style='my.TButton')
        self.buttonReturn3.pack(padx=60, pady=30)
        ##END OF COMPARE FRAME ELEMENTS

        #SPEED FRAME ELEMENTS
        self.v = tk.IntVar()
        self.v.set(1)
        tk.Label(self.speedFrame, text="Vitesse d'animation:", justify=tk.LEFT, padx=20, pady=20, font=controller.restFont).pack()
        tk.Radiobutton(self.speedFrame, text="haute", padx=20, variable=self.v, value=0, font=controller.restFont).pack()
        tk.Radiobutton(self.speedFrame, text="moyenne", padx=20, variable=self.v, value=1, font=controller.restFont).pack()
        tk.Radiobutton(self.speedFrame, text="basse", padx=20, variable=self.v, value=2, font=controller.restFont).pack()
        #END OF SPEED FRAME ELEMENTS
        ##End of Notebook Area

        # Definition of the canvas, canvas drawing is res1ponsive to size changes
        self.canvasWidth = 700
        self.canvasHeight = 400
        self.canvas = tk.Canvas(self, width=self.canvasWidth, height=self.canvasHeight)
        self.canvas.grid(row=1, column=2, padx=5, pady=20, rowspan=3)

        # Message fields to display the text
        self.messageLeft = tk.Message(self, text=ressource.quicksortExplain, width =700)
        self.messageLeft.grid(row=4 ,column=1)
        self.messageLeft.configure(font=("Arial", 14))

        self.messageRight = tk.Message(self, text=ressource.quicksortPseudo, width=700)
        self.messageRight.grid(row=4, column=2)
        self.messageRight.configure(font=("Arial", 14))


        ##----------
        ##End of Section for declaration of GUI elements
        ##----------

        #Initialise the Data and Start the draw Loop
        config.A = [random.randrange(6, 101, 1) for _ in range(20)]
        config.copyA = config.A[:]
        self.draw()

    # Loads array data into the method using pandas
    def load(self):
        name = askopenfilename(filetypes=[('Excel', ('*.xls', '*.xlsx'))])
        df = pd.read_excel(name,index_col=None, header=None)
        #gives the full dataframe as a multidimensional list
        listTosort = df.values.tolist()
        #picks just the first row as the data to be sorted
        #NOTE the animation ist scaled to fit values between 0 and 100
        listTosort = listTosort[0]
        config.A = listTosort[:]

    # Randomly generates a new List
    def generateNew(self):
        config.A = [random.randrange(6, 101, 1) for _ in range(20)]
        config.copyA = config.A[:]

    # Used to execute the quicksort thread on button click
    def runCommand(self):
        if config.algnum == 0:
            quicksort = Quicksort(self, config.A)
        if config.algnum == 1:
            insertionsort = Insertionsort(self, config.A)
        if config.algnum == 2:
            bubblesort = Bubblesort(self, config.A)

    #Used to return to the start page on button click
    def returnCommand(self):
        self.controller.state("normal")
        self.controller.geometry("500x300")
        self.controller.show_frame("StartPage")

    #Method to open the comparing screen
    def compareAlgorithms(self):
        algorithm = self.var.get()
        if algorithm == "Quicksort":
            if config.algnum==0:
                messagebox.showinfo("Error", " un algorithme ")
            else:
                config.comparealg=0
                self.controller.state("normal")
                self.controller.geometry("1050x500")
                self.controller.title("Comparison")
                self.controller.show_frame("Compare")
        elif algorithm == "Insertionsort":
            if config.algnum==1:
                messagebox.showinfo("Error", " un algorithme ")
            else:
                config.comparealg=1
                self.controller.state("normal")
                self.controller.geometry("1050x500")
                self.controller.title("Comparison")
                self.controller.show_frame("Compare")
        elif algorithm == "Bubblesort":
            if config.algnum==2:
                messagebox.showinfo("Error", " un algorithme ")
            else:
                config.comparealg=2
                self.controller.state("normal")
                self.controller.geometry("1050x500")
                self.controller.title("Comparison")
                self.controller.show_frame("Compare")

    # Canvas draw
    def draw(self):
        if config.runvar == 1:
            self.newData.config(state="disabled")
            self.runAlgorithm1.config(state="disabled")
            self.buttonReturn1.config(state="disabled")
            self.runAlgorithm2.config(state="disabled")
            self.buttonReturn2.config(state="disabled")
            self.buttonReturn3.config(state="disabled")
            self.compareButton.config(state="disabled")
        else:
            self.newData.config(state="normal")
            self.runAlgorithm1.config(state="normal")
            self.buttonReturn1.config(state="normal")
            self.runAlgorithm2.config(state="normal")
            self.buttonReturn2.config(state="normal")
            self.buttonReturn3.config(state="normal")
            self.compareButton.config(state="normal")
        #update the speed of the animation
        config.speedind = self.v.get()
        # clear the canvas
        self.canvas.delete("all")
        # Give the canvas a white background
        self.canvas.create_rectangle(0, 0, self.canvasWidth, self.canvasHeight, width=0, fill="white")
        # Algorithm for painting the diagram
        distance = 3
        # color = "black"
        elementWidth = (self.canvasWidth - (len(config.A) * distance)) / (len(config.A))
        for i in range(0, len(config.A)):
            if i == config.currentPos and config.algnum == 0:
                color = "red"
            elif i == config.pivot and config.algnum == 0:
                color = "green"
            elif i == config.currentElement and config.algnum==1:
                color="red"
            elif i == config.bubbleElement and config.algnum==2:
                color="red"
            else:
                color = "black"
            posElement = i * elementWidth + i * distance
            elementHeight = config.A[i] * (self.canvasHeight / 100)
            self.canvas.create_rectangle(posElement, self.canvasHeight - elementHeight, posElement + elementWidth,
                                         self.canvasHeight, width=0, fill=color)
            self.canvas.create_text(posElement + 15, self.canvasHeight - 15, fill="white",font="Arial 17 bold", text=config.A[i])
        # Delay before redrawing the canvas
        self.canvas.after(15, self.draw)
