Ocena = [1, 2, 3, 4, 5, 6]
x = int(input('Podaj ocene: '))
for x in Ocena:
    if x != Ocena:
        print('Wrong number')
    elif x == Ocena:
        print('Good')