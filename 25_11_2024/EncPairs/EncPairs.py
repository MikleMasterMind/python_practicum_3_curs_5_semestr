import sys
from itertools import product

cods = ["KOI8-R", "CP1251", "MACCYRILLIC", "CP866", "ISO-8859-5", "CP855"]

data = sys.stdin.buffer.read()
for cod1, cod2, cod3 in product(cods, repeat=3):
    try:
        result = data.decode(cod1).encode(cod2).decode(cod3)
        if 'Зимбабве' in result:
            print(result)
            break
    except Exception:
        pass