import random
L = []
for x in range(20):
    x = random.randint(-20,-5)
    L.append(x)
print(*L, sep=" ")
