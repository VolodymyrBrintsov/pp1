print('Podaj masu w kilogramach')
m = float(input())
print('Podaj wzrost w metrach')
h = float(input())
I = round(m / h**2, 1)
if h < 3.5:
    if I < 18.5:
        print(f'Masz za malo wagi, twoj pokaznik BMI: {I}')
    elif 18.5 < I < 25:
        print(f'Masz normalna wage, twoj pokaznik BMI: {I}')
    elif 24 < I:
        print(f'Masz za duzo wagi, twoj pokaznik BMI: {I}')
elif h > 3.5:
    print('Nie moge policzyc. Napisales wzrost w cantymetrach')