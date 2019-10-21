tab = [15, 8, 31, 47, 2, 19]
suma = 0
n = len(tab)


for i in tab:
    if i%2 != 0:
        suma += i
    
wynik = suma/n
print(f'Srednia aretmetyczna wynosi: {wynik}')