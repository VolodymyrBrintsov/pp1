x = float(input('Podaj wiek pla w ludzskich latach: '))
jeden_rok_psa = 10.5 * x
rok_psa = x * 4
if x > 0 and x <= 2:
    print(f'Rok zycia psa stanowi: {jeden_rok_psa}.')
elif x > 2:
    print(f'Rok zycia psa stanowi: {rok_psa + 21}.')