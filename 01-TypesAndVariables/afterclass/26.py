m = float(input('Podaj masu w kilogramach:'))
h = float(input('Podaj wzrost w metrach:'))
I = round(m / h**2, 1)
if h < 10:
    if I < 18.5:
        print(f'Masz za malo wagi, twoj pokaznik BMI: {I}')
    elif 18.5 < I < 24:
        print(f'Masz normalna wage, twoj pokaznik BMI: {I}')
    elif 24 < I:
        print(f'Masz za duzo wagi, twoj pokaznik BMI: {I}')
elif h > 10:
    print('Nie moge policzyc. Napisales wzrost w cantymetrach')