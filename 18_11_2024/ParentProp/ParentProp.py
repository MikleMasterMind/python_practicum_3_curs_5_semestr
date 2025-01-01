import sys


class Sire:
    
    @property
    def parent(self):
        return self.__class__.mro()[1].__name__
    

exec(sys.stdin.read())