
def mix(*args):
    class C: 
        def __str__(self):
          attrs = {attr: getattr(self, attr) for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith('_')}
          return ', '.join(f'{attr}={val}' for attr, val in sorted(attrs.items()))

    mixed = C()
  
    for obj in args:
        for attr in dir(obj):
            if not callable(getattr(obj, attr)) and not attr.startswith('_'):
              setattr(mixed, attr, getattr(obj, attr))

    return mixed

exec(__import__("sys").stdin.read(), globals())