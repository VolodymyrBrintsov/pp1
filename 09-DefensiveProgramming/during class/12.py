def sprawdżWiek(wiek):
    if type(wiek) != int or 120 < wiek or wiek < 0:
        raise ValueError("Weik powinien być dodatną liczbą całkowitą mniejszą od 120!")
    print(f'Masz {wiek} lat')
    
sprawdżWiek('5')