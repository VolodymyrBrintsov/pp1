from math import sqrt

def sqrtLiczby():
    while True:
        try:
            liczba = float(input('Podaj liczbę: '))
            print(f'sqrt({liczba}) = {sqrt(liczba)}')
            break
        except:
            print('Proszę podaj liczbę wiekszą od 0')
        
sqrtLiczby()