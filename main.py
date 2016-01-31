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
'''
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
white.rotateCCW(Faces)






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
