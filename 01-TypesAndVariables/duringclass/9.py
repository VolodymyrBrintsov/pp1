#zadania 9
import random
for x in range(int(input(f'Ilosc rzutow:'))):
    
    print('1: ' ,random.random())
    print('2: ' ,random.randrange(0, 100))
    print('3: ', random.randint(5,10))
    Kolory = ['karo', 'kier', 'pik', 'trefl']
    print('4: ' ,random.choice(Kolory))