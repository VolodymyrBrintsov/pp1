def podatek(dochod):
    podatek = 0
    if dochod <= 5000:
        podatek = 5000*0.17
        print(f'Podatek należny: {podatek}')
    elif dochod > 5000:
        nadbawka = dochod - 5000
        nadbawka = nadbawka * 0.32
        podatek = nadbawka + 5000*0.17
        print(f'Podatek należny: {podatek}')
podatek(int(input('Podaj dochod: ')))