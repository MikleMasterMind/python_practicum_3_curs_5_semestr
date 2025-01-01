
import sys


class AnnoDoc(type):
    def __new__(cls, name, bases, attrs):
        
        new_doc = attrs.get('__doc__', None)
        annotations = attrs.get('__annotations__', {})
        new_annotations = {}
        
        for key, value in annotations.items():
            if key in attrs:
                new_annotations[key] = type(attrs[key])

            if isinstance(value, str):
                if not new_doc:
                    new_doc = f'{key}: {value}'
                else:
                    new_doc += f'\n{key}: {value}'
                
        attrs['__annotations__'] = new_annotations
        attrs['__doc__'] = new_doc
        
        return super().__new__(cls, name, bases, attrs)


exec(__import__('sys').stdin.read())