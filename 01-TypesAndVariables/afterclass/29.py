import random
Oczki = int(input('Podaj, ile oczek kostki wyrzucił komputer:'))
Comp = random.randint(1, 6)
print(f'Computer wyrzucil:{Comp}')
if Oczki == Comp:
    print(bool(Oczki == Comp))
elif Oczki != Comp:
    print(bool(Oczki == Comp))
