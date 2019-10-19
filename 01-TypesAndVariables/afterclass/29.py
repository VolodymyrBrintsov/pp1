import random
Oczki = int(input('Podaj, ile oczek kostki wyrzucił komputer:'))
Comp = random.randint(1, 6)
print(f'Computer wyrzucil:{Comp}')
if Oczki < 7:
    if Oczki == Comp:
        print(bool(Oczki == Comp))
    elif Oczki != Comp:
        print(bool(Oczki == Comp))
else:
    print('Podaj cos od 1 do 6')