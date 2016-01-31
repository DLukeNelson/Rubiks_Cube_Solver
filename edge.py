class Edge:
    '''Stores two colors and their relative orientation.'''

    def __init__ (self, col1, col2):
        '''This pair is ordered such that the top or bottom facing part,
        of the piece comes first, and the front or back facing part is before a
        left or right facing part.
        '''
        self._alist = [col1, col2]

    def switch(self):
        '''If the edge is moved, the order must be swapped.'''
        swap = self._alist[0]
        self._alist[0] = self._alist[1]
        self._alist[1] = swap

    def getColors(self):
        return self._alist
