import random
Szóstka = [0]
Piątka = [0]
Czwórka = [0]
Trójka = [0]
Dwójka= [0]
Jedynka= [0]
for y in range(100):
    x = random.randint(1,6)
    print(x)
    if x == 1:
        Jedynka.append(x)
    elif x == 2:
        Dwójka.append(x)
    elif x == 3:
        Trójka.append(x)
    elif x == 4:
        Czwórka.append(x)
    elif x == 5:
        Piątka.append(x)
    else:
        Szóstka.append(x)
print('Jedynka: ',Jedynka.count(1))
print('Dwójka: ',Dwójka.count(2))
print('Trójka: ', Trójka.count(3))
print('Czwórka: ', Czwórka.count(4))
print('Piątka: ', Piątka.count(5))
print('Szóstka: ', Szóstka.count(6))