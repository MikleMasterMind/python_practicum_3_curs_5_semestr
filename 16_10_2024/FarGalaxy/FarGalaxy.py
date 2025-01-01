galaxys = dict()
s = input()
while " " in s:
    s = s.split()
    coord = tuple(map(float, s[:-1]))
    galaxys[coord] = s[-1]
    s = input()  
maxdits = 0
maxgal = list()
other_galaxys = set(galaxys.keys())
for gal1 in galaxys:
    other_galaxys.remove(gal1)
    for gal2 in other_galaxys:
        dist = sum((gal1[i] - gal2[i])*(gal1[i] - gal2[i]) for i in range(3))
        if dist > maxdits:
            maxdits = dist
            maxgal = list((galaxys[gal1], galaxys[gal2]))
maxgal.sort()
print(*maxgal)