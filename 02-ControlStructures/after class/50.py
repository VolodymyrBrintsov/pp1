ld = int(input('Podaj liczbe dziesieta: '))
ld10 = ld
wynik = []
wynik = wynik[::-1]

if ld > 4:
    while ld > 1:
        wynik.append(int(ld%2))
        ld = ld/2
elif ld < 5:
    while ld > 0.4:
        wynik.append(int(ld%2))
        ld = ld/2
print('{}(10) = {}(2)'.format(ld10, " ".join(map(str, wynik[::-1]))))