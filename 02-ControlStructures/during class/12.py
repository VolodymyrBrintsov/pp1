x = int(input('Podaj Liczbe: '))
y = int(input('Podaj Liczbe: '))
if x < 0 and y < 0:
    print('Obe liczby sa ujemnymi')
elif x > 0 and y < 0:
    print('Pierwsza liczba dodtnia, a druga ujemna')
elif x > 0 and y > 0:
    print('Dwie liczby sa dodatnie')
else:
    print('Pierwsza liczba ujemna, a druge ujemna')