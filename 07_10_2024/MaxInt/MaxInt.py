maxint = None
while s := input():
    for a in s.split():
        if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
            maxint = max(maxint, int(a)) if maxint != None else int(a)
print(maxint if maxint else 0)