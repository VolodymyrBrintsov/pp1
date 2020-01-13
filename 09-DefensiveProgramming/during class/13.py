def wyznaćCenuBrutto(netto):
    if type(netto) != int and type(netto) != float or netto < 0:
        raise ValueError('netto musi byc dodatną liczbą!')
    print(round(netto*0.23 + netto, 2))
    
wyznaćCenuBrutto(15.6)
