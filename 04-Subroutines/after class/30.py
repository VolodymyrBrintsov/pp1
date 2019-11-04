import random
def los():
    parzyste = []
    nieparzyste = []
    for x in range(1000):
        x = random.randint(1,50)
        if x%2 == 0:
            parzyste.append(x)
        elif x%2 == 1:
            nieparzyste.append(x)
    procent_parz = len(parzyste)/10
    procent_nieparz = len(nieparzyste)/10
    print(f'''Dla 1000 liczb losowych z przedzialu <1,50>:
liczby parzyste: {procent_parz}%
liczby nieparzyste: {procent_nieparz}%
    ''')
los()