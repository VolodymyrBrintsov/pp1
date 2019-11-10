tab = list(input('Podaj tablice: '))
def reverse(tab):
    tab_reverse = tab[::-1]
    print(f'Tablica: {tab}, jej odwrotna tablica: {tab_reverse}')
reverse(tab)