import sys

class Square:
    __match_args__ = 'x', 'y', 'w'
    
    def __init__(self, x, y, w):
        self._x, self._y = x, y
        self._w = w
        self._center = [x + self._w / 2, y + self._w / 2]
        self._s = w * w
    
    @property
    def s(self):
        return self._s
    
    @s.setter
    def s(self, val):
        pass
    
    @property
    def center(self):
        return tuple(self._center)
    
    @center.setter
    def center(self, new_center):
        if len(new_center) == 2:
            self._center = list(new_center)
        elif len(new_center) == 4:
            self._center = [new_center[0] + new_center[2], new_center[1] + new_center[3]]
        self._x = self._center[0] - self._w / 2
        self._y = self._center[1] - self._w / 2
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, val):
        self._x = val
        self._center = [self._x + self._w / 2, self._x + self._w / 2]
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, val):
        self._y = val
        self._center = [self._x + self._w / 2, self._y + self._w / 2]
            
    @property
    def w(self):
        return self._w
    
    @w.setter
    def w(self, val):
        self._w = val
        self._center = [self._x + self._w / 2, self._y + self._w / 2]
        self._s = self._w * self._w
    
    @property
    def h(self):
        return self._w
    
    @h.setter
    def h(self, val):
        self._w = val
        self._center = [self._x + self._w / 2, self._y + self._w / 2]
        self._s = self._w * self._w
    

exec(sys.stdin.read())