from tkinter import*
import sys

COLORS = ['white', 'yellow', 'orange', 'red', 'green', 'blue']

class Application(Frame):
    """A GUI application with three buttons"""
    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self,master)
        self.grid()
        self.resetClick = 0
        self.solveClick = 0
        self.buttonA0click = 0
        self.buttonA1click = 0
        self.buttonA2click = 0
        self.buttonB0click = 0
        self.buttonB2click = 0
        self.buttonC0click = 0
        self.buttonC1click = 0
        self.buttonC2click = 0
        self.buttonA0 = Button(self, bg = COLORS[0], width = '10', height = '5')
        self.buttonA1 = Button(self, bg = COLORS[0], width = '10', height = '5')
        self.buttonA2 = Button(self, bg = COLORS[0], width = '10', height = '5')
        self.buttonB0 = Button(self, bg = COLORS[0], width = '10', height = '5')
        self.buttonB1 = Button(self, bg = COLORS[0], width = '10', height = '5')
        self.buttonB2 = Button(self, bg = COLORS[0], width = '10', height = '5')
        self.buttonC0 = Button(self, bg = COLORS[0], width = '10', height = '5')
        self.buttonC1 = Button(self, bg = COLORS[0], width = '10', height = '5')
        self.buttonC2 = Button(self, bg = COLORS[0], width = '10', height = '5')
        self.buttonA0.grid(row=1, column = 0)
        self.buttonA1.grid(row=1, column = 1)
        self.buttonA2.grid(row=1, column = 2)
        self.buttonB0.grid(row=2, column = 0)
        self.buttonB1.grid(row=2, column = 1)
        self.buttonB2.grid(row=2, column = 2)
        self.buttonC0.grid(row=3, column = 0)
        self.buttonC1.grid(row=3, column = 1)
        self.buttonC2.grid(row=3, column = 2)
        self.create_widgets()
        self.update_cube_image()

    def create_widgets(self):
        """" Create 3 buttons that do something """
        # Create the first buttons
        # self.buttonReset = Button(self, text = "Reset")
        # self.buttonReset.grid(row = 0, column = 0)

        # Create the reset button
        self.buttonReset = Button(self)
        self.buttonReset.grid(row = 0, column = 0)
        self.buttonReset.configure(text = "Reset")

        # Create the solve button
        self.buttonSolve = Button(self)
        self.buttonSolve.grid(row = 0, column = 2)
        self.buttonSolve.configure(text = "Solve")

        # Create the prev button
        self.buttonPrev = Button(self)
        self.buttonPrev.grid(row = 4, column = 0)
        self.buttonPrev.configure(text = "Previous")

        # Create the next button
        self.buttonNext = Button(self)
        self.buttonNext.grid(row = 4, column = 1)
        self.buttonNext.configure(text = "Next")

        # Create the switch face
        self.buttonFace = Button(self)
        self.buttonFace.grid(row = 4, column = 2)
        self.buttonFace.configure(text = "Switch Face")
        self.buttonFace["command"] = reset_cube

    def reset_cube
    def update_cube_image(self):
        ''' Creates the white face '''

        self.buttonA0["command"] = self.update_A0
        self.buttonA1["command"] = self.update_A1
        self.buttonA2["command"] = self.update_A2
        self.buttonB0["command"] = self.update_B0
        self.buttonB2["command"] = self.update_B2
        self.buttonC0["command"] = self.update_C0
        self.buttonC1["command"] = self.update_C1
        self.buttonC2["command"] = self.update_C2

    def update_A0(self):
        self.buttonA0click += 1
        if self.buttonA0click == 6: self.buttonA0click = 0
        self.buttonA0["bg"] = COLORS[self.buttonA0click]
        # self.buttonA0["text"] = str(self.buttonA0click)

    def update_A1(self):
        self.buttonA1click += 1
        if self.buttonA1click == 6: self.buttonA1click = 0
        self.buttonA1["bg"] = COLORS[self.buttonA1click]

    def update_A2(self):
        self.buttonA2click += 1
        if self.buttonA2click == 6: self.buttonA2click = 0
        self.buttonA2["bg"] = COLORS[self.buttonA2click]

    def update_B0(self):
        self.buttonB0click += 1
        if self.buttonB0click == 6: self.buttonB0click = 0
        self.buttonB0["bg"] = COLORS[self.buttonB0click]

    def update_B2(self):
        self.buttonB2click += 1
        if self.buttonB2click == 6: self.buttonB2click = 0
        self.buttonB2["bg"] = COLORS[self.buttonB2click]

    def update_C0(self):
        self.buttonC0click += 1
        if self.buttonC0click == 6: self.buttonC0click = 0
        self.buttonC0["bg"] = COLORS[self.buttonC0click]

    def update_C1(self):
        self.buttonC1click += 1
        if self.buttonC1click == 6: self.buttonC1click = 0
        self.buttonC1["bg"] = COLORS[self.buttonC1click]

    def update_C2(self):
        self.buttonC2click += 1
        if self.buttonC2click == 6: self.buttonC2click = 0
        self.buttonC2["bg"] = COLORS[self.buttonC2click]

    print("test")

root = Tk()
root.title("The Rubiks Game")
root.geometry("240x370")

app = Application(root)
root.mainloop()
