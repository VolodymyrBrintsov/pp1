imiona = ['Janek', 'Ania', 'Wojtek', 'Zosia']
def jestImie(imie,imiona):
    if imie in imiona:
        print(f'Imiona: ',*imiona)
        print('Imie: ', imie)
        print('Rezultat: imię zawarte jest w wykazie imion.')
    
jestImie('Janek', imiona)