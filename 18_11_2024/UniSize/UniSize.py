import sys


def sizer(cls):
    class SizeDescriptor:
        def __init__(self):
            self._size_value = None
        
        def __get__(self, instance, owner):
            if self._size_value is not None:
                return self._size_value
            
            if instance is None:
                return self
            
            # Определяем поведение для получения размера
            if hasattr(instance, '__len__'):
                return len(instance)
            elif hasattr(instance, '__abs__'):
                return abs(instance)
            else:
                return 0
        
        def __set__(self, instance, value):
            self._size_value = value
            
        def __delete__(self, instance):
            self._size_value = None

    # Добавляем дескриптор в класс
    cls.size = SizeDescriptor()
    return cls


exec(sys.stdin.read())