limit_predkosci = int(input('Podaj limit predkosci (km/h): '))
predkosc_pojazdu = int(input('Podaj predkosc pojazdu (km/h): '))
n = predkosc_pojazdu - limit_predkosci
mandat = 0
if n < 10:
    mandat = n * 5
elif n > 10:
    mandat = 50+( n-10)* 15
print('Mandat (zl): ', mandat)
