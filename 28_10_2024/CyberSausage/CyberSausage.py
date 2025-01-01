from fractions import Fraction
import sys

class Sausage:
    
    mince = 12
    
    def __init__(self, filling="pork!", volume=1):
        self.filling = filling
        self.volume = Fraction(volume) 
        self.length = self.mince + 2

    def __str__(self):

        if self.volume == 0:
            return "/|\n||\n||\n||\n\\|"
        
        full_sandwich = int(self.volume)
        other = self.volume - full_sandwich
        filling_ssusage = (self.filling * (12 // len(self.filling))) + self.filling[:12 % len(self.filling)]
        up = f"/{"-" * self.mince}\\" * full_sandwich
        body = f"|{filling_ssusage}|" * full_sandwich
        down = f"\\{"-" * self.mince}/" * full_sandwich
        other_len = int(other * self.mince)
        if other:
            up += ("/" + "-" * (other_len) + "|")
            body += f"|{filling_ssusage[:int(other * self.mince)]}|"
            down += "\\" + "-" * (other_len) + "|"

        result = ''
        result += up
        result += '\n'
        for _ in range(3):
            result += body
            result += '\n'
        result += down

        return result

    
    def __add__(self, other):
        return Sausage(self.filling, self.volume + other.volume)
    
    def __sub__(self, other):
        return Sausage(self.filling, max(self.volume - other.volume, 0))
    
    def __mul__(self, other):
        return Sausage(self.filling, self.volume * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        return Sausage(self.filling, self.volume / other)
    
    def __abs__(self):
        return self.volume
    
    def __bool__(self):
        return self.volume > 0


exec(sys.stdin.read())