from corner import Corner
from edge import Edge
from face import Face
'''
BIG PLACE TO PUT THE INPUT STUFF
input gets 6 arrays of 8 elements. each element is a string "color"
top
bottom
front
back
left
right
'''
instructions = []
'''
method to turn these arrays into corners, edges, and faces
spits out
top -> white
bottom -> yellow
front -> orange
back -> red
left -> blue
right -> green
'''
'''
cornerA = Corner(top[0], back[2], left[0])
cornerB = Corner(top[2], back[0], right[2])
cornerC = Corner(top[7], front[2], right[0])
cornerD = Corner(top[5], front[0], left[2])
cornerE = Corner(bottom[0], front[5], left[7])
cornerF = Corner(bottom[2], front[7], right[5])
cornerG = Corner(bottom[7], back[5], right[7])
cornerH = Corner(bottom[7], back[7], left[5])

edgeA = Edge(top[1], back[1])
edgeB = Edge(top[4], right[1])
edgeC = Edge(top[6], front[1])
edgeD = Edge(top[3], left[1])
edgeE = Edge(bottom[1], front[6])
edgeF = Edge(bottom[4], right[6])
edgeG = Edge(bottom[6], back[6])
edgeH = Edge(bottom[3], left[6])
edgeI = Edge(front[3], left[4])
edgeJ = Edge(front[4], right[3])
edgeK = Edge(back[3], right[4])
edgeL = Edge(back[4], left[3])
'''


#The following section initializes a default (solved) cube.
cornerA = Corner('white','red', 'blue')
cornerB = Corner('white','red', 'green')
cornerC = Corner('white','orange', 'green')
cornerD = Corner('white','orange', 'blue')
cornerE = Corner('yellow','orange', 'blue')
cornerF = Corner('yellow','orange', 'green')
cornerG = Corner('yellow','red', 'green')
cornerH = Corner('yellow','red', 'blue')

edgeA = Edge('white', 'red')
edgeB = Edge('white', 'green')
edgeC = Edge('white', 'orange')
edgeD = Edge('white', 'blue')
edgeE = Edge('yellow', 'orange')
edgeF = Edge('yellow', 'green')
edgeG = Edge('yellow', 'red')
edgeH = Edge('yellow', 'blue')
edgeI = Edge('orange', 'blue')
edgeJ = Edge('orange', 'green')
edgeK = Edge('red', 'green')
edgeL = Edge('red', 'blue')

white = Face('white', cornerA, cornerB, cornerC, cornerD, edgeA, edgeB, edgeC, edgeD)
yellow = Face('yellow', cornerE, cornerF, cornerG, cornerH, edgeE, edgeF, edgeG, edgeH)
orange = Face('orange', cornerD, cornerC, cornerF, cornerE, edgeC, edgeJ, edgeE, edgeI)
red = Face('red', cornerB, cornerA, cornerH, cornerG, edgeA, edgeL, edgeG, edgeK)
green = Face('green', cornerC, cornerB, cornerG, cornerF, edgeB, edgeK, edgeF, edgeJ)
blue = Face('blue', cornerA, cornerD, cornerE, cornerH, edgeD, edgeI, edgeH, edgeL)
Faces = [white, yellow, orange, red, green, blue]


'''
Use this space to test anything:
'''

white.rotateCW
green.rotateCCW
blue.rotateCW
green.rotateCW




'''
This prints out the current condition of the cube.
'''

for i in Faces:
    print("Face:________________________ "+i.getCentre())
    for j in i.getCorners():
        for k in j.getColors():
            print(k, end=' ')
        print()
    for j in i.getEdges():
        for k in j.getColors():
            print(k, end=' ')
        print()

#for corner peice 
#repeat until corner peice in correct position

#white face if corner peice is located on index 2 on orange face or index 3 on green face or index 1 on yellow face
#while
while(yellow.getCorners()[1].getColors!=  ['white', 'orange', 'green']):
    yellow.rotateCW
    while (white.getCorners()[2].getColors()!= ['white', 'orange', 'green']):

        green.rotateCCW(Faces)
        yellow.rotateCCW(Faces)
        green.rotateCW(Faces)
        yellow.rotateCW(Faces)
        instructions.append("!R !D R D ")

#white face if corner peice is located on index 2 on green face or index 3 on red face or index 2 on yellow face
while(yellow.getCorners()[2].getColors!= ['white', 'red', 'green']):
    yellow.rotateCW
    while (white.getCorners()[1].getColors()!= ['white', 'red', 'green']):

        red.rotateCCW(Faces)
        yellow.rotateCCW(Faces)
        red.rotateCW(Faces)
        yellow.rotateCW(Faces)
        instructions.append("B !D !B D ")

#white face if corner peice is located on index 2 on red face index 3 on blue face or index 3 on yellow face
while(yellow.getCorners()[3].getColors!=['white', 'red', 'blue']):
    yellow.rotateCW
    while (white.getCorners()[0].getColors()!=['white', 'red', 'blue']):
        blue.rotateCCW(Faces)
        yellow.rotateCCW(Faces)
        blue.rotateCW(Faces)
        yellow.rotateCW(Faces)
        instructions.append("!L !D L D ")

#white face if corner peice is located on index 3 on orange face or index 2 on blue face or index 0 on yellow face
while(yellow.getCorners()[0].getColors!=['white', 'orange', 'blue']):
    yellow.rotateCW
    while (white.getCorners()[3].getColors()!=['white', 'orange', 'blue']):
        orange.rotateCCW(Faces)
        yellow.rotateCCW(Faces)
        orange.rotateCW(Faces)
        yellow.rotateCW(Faces)
        instructions.append("!F !D F D ")

#for edge peices
while( white.getEdges()[3].getColors()!=(['white', 'blue'] or ['blue', 'white'])):
    blue.rotateCW
    if(white.getEdges()[3].getColors()==['blue', 'white']):
        orange.rotateCCW
        white.rotateCW
        blue.rotateCCW
        white.rotateCCW
        instructions.append("!F U !L !U ")
        if(blue.getEdges()[1].getColors()==['blue','white']):
           blue.rotateCW
           blue.rotateCW
           instructions.append("L L ")

while(white.getEdges()[1].getColors!=(['white', 'green'] or ['green', 'white'])):
    yellow.rotateCW
    instructions.append("D ")
    if(white.getEdges()[1].getColors()==['green', 'white']):
        green.rotateCW
        white.rotateCW
        orange.rotateCCW
        white.rotateCCW
        instructions.append("R U !F !U ")
    if(green.getEdges()[1].getColour()==['white', 'green']):
        green.rotateCW
        green.rotateCW
        instructions.append("R R ")
       
while(white.getEdges()[0].getColors()!=(['white', 'red'] or ['red', 'white'])):
    yellow.rotateCW
    instructions.append("D ")
    if(white.getEdges()[0].getColors()==['red', 'white']):
        red.rotateCCW
        white.rotateCW
        green.rotateCCW
        white.rotateCCW
        instructions.append("B U !R !U ")
        if(red.getEdges()[1].getColors()==['white','red']):   
           red.rotateCW
           red.rotateCW
           instructions.append("!B !B ")
       
while(white.getEdges()[2].getColors()!= (['white', 'orange'] or ['orange', 'white'])):
    yellow.rotateCW
    instructions.append("D ")
    if(white.getEdges()[2].getColors()==['orange', 'white']):
        orange.rotateCCW
        white.rotateCW
        blue.rotateCCW
        white.rotateCCW
        instructions.append("!F U !L !U ")
        if(orage.getEdges()[1].getColors()==['white','orange']):
            orange.rotateCW
            orange.rotateCW
            instructions.append("F F ")
          
while(true):
    if(orange.getEdges()[3].getColors!=(['orange', 'blue'])):
        i = 0
        unfound = true
        while(i<4 & unfound):
            if(yellow.getEdges()[i].getColors==(['blue','orange'] or ['orange','blue'])):
                unfound = false
            else:
                i+=1
        if(yellow.getEdges()[i].getColors==(['orange', 'blue'])):
            unmatched = true
            while(unmatched):
                yellow.rotateCW
                if('blue' == blue.getEdges()[2].getColors()[1]):
                    unmatched = false
            #Algorithm start
            yellow.rotateCCW
            green.rotateCW
            orange.rotateCCW
            green.rotateCCW
            blue.rotateCW
            yellow.rotateCW
            blue.rotateCCW
            yellow.rotateCW
            blue.rotateCCW
            green.rotateCW
            yellow.rotateCCW
            blue.rotateCW
            green.rotateCCW
            instructions.append("!D R !F !R L D !L D !L R !D L !R ")
        if(yellow.getEdges()[i].getColors==(['blue', 'orange'])):
            unmatched = true
            while(unmatched):
                yellow.rotateCW
                instructions.append("D ")
                if('orange' == orange.getEdges()[2].getColors()[1]):
                    unmatched = false
            #Algorithm start
            yellow.rotateCW
            red.rotateCCW
            blue.rotateCW
            red.rotateCW
            orange.rotateCCW
            yellow.rotateCCW
            orange.rotateCW
            yellow.rotateCW
            orange.rotateCW
            red.rotateCCW
            yellow.rotateCCW
            orange.rotateCCW
            red.rotateCW   
            instructions.append("D B L !B !F !D !f D !F B !D F R ")
while(true):
    if(green.getEdges()[3].getColors!=(['orange', 'green'])):
        i = 0
        unfound = true
        while(i<4 & unfound):
            if(yellow.getEdges()[i].getColors==(['green','orange'] or ['orange','green'])):
                unfound = false
            else:
                i+=1
        if(yellow.getEdges()[i].getColors==(['orange', 'green'])):
            unmatched = true
            while(unmatched):
                yellow.rotateCW
                instructions.append("D ")
                if('orange' == orange.getEdges()[2].getColors()[1]):
                    unmatched = false
            #Algorithm start
            yellow.rotateCCW
            red.rotateCW
            green.rotateCCW
            red.rotateCCW
            orange.rotateCW
            yellow.rotateCW
            orange.rotateCCW
            yellow.rotateCW
            orange.rotateCCW
            red.rotateCW
            yellow.rotateCCW
            orange.rotateCW
            red.rotateCCW
            instructions.append("!D !B !R B F D !F D !F !B !D F B ")
        if(yellow.getEdges()[i].getColors==(['green', 'orange'])):
            unmatched = true
            while(unmatched):
                yellow.rotateCW
                instructions.append("D ")
                if('green' == green.getEdges()[2].getColors()[1]):
                    unmatched = false
            #Algorithm start
            yellow.rotateCW
            blue.rotateCCW
            orange.rotateCW
            blue.rotateCW
            green.rotateCCW
            yellow.rotateCCW
            green.rotateCW
            yellow.rotateCW
            green.rotateCW
            blue.rotateCCW
            yellow.rotateCCW
            green.rotateCCW
            blue.rotateCW
            instructions.append("D !L R L !R !D R D R !L !D !R L ")

while(true):
    if(red.getEdges()[3].getColors!=(['red', 'green'])):
        i = 0
        unfound = true
        while(i<4 & unfound):
            if(yellow.getEdges()[i].getColors==(['green','red'] or ['red','green'])):
                unfound = false
            else:
                i+=1
        if(yellow.getEdges()[i].getColors==(['red', 'green'])):
            unmatched = true
            while(unmatched):
                yellow.rotateCW
                instructions.append("D ")
                if('green' == green.getEdges()[2].getColors()[1]):
                    unmatched = false
            #Algorithm start
            yellow.rotateCCW
            blue.rotateCW
            red.rotateCCW
            blue.rotateCCW
            green.rotateCW
            yellow.rotateCW
            green.rotateCCW
            yellow.rotateCW
            green.rotateCCW
            blue.rotateCW
            yellow.rotateCCW
            green.rotateCW
            blue.rotateCCW
            instructions.append("!D L B !L R D !R D !R L !D R !L ")
            
        if(yellow.getEdges()[i].getColors==(['green', 'red'])):
            unmatched = true
            while(unmatched):
                yellow.rotateCW
                instructions.append("D ")
                if('red' == red.getEdges()[2].getColors()[1]):
                    unmatched = false
            #Algorithm start
            yellow.rotateCW
            orange.rotateCCW
            green.rotateCW
            orange.rotateCW
            red.rotateCCW
            yellow.rotateCCW
            red.rotateCW
            yellow.rotateCW
            red.rotateCW
            orange.rotateCCW
            yellow.rotateCCW
            red.rotateCCW
            orange.rotateCW
            instructions.append("D !F R F B !D !B D !B !F !D B !F ")
            
while(true):
    if(blue.getEdges()[3].getColors!=(['red', 'blue'])):
        i = 0
        unfound = true
        while(i<4 & unfound):
            if(yellow.getEdges()[i].getColors==(['blue','red'] or ['red','blue'])):
                unfound = false
            else:
                i+=1
        if(yellow.getEdges()[i].getColors==(['red', 'blue'])):
            unmatched = true
            while(unmatched):
                yellow.rotateCW
                instructions.append("D ")
                if('red' == red.getEdges()[2].getColors()[1]):
                    unmatched = false
            #Algorithm start
            yellow.rotateCCW
            orange.rotateCW
            blue.rotateCCW
            orange.rotateCCW
            red.rotateCW
            yellow.rotateCW
            red.rotateCCW
            yellow.rotateCW
            red.rotateCCW
            orange.rotateCW
            yellow.rotateCCW
            red.rotateCW
            orange.rotateCCW
            instructions.append("!D F !L !F !B D B D B F !D !B !F ")
        if(yellow.getEdges()[i].getColors==(['blue', 'red'])):
            unmatched = true
            while(unmatched):
                yellow.rotateCW
                instructions.append("D ")
                if('blue' == blue.getEdges()[2].getColors()[1]):
                    unmatched = false
            #Algorithm start
            yellow.rotateCW
            green.rotateCCW
            red.rotateCW
            green.rotateCW
            blue.rotateCCW
            yellow.rotateCCW
            blue.rotateCW
            yellow.rotateCW
            blue.rotateCW
            green.rotateCCW
            yellow.rotateCCW
            blue.rotateCCW
            green.rotateCW
            
red.rotateCW
yellow.rotateCW
red.rotateCCW
yellow.rotateCW
red.rotateCW
yellow.rotateCW
yellow.rotateCW
red.rotateCCW
instructions.append("D !R !B R !L !D L D L !R !D !L R !B D B D R Y Y B")

lengthinst = len(instructions)
text_file = open("instructions.txt")
for i in range(lengthinst):
    text_file.write(str(instructions[i]))
text_file.close()