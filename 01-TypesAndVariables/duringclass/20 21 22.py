#zadania 20
import math
Promien = 5
math.pi
P = Promien**2 * math.pi
Obwod = 2*math.pi * Promien
print(f'Pole kola jest rowna: {P}, a obwod kola jest: {Obwod}')

#zadania 21
C = float(input('Podaj liczbe:'))
F = (C * 1.8) + 32
print(F)

#zadania 22
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
P = (a+b+c)/2
S = (P*(P-a)*(P-b)*(P-c))**0.5
print(S)
