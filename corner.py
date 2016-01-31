class Corner:
    '''Stores three colors and their relative orientation'''

    def __init__ (self, col1, col2, col3):
        '''This list is ordered from the top/bottom color, to the front/back
        color, to the left/right color.
        '''
        self._alist = [col1, col2, col3]

    def rotate(self, a, b):
        '''If the corner is rotated CW, the list must be reordered.'''
        swap = self._alist[a]
        self._alist[a] = self._alist[b]
        self._alist[b] = swap

    def getColors(self):
        return self._alist
