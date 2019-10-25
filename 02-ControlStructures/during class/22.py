tab = [15, 8, 31, 47, 2, 19, 6]
suma = 0
n = 0


for i in tab:
    if i%2 != 0:
        suma += i
        n += 1
    
wynik = suma/n
print(f'Srednia aretmetyczna wynosi: {wynik}')