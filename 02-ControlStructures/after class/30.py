PIN = '0805'
count = 0
while count != 3:
    wpr_PIN = input('Podaj PIN: ')
    if wpr_PIN != PIN:
        count +=1
        print('Nieprawidlowy PIN!')
print('Karta zablokowana!')
