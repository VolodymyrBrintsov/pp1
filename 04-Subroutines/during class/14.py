Liczba = 23
Tablica = [15, 38, 7, 23, 14]
def spr():
    if Liczba in Tablica:
        for x in Tablica:
            print(Tablica[Liczba[x]])
    else:
        print(f'Liczba: {Liczba}')
        print(f'Tablica: {Tablica}')
        print('Podanej liczby nie ma w tablicy')
spr()