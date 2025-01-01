text = str()
while s := input():
    text += ' ' + s
text = text.split()
pairs = set()
for i in range(len(text) - 1):
    pairs.add(frozenset((text[i], text[i + 1])))
print(len(pairs))