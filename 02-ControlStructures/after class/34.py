pesel=str(input('Podaj pesel: '))

if int(pesel[9])%2==1:
    plec='kobieta'
else:
    plec='mężczyzna'
if int(pesel[2])>1:
    rok=2000+int(pesel[0:2])
else:
    rok=1900+int(pesel[0:2])
wiek=2018-rok

print(f'Płeć: {pesel}')
print(f'Płeć: {plec}')
print(f'Wiek: {wiek}')