import re
tab = input('Podaj ciag znakow: ')
def wielkieLitery():
    y = ''
    x = re.findall('[A-Z]', tab)
    for i in x:
        y += i + ", "
    print(f'Wielkie litery: {y}')
wielkieLitery()