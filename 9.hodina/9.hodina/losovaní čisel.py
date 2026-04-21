los = list(range(1,33))
los2 = []
print(los)
pruchod = 0

import random
for i in range(len(los)):
    while True:
        cislo = random.randint(0,31)
        pruchod += 1
        if los[cislo] != None:
            los2.append(los[cislo])
            los[cislo] = None
            break

print(pruchod)
print(los2)


