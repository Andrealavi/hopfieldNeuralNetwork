from HopfieldNetwork import HopfieldNetwork
from tkinter import *
from tkinter import ttk
import os

class PatternGrid():
    def __init__(self, parent: ttk.Frame, n: int = 25):
        self.parent: ttk.Frame = parent
        self.n: int = n
        self.buttons: list[list[Button]] = []

    def changeColor(self, event: Event) -> None:
        background = "blue" if event.widget["bg"] == "white" else "white"
        event.widget.configure(background=background)    


    def addPatternElements(self) -> None:
        for i in range(self.n):
            buttonsRow: list[Button] = []

            for j in range(self.n):
                button = Button(self.parent, background="white", height=1, width=1)
                button.bind("<Button>", self.changeColor)
                button.grid(column=j+1, row=i+1)

                buttonsRow.append(button)
            
            self.buttons.append(buttonsRow)

    def getMatrixValues(self) -> list[list[int]]:
        matrixValues: list[list[int]] = []
        
        for i in range(self.n):
            row: list[int] = []
            for j in range(self.n):
                if self.buttons[i][j]['bg'] == 'white':
                    row.append(-1)
                else:
                    row.append(1)

            matrixValues.append(row)
        
        return matrixValues

    def cleanPattern(self) -> None:
        for i in range(self.n):
            for j in range(self.n):
                self.buttons[i][j]['bg'] = 'white'

def computePattern(event: Event) -> None:
    matrixValues: list[list[int]] = pattern.getMatrixValues()

    rowSum = 0
    for row in matrixValues:
        rowSum += sum(row)

    if rowSum == (-1 * NEURONS_NUMBER**2):
        return

    result = net.classify(matrixValues)

    if result == None:
        canva.delete('all')
        return

    length = 30 

    for i in range(len(result)):
        for j in range(len(result[0])):
            x1: int = i*length + (1 if i > 0 else 0)*5
            x2: int = i*length + length
            y1: int = j*length + (1 if j > 0 else 0)*5
            y2: int = j*length + length 

            if result[j][i] == 1:
                color: str = "#000000"
            else:
                color: str = "#ffffff"

            canva.create_polygon(x1, y1, x2, y1, x2, y2, x1, y2, outline=color, fill=color)

    pattern.cleanPattern()


def cleanGrid(event: Event) -> None:
    pattern.cleanPattern()

def read_pattern(file_name: str) -> list[list[int]]:
    f = open(file_name)

    pattern: list[list[int]] = []

    for line in f.readlines():
        line = line.replace("\n", "").split(" ")
        pattern.append([int(num) for num in line])
    
    return pattern

def addPattern(event: Event) -> None:
    matrixValues: list[list[int]] = pattern.getMatrixValues()

    net.add_pattern(matrixValues)

    net.train()

    pattern.cleanPattern()

App: Tk = Tk()
net: HopfieldNetwork = HopfieldNetwork()

net.add_pattern(read_pattern(os.path.join(".", "patterns", "1.txt")))
net.add_pattern(read_pattern(os.path.join(".", "patterns", "2.txt")))
net.add_pattern(read_pattern(os.path.join(".", "patterns", "3.txt")))

net.train()

NEURONS_NUMBER: int = 9
frame: ttk.Frame = ttk.Frame(App, padding=10, height=300, width=500)

pattern: PatternGrid = PatternGrid(frame, NEURONS_NUMBER)
pattern.addPatternElements()

canva: Canvas = Canvas(frame, height=275, width=275)
canva.grid(column=NEURONS_NUMBER+2, row=1, rowspan=NEURONS_NUMBER)

inputButton: Button = Button(frame, text="Input", height=1, width=15)
inputButton.bind("<Button>", computePattern)
inputButton.grid(column=NEURONS_NUMBER+1, row=NEURONS_NUMBER//2, padx=20)

cleanButton: Button = Button(frame, text="Clear", height=1, width=15)
cleanButton.bind("<Button>", cleanGrid)
cleanButton.grid(column=NEURONS_NUMBER+1, row=NEURONS_NUMBER//2 + 1, padx=20)

addButton: Button = Button(frame, text="Add Pattern", height=1, width=15, padx=20)
addButton.bind("<Button>", addPattern)
addButton.grid(column=NEURONS_NUMBER+1, row=NEURONS_NUMBER//2 + 3, padx=20)

frame.grid(column=0, row=0)

App.mainloop()

