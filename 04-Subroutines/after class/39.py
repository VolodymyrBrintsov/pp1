def sprawdz():
    x = int(input('Podaj od jakiej liczby zaczyna zakres: '))
    y = int(input('Podaj koniec zakres: '))
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
    elif podane not in zakres:
        print(f'Liczby {podane} nie ma w zakresie od {x1}, {y}')
sprawdz()
    