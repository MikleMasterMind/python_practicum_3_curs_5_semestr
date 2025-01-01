from collections.abc import Sequence
from sys import stdin


class NegExt:
    def __neg__(self):
        # Получаем родительский класс
        parent_class = self.__class__.mro()[2]
        
        # Проверяем, есть ли у родителя метод __neg__
        if hasattr(parent_class, '__neg__'):
            return self.__class__(super().__neg__())  # Вызываем унарный минус у родителя

        # Проверяем, есть ли у родителя операция секционирования
        if hasattr(parent_class, '__getitem__'):
            # Возвращаем секцию [1:-1]
            try:
                return self.__class__(self[1:-1])
            except KeyError: # если есть метод getitem который не может обработать slice
                pass    

        # В противном случае возвращаем сам объект
        return self.__class__(self)
    
    
exec(stdin.read())