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
The following section initializes a default (solved) cube.
'''


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
