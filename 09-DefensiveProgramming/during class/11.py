def sprawdżWiek(wiek):
    if type(wiek) != int:
        raise TypeError('Wiek powinien być liczbą całkowitą!')
    print(f'Masz {wiek} lat')
    
sprawdżWiek('5')