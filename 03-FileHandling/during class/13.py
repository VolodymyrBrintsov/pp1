import re
kek = []
komunikat = 'wtorek - 23C, środa - 21C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
for x in cyfry:
    kek.append(int(x))
    srednia = sum(kek)/len(kek)
print(srednia)