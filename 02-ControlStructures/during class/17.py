L = [i for i in range(51)]
L.remove(0)
suma_parzystych = 0
suma_nieparzystych = 0
for x in L:
    if x%2 == 0:
        suma_parzystych += x
    elif x%2 != 0:
        suma_nieparzystych += x
print(f'Suma nieparzystych sklada: {suma_nieparzystych}, a suma parzystych: {suma_parzystych}')
