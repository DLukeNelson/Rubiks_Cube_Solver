class edge:
    '''Stores two colors and their relative orientation.'''

    def __init__ (self):
        '''This pair is ordered such that the top or bottom facing part,
        of the piece comes first, and the front or back facing part is before a
        left or right facing part.
        '''
        self._alist = list()

    def switch(self):
        '''If the edge is moved, the order must be swapped.'''
        swap = self._alist[0]
        self._alist[0] = self._alist[1]
        self._alist[1] = swap
