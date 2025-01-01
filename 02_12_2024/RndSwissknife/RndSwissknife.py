import random
import sys
from collections.abc import Sequence, Iterable

def rnd(a, b=None):
    match (a, b):
        case (int(), None):
            return random.randint(0, a)
        case (int(), int()):
            return random.randint(a, b)
        case (float(), float() | int()):
            return random.uniform(a, b)
        case (str(), None):
            return random.choice(a.split())
        case (str(), int()):
            i = random.randint(0, len(a) - b)
            return a[i:i + b]
        case (str(), str()):
            return random.choice(a.split(b))
        case (Sequence() | Iterable(), None):
            return random.choice(tuple(a))
        case (Sequence() | Iterable(), int()):
            return random.choices(tuple(a), k=b)


exec(sys.stdin.read())