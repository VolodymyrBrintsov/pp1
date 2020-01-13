from math import sqrt

def sqrtLiczby():
    try:
        liczba = float(input('Podaj liczbę: '))
        print(f'sqrt({liczba}) = {sqrt(liczba)}')
    except:
        print('Proszę podaj liczbę wiekszą od 0')
        
sqrtLiczby()