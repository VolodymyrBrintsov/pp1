def quadra():
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    c = int(input('Podaj c: '))
    D = ((b)**2 - 4 * a * c)**(1/2)
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)
    print(x1,x2)
quadra()