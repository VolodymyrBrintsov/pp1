import re
import statistics
def czytajTekst(nazwa_pliku):
    dane = []
    
    with open(nazwa_pliku)as f:
        
        for line in f:
            liczby = re.findall('\d+.\d*', line)
        
        for li in liczby:
            dane.append(float(li))
        
        return dane
kwoty = czytajTekst('wydatki.txt')


def obliczeniaSrednia(kwoty):
    Srednia = statistics.mean(kwoty)
    return Srednia
Srednia = obliczeniaSrednia(kwoty)    
def obliczeniaMediana(kwoty):    
    Mediana = statistics.median(kwoty)
    return Mediana
Mediana = obliczeniaMediana(kwoty)
def obliczeniaMinimum(kwoty):    
    Minimum = min(kwoty)
    return Minimum
Minimum = obliczeniaMinimum(kwoty)
def obliczeniaMaximum(kwoty):    
    Maximum = max(kwoty)
    return Maximum
Maximum = obliczeniaMaximum(kwoty)




def pokazWynik(kwoty,Srednia,Mediana,Minimum,Maximum):
    print(f'''Raport z wydatkow
Miesiac    Wydatki
styczen    {kwoty[0]}
luty       {kwoty[1]}
marzec     {kwoty[2]}
kwiecen    {kwoty[3]}
maj        {kwoty[4]}
cierwiec   {kwoty[5]}''')
    print(f'''
Statystyka wydatkow:
srednia {Srednia}
mediana {Mediana}
minimum {Minimum}
maximum {Maximum}''')

    print(f'''
Graficzna reprezentacja wydatkow:
styczen    {int(kwoty[0]/100)*'#'}
luty       {int(kwoty[1]/100)*'#'}
marzec     {int(kwoty[2]/100)*'#'}
kwiecen    {int(kwoty[3]/100)*'#'}
maj        {int(kwoty[4]/100)*'#'}
cierwiec   {int(kwoty[5]/100)*'#'}''')
pokazWynik(kwoty,Srednia,Mediana,Minimum,Maximum)    

  











