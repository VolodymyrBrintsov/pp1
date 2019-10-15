NR = input()
print(f'Podaj NR konta: {NR}')
if len(NR)<26:
    print('Nieprawidlowe')
elif len(NR)>26:
    print('Nieprawidlowe')
elif len(NR)==26:
    print('Numer konta: ', encrypt(NR,4))