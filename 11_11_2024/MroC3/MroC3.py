import sys


def parse_classes(lines):
    classes = {}

    for line in lines:
        if line.startswith("class "):
            parts = line.split('(')
            class_name = parts[0].split()[1].rstrip(':')
            parent_classes = []
            if len(parts) > 1:
                parent_part = parts[1].rstrip(' pass\n').rstrip('):')
                parent_classes = [p.strip() for p in parent_part.split(',')]
            classes[class_name] = parent_classes

    return classes

def c3_mro(classes):
    test_classes = dict()
    for class_name in classes:
        parents = classes[class_name].copy()
        test_parents = tuple(test_classes[parent] for parent in parents)
        test_classes[class_name] = type(class_name, test_parents, dict())
        test_classes[class_name].mro()


input_code = sys.stdin.readlines()
try:
    c3_mro(parse_classes(input_code))
except (KeyError, TypeError):
    print('No')
else:
    print('Yes')
