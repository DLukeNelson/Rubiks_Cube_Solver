from corner import Corner
from edge import Edge
class Face:
    def __init__(self, centre, corner1, corner2, corner3, corner4, edge1, edge2, edge3, edge4):
        ''' The corner list is indexed such that the top left corner is 0,
        and goes clockwise. The edge list is indexed such that the upper edge
        is 0, and continues clockwise.
        '''
        self.centre = centre
        self._clist = [corner1, corner2, corner3, corner4]
        self._elist = [edge1, edge2, edge3, edge4]

    def updateselfCW(self):
        # Make necessary changes to the orientations of the edges and corners
        if (self.centre is "white") or (self.centre is "yellow"):
            for i in range(4):
                self._clist[i].rotate(1, 2)
        elif (self.centre is "orange") or (self.centre is "red"):
            for i in range(4):
                self._clist[i].rotate(0, 2)
                self._elist[i].switch()
        else:
            for i in range(4):
                self._clist[i].rotate(0, 1)
            for i in range(2):
                self._elist[2*i].switch()
        #rotate the corners within the list.
        swap = self._clist[3]
        self._clist[3] = self._clist[2]
        self._clist[2] = self._clist[1]
        self._clist[1] = self._clist[0]
        self._clist[0] = swap
        # rotate the edges within the list.
        swap = self._elist[3]
        self._elist[3] = self._elist[2]
        self._elist[2] = self._elist[1]
        self._elist[1] = self._elist[0]
        self._elist[0] = swap

    def updateselfCCW(self):
        # Make necessary changes to the orientations of the edges and corners
        if (self.centre is "white") or (self.centre is "yellow"):
            for i in range(4):
                self._clist[i].rotate(1, 2)
        elif (self.centre is "orange") or (self.centre is "red"):
            for i in range(4):
                self._clist[i].rotate(0, 2)
                self._elist[i].switch()
        else:
            for i in range(4):
                self._clist[i].rotate(0, 1)

        # rotate the corners within the list.
        swap = self._clist[0]
        self._clist[0] = self._clist[1]
        self._clist[1] = self._clist[2]
        self._clist[2] = self._clist[3]
        self._clist[3] = swap
        # rotate the edges within the list.
        swap = self._elist[0]
        self._elist[0] = self._elist[1]
        self._elist[1] = self._elist[2]
        self._elist[2] = self._elist[3]
        self._elist[3] = swap

    def replaceCorner(self, idx, corner):
        self._clist[idx] = corner

    def replaceEdge(self, idx, edge):
        self._elist[idx] = edge

    def rotateCW(self, Faces):
        self.updateselfCW()
        if self.centre is 'white':
            Faces[2].replaceCorner(0, self._clist[3])
            Faces[2].replaceCorner(1, self._clist[2])
            Faces[2].replaceEdge(0, self._elist[2])
            Faces[4].replaceCorner(0, self._clist[2])
            Faces[4].replaceCorner(1, self._clist[1])
            Faces[4].replaceEdge(0, self._elist[1])
            Faces[3].replaceCorner(0, self._clist[1])
            Faces[3].replaceCorner(1, self._clist[0])
            Faces[3].replaceEdge(0, self._elist[0])
            Faces[5].replaceCorner(0, self._clist[0])
            Faces[5].replaceCorner(1, self._clist[3])
            Faces[5].replaceEdge(0, self._elist[3])
        elif self.centre is 'yellow':
            Faces[2].replaceCorner(3, self._clist[0])
            Faces[2].replaceCorner(2, self._clist[1])
            Faces[2].replaceEdge(2, self._elist[0])
            Faces[4].replaceCorner(3, self._clist[1])
            Faces[4].replaceCorner(2, self._clist[2])
            Faces[4].replaceEdge(2, self._elist[1])
            Faces[3].replaceCorner(3, self._clist[2])
            Faces[3].replaceCorner(2, self._clist[3])
            Faces[3].replaceEdge(2, self._elist[2])
            Faces[5].replaceCorner(3, self._clist[3])
            Faces[5].replaceCorner(2, self._clist[0])
            Faces[5].replaceEdge(2, self._elist[3])
        elif self.centre is 'orange':
            Faces[0].replaceCorner(3, self._clist[0])
            Faces[0].replaceCorner(2, self._clist[1])
            Faces[0].replaceEdge(2, self._elist[0])
            Faces[4].replaceCorner(0, self._clist[1])
            Faces[4].replaceCorner(3, self._clist[2])
            Faces[4].replaceEdge(3, self._elist[1])
            Faces[1].replaceCorner(1, self._clist[2])
            Faces[1].replaceCorner(0, self._clist[3])
            Faces[1].replaceEdge(0, self._elist[2])
            Faces[5].replaceCorner(1, self._clist[0])
            Faces[5].replaceCorner(2, self._clist[3])
            Faces[5].replaceEdge(1, self._elist[3])
        elif self.centre is 'red':
            Faces[0].replaceCorner(0, self._clist[1])
            Faces[0].replaceCorner(1, self._clist[0])
            Faces[0].replaceEdge(0, self._elist[0])
            Faces[4].replaceCorner(1, self._clist[0])
            Faces[4].replaceCorner(2, self._clist[3])
            Faces[4].replaceEdge(1, self._elist[3])
            Faces[1].replaceCorner(2, self._clist[3])
            Faces[1].replaceCorner(3, self._clist[2])
            Faces[1].replaceEdge(2, self._elist[2])
            Faces[5].replaceCorner(0, self._clist[1])
            Faces[5].replaceCorner(3, self._clist[2])
            Faces[5].replaceEdge(3, self._elist[1])
        elif self.centre is 'green':
            Faces[0].replaceCorner(1, self._clist[1])
            Faces[0].replaceCorner(2, self._clist[0])
            Faces[0].replaceEdge(1, self._elist[0])
            Faces[3].replaceCorner(0, self._clist[1])
            Faces[3].replaceCorner(3, self._clist[2])
            Faces[3].replaceEdge(3, self._elist[1])
            Faces[1].replaceCorner(1, self._clist[3])
            Faces[1].replaceCorner(2, self._clist[2])
            Faces[1].replaceEdge(1, self._elist[2])
            Faces[2].replaceCorner(1, self._clist[0])
            Faces[2].replaceCorner(2, self._clist[3])
            Faces[2].replaceEdge(1, self._elist[3])
        else:
            Faces[0].replaceCorner(0, self._clist[0])
            Faces[0].replaceCorner(3, self._clist[1])
            Faces[0].replaceEdge(3, self._elist[0])
            Faces[3].replaceCorner(1, self._clist[0])
            Faces[3].replaceCorner(2, self._clist[3])
            Faces[3].replaceEdge(1, self._elist[3])
            Faces[1].replaceCorner(0, self._clist[2])
            Faces[1].replaceCorner(3, self._clist[3])
            Faces[1].replaceEdge(3, self._elist[2])
            Faces[2].replaceCorner(0, self._clist[1])
            Faces[2].replaceCorner(3, self._clist[2])
            Faces[2].replaceEdge(3, self._elist[1])

    def rotateCCW(self, Faces):
        self.updateselfCCW()
        if self.centre is 'white':
            Faces[2].replaceCorner(0, self._clist[3])
            Faces[2].replaceCorner(1, self._clist[2])
            Faces[2].replaceEdge(0, self._elist[2])
            Faces[4].replaceCorner(0, self._clist[2])
            Faces[4].replaceCorner(1, self._clist[1])
            Faces[4].replaceEdge(0, self._elist[1])
            Faces[3].replaceCorner(0, self._clist[1])
            Faces[3].replaceCorner(1, self._clist[0])
            Faces[3].replaceEdge(0, self._elist[0])
            Faces[5].replaceCorner(0, self._clist[0])
            Faces[5].replaceCorner(1, self._clist[3])
            Faces[5].replaceEdge(0, self._elist[3])
        elif self.centre is 'yellow':
            Faces[2].replaceCorner(3, self._clist[0])
            Faces[2].replaceCorner(2, self._clist[1])
            Faces[2].replaceEdge(2, self._elist[0])
            Faces[4].replaceCorner(3, self._clist[1])
            Faces[4].replaceCorner(2, self._clist[2])
            Faces[4].replaceEdge(2, self._elist[1])
            Faces[3].replaceCorner(3, self._clist[2])
            Faces[3].replaceCorner(2, self._clist[3])
            Faces[3].replaceEdge(2, self._elist[2])
            Faces[5].replaceCorner(3, self._clist[3])
            Faces[5].replaceCorner(2, self._clist[0])
            Faces[5].replaceEdge(2, self._elist[3])
        elif self.centre is 'orange':
            Faces[0].replaceCorner(3, self._clist[0])
            Faces[0].replaceCorner(2, self._clist[1])
            Faces[0].replaceEdge(2, self._elist[0])
            Faces[4].replaceCorner(0, self._clist[1])
            Faces[4].replaceCorner(3, self._clist[2])
            Faces[4].replaceEdge(3, self._elist[1])
            Faces[1].replaceCorner(1, self._clist[2])
            Faces[1].replaceCorner(0, self._clist[3])
            Faces[1].replaceEdge(0, self._elist[2])
            Faces[5].replaceCorner(1, self._clist[0])
            Faces[5].replaceCorner(2, self._clist[3])
            Faces[5].replaceEdge(1, self._elist[3])
        elif self.centre is 'red':
            Faces[0].replaceCorner(0, self._clist[1])
            Faces[0].replaceCorner(1, self._clist[0])
            Faces[0].replaceEdge(0, self._elist[0])
            Faces[4].replaceCorner(1, self._clist[0])
            Faces[4].replaceCorner(2, self._clist[3])
            Faces[4].replaceEdge(1, self._elist[3])
            Faces[1].replaceCorner(2, self._clist[3])
            Faces[1].replaceCorner(3, self._clist[2])
            Faces[1].replaceEdge(2, self._elist[2])
            Faces[5].replaceCorner(0, self._clist[1])
            Faces[5].replaceCorner(3, self._clist[2])
            Faces[5].replaceEdge(3, self._elist[1])
        elif self.centre is 'green':
            Faces[0].replaceCorner(1, self._clist[1])
            Faces[0].replaceCorner(2, self._clist[0])
            Faces[0].replaceEdge(1, self._elist[0])
            Faces[3].replaceCorner(0, self._clist[1])
            Faces[3].replaceCorner(3, self._clist[2])
            Faces[3].replaceEdge(3, self._elist[1])
            Faces[1].replaceCorner(1, self._clist[3])
            Faces[1].replaceCorner(2, self._clist[2])
            Faces[1].replaceEdge(1, self._elist[2])
            Faces[2].replaceCorner(1, self._clist[0])
            Faces[2].replaceCorner(2, self._clist[3])
            Faces[2].replaceEdge(1, self._elist[3])
        else:
            Faces[0].replaceCorner(0, self._clist[0])
            Faces[0].replaceCorner(3, self._clist[1])
            Faces[0].replaceEdge(3, self._elist[0])
            Faces[3].replaceCorner(1, self._clist[0])
            Faces[3].replaceCorner(2, self._clist[3])
            Faces[3].replaceEdge(1, self._elist[3])
            Faces[1].replaceCorner(0, self._clist[2])
            Faces[1].replaceCorner(3, self._clist[3])
            Faces[1].replaceEdge(3, self._elist[2])
            Faces[2].replaceCorner(0, self._clist[1])
            Faces[2].replaceCorner(3, self._clist[2])
            Faces[2].replaceEdge(3, self._elist[1])

    def getCorners(self):
        return self._clist

    def getEdges(self):
        return self._elist

    def getCentre(self):
        return self.centre
