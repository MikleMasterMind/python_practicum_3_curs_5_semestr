import sys


class ExceptionTree:
    def __init__(self):
        self.exceptions = dict()

    def __call__(self, n):
        if n in self.exceptions:
            return self.exceptions[n]

        # Определяем имя класса исключения
        class_name = f"Exception-{n}"
        
        # Определяем родительский класс
        possible_parent = n // 2
        while possible_parent > 0:
            if possible_parent in self.exceptions:
                parent_class = self.exceptions[possible_parent]
                break
            possible_parent //= 2
        else:
            parent_class = Exception
        
        # Создаем новый класс исключения
        new_exception = type(class_name, (parent_class,), {'n': n})
        
        # Сохраняем созданный класс в словаре
        self.exceptions[n] = new_exception
        return new_exception
    
    
exec(sys.stdin.read())