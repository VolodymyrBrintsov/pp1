from math import ceil

def wskaznikBMI():
    wzrost = float(input('Podaj wzrost w cm: '))
    waga = float(input('Podaj wagę w kilogramach: '))
    możliwa_waga = []
    możliwy_wzrost = []
    od_wzrost = 150
    od_waga = 40
    
    while od_wzrost != 221:
        możliwy_wzrost.append(od_wzrost)
        od_wzrost += 1
    
    while od_waga != 151:
        możliwa_waga.append(od_waga)
        od_waga += 1
    
    assert ceil(wzrost) in możliwy_wzrost, "wzrost nie w cm!"
    assert ceil(waga) in możliwa_waga, "za duża lub za mala waga."
    
    return round(waga/(wzrost/100)**2,1)

print(wskaznikBMI())
        