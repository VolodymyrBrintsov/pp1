x = int(input('Podaj Liczbe: '))
mnoznik = 1
while mnoznik != 11 :
    y = x * mnoznik
    mnoznik += 1
    print(f'{x} x {mnoznik-1}: ',y)