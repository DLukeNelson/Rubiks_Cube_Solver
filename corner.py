class corner:
    '''Stores three colors and their relative orientation'''

    def __init__ (self):
        '''This list is ordered from the top/bottom color, to the front/back
        color, to the left/right color.
        '''
        self._alist = list()

    def rotate(self, a, b):
        '''If the corner is rotated CW, the list must be reordered.'''
        swap = self._alist[a]
        self._alist[a] = self._alist[b]
        self._alist[b] = swap
