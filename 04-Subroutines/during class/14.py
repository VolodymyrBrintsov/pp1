Liczba = 23
Tablica = [15, 38, 7, 23, 14]
def spr():
    if Liczba in Tablica:
        print(f'Liczba: {Liczba}')
        print(f'Tablica: ',*Tablica, sep=" ")
        print('Podana liczba jest w tablicy')
    else:
        print(f'Liczba: {Liczba}')
        print(f'Tablica: {Tablica}')
        print('Podanej liczby nie ma w tablicy')
spr()