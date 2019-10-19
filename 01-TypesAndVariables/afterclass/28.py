import random
x = int(input('Ile chces zevy komputer zrobil rzutow?')) #ilosc rzutow
suma = [] #zeby mozna bylo wykorztstac .append
for y in range(x): 
        los = random.randint(1,6) #wykorzystamy jeden random zeby rezultaty byli jednymi
        suma.append(los) #dodajemy rezultat do sumy
        print('Wyrzucone liczby to : {0}'.format(los))
print('Suma wyrzuconych liczb: ', sum(suma)) #dodajemy rezultaty