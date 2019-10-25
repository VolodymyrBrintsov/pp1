ld = int(input('Podaj liczbe dziesieta: '))
wynik = []
while ld > 1:
    wynik.append(int(ld%2))
    ld = ld/2
print(*wynik[::-1],sep='')