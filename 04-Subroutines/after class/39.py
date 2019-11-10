def sprawdz(x,y):
    zakres = []
    podane = int(input('Podaj liczbe: '))
    x1 = x
    if x<y:
        while x != y+1:
            zakres.append(x)
            x += 1
    elif x>y:
        while x != y-1:
            zakres.append(x)
            x -= 1
    if podane in zakres:
        print(f'Liczba {podane} jest w zakresie od {x1}, {y}.')
        print(zakres)
    elif podane not in zakres:
        print(f'Liczby {podane} nie ma w zakresie od {x1}, {y}')
sprawdz(12,10)
    