import sys


class vector:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return ":".join(str(x) for x in self.data)

    def __add__(self, other):
        return vector([x + y for x, y in zip(self.data, other)])
    
    def __radd__(self, other):
        return self + other

    def __matmul__(self, other):
        return sum(x * y for x, y in zip(self.data, other))

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.data)

exec(sys.stdin.read())