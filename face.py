from corner import corner
from edge import edge
class face:
    def __init__(self, color):
        ''' The corner list is indexed such that the top left corner is 0,
        and goes clockwise. The edge list is indexed such that the upper edge
        is 0, and continues clockwise.
        '''
        self.centre = color
        self._clist = list()
        self._elist = list()

    def updateselfCW(self):
        #rotate the corners within the list.
        swap = self.clist[3]
        self.clist[3] = self.clist[2]
        self.clist[2] = self.clist[1]
        self.clist[1] = self.clist[0]
        self.clist[0] = swap
        # rotate the edges within the list.
        swap = self.elist[3]
        self.elist[3] = self.elist[2]
        self.elist[2] = self.elist[1]
        self.elist[1] = self.elist[0]
        self.elist[0] = swap

        # Make necessary changes to the orientations of the edges and corners
        if (self.centre is "white") or (self.centre is "yellow"):
            for i in range(4):
                self.clist[i].rotate(1, 2)
        elif (self.centre is "orange") or (self.centre is "red"):
            for i in range(4):
                self.clist[i].rotate(0, 2)
        else:
            for i in range(4):
                self.clist[i].rotate(0, 1)

    def updateselfCCW(self):
        # rotate the corners within the list.
        swap = self.clist[0]
        self.clist[0] = self.clist[1]
        self.clist[1] = self.clist[2]
        self.clist[2] = self.clist[3]
        self.clist[3] = swap
        # rotate the edges within the list.
        swap = self.elist[0]
        self.elist[0] = self.elist[1]
        self.elist[1] = self.elist[2]
        self.elist[2] = self.elist[3]
        self.elist[3] = swap

        # Make necessary changes to the orientations of the edges and corners
        if (self.centre is "white") or (self.centre is "yellow"):
            for i in range(4):
                self.clist[i].rotate(1, 2)
        elif (self.centre is "orange") or (self.centre is "red"):
            for i in range(4):
                self.clist[i].rotate(0, 2)
        else:
            for i in range(4):
                self.clist[i].rotate(0, 1)

    def replaceCorner(self, idx, corner):
        self._clist[idx] = corner

    def replaceEdge(self, idx, edge):
        self._elist[idx] = edge

    def rotateCW(self):
        updateselfCW()
        if self.color is 'white':
            orange.replaceCorner(0, self._clist[3])
            orange.replaceCorner(1, self._clist[2])
            orange.replaceEdge(0, self._elist[2])
            green.replaceCorner(0, self._clist[2])
            green.replaceCorner(1, self._clist[1])
            green.replaceEdge(0, self._elist[1])
            red.replaceCorner(0, self._clist[1])
            red.replaceCorner(1, self._clist[0])
            red.replaceEdge(0, self._elist[0])
            blue.replaceCorner(0, self._clist[0])
            blue.replaceCorner(1, self._clist[3])
            blue.replaceEdge(0, self._elist[3])
        elif self.color is 'yellow':
            orange.replaceCorner(3, self._clist[0])
            orange.replaceCorner(2, self._clist[1])
            orange.replaceEdge(2, self._elist[0])
            green.replaceCorner(3, self._clist[1])
            green.replaceCorner(2, self._clist[2])
            green.replaceEdge(2, self._elist[1])
            red.replaceCorner(3, self._clist[2])
            red.replaceCorner(2, self._clist[3])
            red.replaceEdge(2, self._elist[2])
            blue.replaceCorner(3, self._clist[3])
            blue.replaceCorner(2, self._clist[0])
            blue.replaceEdge(2, self._elist[3])
        elif self.color is 'orange':
            white.replaceCorner(3, self._clist[0])
            white.replaceCorner(2, self._clist[1])
            white.replaceEdge(2, self._elist[0])
            green.replaceCorner(0, self._clist[1])
            green.replaceCorner(3, self._clist[2])
            green.replaceEdge(3, self._elist[1])
            yellow.replaceCorner(1, self._clist[2])
            yellow.replaceCorner(0, self._clist[3])
            yellow.replaceEdge(0, self._elist[2])
            blue.replaceCorner(1, self._clist[0])
            blue.replaceCorner(2, self._clist[3])
            blue.replaceEdge(1, self._elist[3])
        elif self.color is 'red':
            white.replaceCorner(0, self._clist[1])
            white.replaceCorner(1, self._clist[0])
            white.replaceEdge(0, self._elist[0])
            green.replaceCorner(1, self._clist[0])
            green.replaceCorner(2, self._clist[3])
            green.replaceEdge(1, self._elist[3])
            yellow.replaceCorner(2, self._clist[3])
            yellow.replaceCorner(3, self._clist[2])
            yellow.replaceEdge(2, self._elist[2])
            blue.replaceCorner(0, self._clist[1])
            blue.replaceCorner(3, self._clist[2])
            blue.replaceEdge(3, self._elist[2])
        elif self.color is 'green':
            white.replaceCorner(1, self._clist[1])
            white.replaceCorner(2, self._clist[0])
            white.replaceEdge(1, self._elist[0])
            red.replaceCorner(0, self._clist[1])
            red.replaceCorner(3, self._clist[2])
            red.replaceEdge(3, self._elist[1])
            yellow.replaceCorner(1, self._clist[3])
            yellow.replaceCorner(2, self._clist[2])
            yellow.replaceEdge(1, self._elist[2])
            orange.replaceCorner(1, self._clist[0])
            orange.replaceCorner(2, self._clist[3])
            orange.replaceEdge(2, self._elist[3])
        else:
            white.replaceCorner(0, self._clist[0])
            white.replaceCorner(3, self._clist[1])
            white.replaceEdge(3, self._elist[0])
            red.replaceCorner(1, self._clist[0])
            red.replaceCorner(2, self._clist[3])
            red.replaceEdge(1, self._elist[3])
            yellow.replaceCorner(0, self._clist[2])
            yellow.replaceCorner(3, self._clist[3])
            yellow.replaceEdge(3, self._elist[2])
            orange.replaceCorner(0, self._clist[1])
            orange.replaceCorner(3, self._clist[2])
            orange.replaceEdge(3, self._elist[1])

    def rotateCCW(self):
        updateselfCCW()
        if self.color is 'white':
            orange.replaceCorner(0, self._clist[3])
            orange.replaceCorner(1, self._clist[2])
            orange.replaceEdge(0, self._elist[2])
            green.replaceCorner(0, self._clist[2])
            green.replaceCorner(1, self._clist[1])
            green.replaceEdge(0, self._elist[1])
            red.replaceCorner(0, self._clist[1])
            red.replaceCorner(1, self._clist[0])
            red.replaceEdge(0, self._elist[0])
            blue.replaceCorner(0, self._clist[0])
            blue.replaceCorner(1, self._clist[3])
            blue.replaceEdge(0, self._elist[3])
        elif self.color is 'yellow':
            orange.replaceCorner(3, self._clist[0])
            orange.replaceCorner(2, self._clist[1])
            orange.replaceEdge(2, self._elist[0])
            green.replaceCorner(3, self._clist[1])
            green.replaceCorner(2, self._clist[2])
            green.replaceEdge(2, self._elist[1])
            red.replaceCorner(3, self._clist[2])
            red.replaceCorner(2, self._clist[3])
            red.replaceEdge(2, self._elist[2])
            blue.replaceCorner(3, self._clist[3])
            blue.replaceCorner(2, self._clist[0])
            blue.replaceEdge(2, self._elist[3])
        elif self.color is 'orange':
            white.replaceCorner(3, self._clist[0])
            white.replaceCorner(2, self._clist[1])
            white.replaceEdge(2, self._elist[0])
            green.replaceCorner(0, self._clist[1])
            green.replaceCorner(3, self._clist[2])
            green.replaceEdge(3, self._elist[1])
            yellow.replaceCorner(1, self._clist[2])
            yellow.replaceCorner(0, self._clist[3])
            yellow.replaceEdge(0, self._elist[2])
            blue.replaceCorner(1, self._clist[0])
            blue.replaceCorner(2, self._clist[3])
            blue.replaceEdge(1, self._elist[3])
        elif self.color is 'red':
            white.replaceCorner(0, self._clist[1])
            white.replaceCorner(1, self._clist[0])
            white.replaceEdge(0, self._elist[0])
            green.replaceCorner(1, self._clist[0])
            green.replaceCorner(2, self._clist[3])
            green.replaceEdge(1, self._elist[3])
            yellow.replaceCorner(2, self._clist[3])
            yellow.replaceCorner(3, self._clist[2])
            yellow.replaceEdge(2, self._elist[2])
            blue.replaceCorner(0, self._clist[1])
            blue.replaceCorner(3, self._clist[2])
            blue.replaceEdge(3, self._elist[2])
        elif self.color is 'green':
            white.replaceCorner(1, self._clist[1])
            white.replaceCorner(2, self._clist[0])
            white.replaceEdge(1, self._elist[0])
            red.replaceCorner(0, self._clist[1])
            red.replaceCorner(3, self._clist[2])
            red.replaceEdge(3, self._elist[1])
            yellow.replaceCorner(1, self._clist[3])
            yellow.replaceCorner(2, self._clist[2])
            yellow.replaceEdge(1, self._elist[2])
            orange.replaceCorner(1, self._clist[0])
            orange.replaceCorner(2, self._clist[3])
            orange.replaceEdge(2, self._elist[3])
        else:
            white.replaceCorner(0, self._clist[0])
            white.replaceCorner(3, self._clist[1])
            white.replaceEdge(3, self._elist[0])
            red.replaceCorner(1, self._clist[0])
            red.replaceCorner(2, self._clist[3])
            red.replaceEdge(1, self._elist[3])
            yellow.replaceCorner(0, self._clist[2])
            yellow.replaceCorner(3, self._clist[3])
            yellow.replaceEdge(3, self._elist[2])
            orange.replaceCorner(0, self._clist[1])
            orange.replaceCorner(3, self._clist[2])
            orange.replaceEdge(3, self._elist[1])
