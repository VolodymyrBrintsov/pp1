ld = int(input('Podaj liczbe dziesieta: '))
wynik = []
while ld > 0.4:
    wynik.append(int(ld%2))
    ld = ld/2
print(*wynik[::-1],sep='')