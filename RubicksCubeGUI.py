from tkinter import*
import sys

COLORS     = ['white', 'yellow', 'orange', 'red', 'green', 'blue']
CURRENTFACE= [0, 0, 0, 0, 0, 0, 0, 0, 0]
WHITEFACE  = [0, 0, 0, 0, 0, 0, 0, 0, 0]
YELLOWFACE = [1, 1, 1, 1, 1, 1, 1, 1, 1]
ORANGEFACE = [2, 2, 2, 2, 2, 2, 2, 2, 2]
REDFACE    = [3, 3, 3, 3, 3, 3, 3, 3, 3]
GREENFACE  = [4, 4, 4, 4, 4, 4, 4, 4, 4]
BLUEFACE   = [5, 5, 5, 5, 5, 5, 5, 5, 5]
SOLVESTATE = 0

class Application(Frame):
    """A GUI application with three buttons"""
    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self,master)
        self.grid()
        self.resetClick    = 0
        self.solveClick    = 0
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
        self.buttonA0.grid(row=3, column = 0)
        self.buttonA1.grid(row=3, column = 1)
        self.buttonA2.grid(row=3, column = 2)
        self.buttonB0.grid(row=4, column = 0)
        self.buttonB1.grid(row=4, column = 1)
        self.buttonB2.grid(row=4, column = 2)
        self.buttonC0.grid(row=5, column = 0)
        self.buttonC1.grid(row=5, column = 1)
        self.buttonC2.grid(row=5, column = 2)
        self.FACEVALUE = 0
        self.create_widgets()
        self.update_cube_image()

    def create_widgets(self):


        # Create the solve button
        self.buttonSolve = Button(self)
        self.buttonSolve.grid(row = 0, column = 2)
        self.buttonSolve.configure(text = "Solve")

        if SOLVESTATE != 1: self.buttonSolve["command"] = self.sendToSolve

        # Create the prev button
        self.buttonPrev = Button(self)
        self.buttonPrev.grid(row = 6, column = 0)
        self.buttonPrev.configure(text = "Previous")

        # Create the next button
        self.buttonNext = Button(self)
        self.buttonNext.grid(row = 6, column = 1)
        self.buttonNext.configure(text = "Next")

        # Create the switch face
        self.buttonFace = Button(self)
        self.buttonFace.grid(row = 6, column = 2)
        self.buttonFace.configure(text = "Switch Face")
        self.buttonFace["command"] = self.reset_cube

        # Create the the 1st descriptive label
        self.frtLabel = Label(self)
        self.frtLabel.grid(row = 2, column = 1)
        self.frtLabel.configure(text = "Red Face")

        # Create the the 2nd descriptive label
        self.topLabel = Label(self)
        self.topLabel.grid(row = 1, column = 1)
        self.topLabel.configure(text = "White Face")

        # Create the the 1st descriptive label thing
        self.frtLabelthing = Label(self)
        self.frtLabelthing.grid(row = 1, column = 0)
        self.frtLabelthing.configure(text = "Front face:")

        # Create the the 2nd descriptive label thing
        self.topLabelthing = Label(self)
        self.topLabelthing.grid(row = 2, column = 0)
        self.topLabelthing.configure(text = "Top face:")

        # Create the steps label
        self.stepLabel = Label(self)
        self.stepLabel.grid(row = 7, column = 1)
        self.stepLabel.configure(text = "hERE i AM!")


    def sendToSolve(self):
        SOLVESTATE = 1
        self.buttonSolve["command"] = " "
        self.reset_cube()
        text_file = open("UserData.txt", "w")
        for i in range(0,4):
            text_file.write("%s " % str(COLORS[WHITEFACE[i]]))
        for i in range(5,9):
            text_file.write("%s " % str(COLORS[WHITEFACE[i]]))
        text_file.write("\n")
        for i in range(0,4):
            text_file.write("%s " % str(COLORS[YELLOWFACE[i]]))
        for i in range(5,9):
            text_file.write("%s " % str(COLORS[YELLOWFACE[i]]))
        text_file.write("\n")
        for i in range(0,4):
            text_file.write("%s " % str(COLORS[ORANGEFACE[i]]))
        for i in range(5,9):
            text_file.write("%s " % str(COLORS[ORANGEFACE[i]]))
        text_file.write("\n")
        for i in range(0,4):
            text_file.write("%s " % str(COLORS[REDFACE[i]]))
        for i in range(5,9):
            text_file.write("%s " % str(COLORS[REDFACE[i]]))
        text_file.write("\n")
        for i in range(0,4):
            text_file.write("%s " % str(COLORS[GREENFACE[i]]))
        for i in range(5,9):
            text_file.write("%s " % str(COLORS[GREENFACE[i]]))
        text_file.write("\n")
        for i in range(0,4):
            text_file.write("%s " % str(COLORS[BLUEFACE[i]]))
        for i in range(5,9):
            text_file.write("%s " % str(COLORS[BLUEFACE[i]]))
        text_file.write("\n")
        text_file.close()

        notfound = True
        self.thingsToDo = []
        while notfound:
            with open("instructions.txt") as file:
                for line in file:
                    self.thingsToDo.append(line.strip())
                notfound = False


    def reset_cube(self):
        self.FACEVALUE += 1
        if self.FACEVALUE == 6: self.FACEVALUE = 0
        if self.FACEVALUE == 0:
            self.topLabel.configure(text = "White Face")
            self.frtLabel.configure(text = "Red Face")
            for i in range(9):
                BLUEFACE[i] = CURRENTFACE[i]
            for i in range(9):
                CURRENTFACE[i] = WHITEFACE[i]
        if self.FACEVALUE == 1:
            self.topLabel.configure(text = "Yellow Face")
            self.frtLabel.configure(text = "Orange Face")
            for i in range(9):
                WHITEFACE[i] = CURRENTFACE[i]
            for i in range(9):
                CURRENTFACE[i] = YELLOWFACE[i]
        if self.FACEVALUE == 2:
            self.topLabel.configure(text = "Orange Face")
            self.frtLabel.configure(text = "White Face")
            for i in range(9):
                YELLOWFACE[i] = CURRENTFACE[i]
            for i in range(9):
                CURRENTFACE[i] = ORANGEFACE[i]
        if self.FACEVALUE == 3:
            self.topLabel.configure(text = "Red Face")
            self.frtLabel.configure(text = "White Face")
            for i in range(9):
                ORANGEFACE[i] = CURRENTFACE[i]
            for i in range(9):
                CURRENTFACE[i] = REDFACE[i]
        if self.FACEVALUE == 4:
            self.topLabel.configure(text = "Green Face")
            self.frtLabel.configure(text = "White Face")
            for i in range(9):
                REDFACE[i] = CURRENTFACE[i]
            for i in range(9):
                CURRENTFACE[i] = GREENFACE[i]
        if self.FACEVALUE == 5:
            self.topLabel.configure(text = "Blue Face")
            self.frtLabel.configure(text = "White Face")
            for i in range(9):
                GREENFACE[i] = CURRENTFACE[i]
            for i in range(9):
                CURRENTFACE[i] = BLUEFACE[i]


        if self.FACEVALUE == 0 :
            self.buttonA0.configure(bg = COLORS[WHITEFACE[0]])
            self.buttonA1.configure(bg = COLORS[WHITEFACE[1]])
            self.buttonA2.configure(bg = COLORS[WHITEFACE[2]])
            self.buttonB0.configure(bg = COLORS[WHITEFACE[3]])
            self.buttonB1.configure(bg = COLORS[WHITEFACE[4]])
            self.buttonB2.configure(bg = COLORS[WHITEFACE[5]])
            self.buttonC0.configure(bg = COLORS[WHITEFACE[6]])
            self.buttonC1.configure(bg = COLORS[WHITEFACE[7]])
            self.buttonC2.configure(bg = COLORS[WHITEFACE[8]])
        if self.FACEVALUE == 1 :
            self.buttonA0.configure(bg = COLORS[YELLOWFACE[0]])
            self.buttonA1.configure(bg = COLORS[YELLOWFACE[1]])
            self.buttonA2.configure(bg = COLORS[YELLOWFACE[2]])
            self.buttonB0.configure(bg = COLORS[YELLOWFACE[3]])
            self.buttonB1.configure(bg = COLORS[YELLOWFACE[4]])
            self.buttonB2.configure(bg = COLORS[YELLOWFACE[5]])
            self.buttonC0.configure(bg = COLORS[YELLOWFACE[6]])
            self.buttonC1.configure(bg = COLORS[YELLOWFACE[7]])
            self.buttonC2.configure(bg = COLORS[YELLOWFACE[8]])
        if self.FACEVALUE == 2 :
            self.buttonA0.configure(bg = COLORS[ORANGEFACE[0]])
            self.buttonA1.configure(bg = COLORS[ORANGEFACE[1]])
            self.buttonA2.configure(bg = COLORS[ORANGEFACE[2]])
            self.buttonB0.configure(bg = COLORS[ORANGEFACE[3]])
            self.buttonB1.configure(bg = COLORS[ORANGEFACE[4]])
            self.buttonB2.configure(bg = COLORS[ORANGEFACE[5]])
            self.buttonC0.configure(bg = COLORS[ORANGEFACE[6]])
            self.buttonC1.configure(bg = COLORS[ORANGEFACE[7]])
            self.buttonC2.configure(bg = COLORS[ORANGEFACE[8]])
        if self.FACEVALUE == 3 :
            self.buttonA0.configure(bg = COLORS[REDFACE[0]])
            self.buttonA1.configure(bg = COLORS[REDFACE[1]])
            self.buttonA2.configure(bg = COLORS[REDFACE[2]])
            self.buttonB0.configure(bg = COLORS[REDFACE[3]])
            self.buttonB1.configure(bg = COLORS[REDFACE[4]])
            self.buttonB2.configure(bg = COLORS[REDFACE[5]])
            self.buttonC0.configure(bg = COLORS[REDFACE[6]])
            self.buttonC1.configure(bg = COLORS[REDFACE[7]])
            self.buttonC2.configure(bg = COLORS[REDFACE[8]])
        if self.FACEVALUE == 4 :
            self.buttonA0.configure(bg = COLORS[GREENFACE[0]])
            self.buttonA1.configure(bg = COLORS[GREENFACE[1]])
            self.buttonA2.configure(bg = COLORS[GREENFACE[2]])
            self.buttonB0.configure(bg = COLORS[GREENFACE[3]])
            self.buttonB1.configure(bg = COLORS[GREENFACE[4]])
            self.buttonB2.configure(bg = COLORS[GREENFACE[5]])
            self.buttonC0.configure(bg = COLORS[GREENFACE[6]])
            self.buttonC1.configure(bg = COLORS[GREENFACE[7]])
            self.buttonC2.configure(bg = COLORS[GREENFACE[8]])
        if self.FACEVALUE == 5 :
            self.buttonA0.configure(bg = COLORS[BLUEFACE[0]])
            self.buttonA1.configure(bg = COLORS[BLUEFACE[1]])
            self.buttonA2.configure(bg = COLORS[BLUEFACE[2]])
            self.buttonB0.configure(bg = COLORS[BLUEFACE[3]])
            self.buttonB1.configure(bg = COLORS[BLUEFACE[4]])
            self.buttonB2.configure(bg = COLORS[BLUEFACE[5]])
            self.buttonC0.configure(bg = COLORS[BLUEFACE[6]])
            self.buttonC1.configure(bg = COLORS[BLUEFACE[7]])
            self.buttonC2.configure(bg = COLORS[BLUEFACE[8]])




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
        CURRENTFACE[0] += 1
        if CURRENTFACE[0] == 6: CURRENTFACE[0] = 0

    def update_A1(self):
        self.buttonA1click += 1
        if self.buttonA1click == 6: self.buttonA1click = 0
        self.buttonA1["bg"] = COLORS[self.buttonA1click]
        CURRENTFACE[1] += 1
        if CURRENTFACE[1] == 6: CURRENTFACE[1] = 0

    def update_A2(self):
        self.buttonA2click += 1
        if self.buttonA2click == 6: self.buttonA2click = 0
        self.buttonA2["bg"] = COLORS[self.buttonA2click]
        CURRENTFACE[2] += 1
        if CURRENTFACE[2] == 6: CURRENTFACE[2] = 0

    def update_B0(self):
        self.buttonB0click += 1
        if self.buttonB0click == 6: self.buttonB0click = 0
        self.buttonB0["bg"] = COLORS[self.buttonB0click]
        CURRENTFACE[3] += 1
        if CURRENTFACE[3] == 6: CURRENTFACE[3] = 0

    def update_B2(self):
        self.buttonB2click += 1
        if self.buttonB2click == 6: self.buttonB2click = 0
        self.buttonB2["bg"] = COLORS[self.buttonB2click]
        CURRENTFACE[5] += 1
        if CURRENTFACE[5] == 6: CURRENTFACE[5] = 0

    def update_C0(self):
        self.buttonC0click += 1
        if self.buttonC0click == 6: self.buttonC0click = 0
        self.buttonC0["bg"] = COLORS[self.buttonC0click]
        CURRENTFACE[6] += 1
        if CURRENTFACE[6] == 6: CURRENTFACE[6] = 0

    def update_C1(self):
        self.buttonC1click += 1
        if self.buttonC1click == 6: self.buttonC1click = 0
        self.buttonC1["bg"] = COLORS[self.buttonC1click]
        CURRENTFACE[7] += 1
        if CURRENTFACE[7] == 6: CURRENTFACE[7] = 0

    def update_C2(self):
        self.buttonC2click += 1
        if self.buttonC2click == 6: self.buttonC2click = 0
        self.buttonC2["bg"] = COLORS[self.buttonC2click]
        CURRENTFACE[8] += 1
        if CURRENTFACE[8] == 6: CURRENTFACE[8] = 0

root = Tk()
root.title("The Rubiks Game")
root.geometry("240x400")

app = Application(root)
root.mainloop()
