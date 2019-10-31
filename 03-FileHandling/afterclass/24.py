tab=[['Imie','Nazwisko','E-mail'],['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'
],['Piotr','Wyga','wygap@gop.pl']]

with open('C:/Users/1/Desktop/pp1/03-FileHandling/afterclass/csv.csv', 'w')as file:
        for i in tab:
            for x in i:
                if x != i[-1]:
                    print(f'{x},')
                else:
                    print(f'{x}\n')4