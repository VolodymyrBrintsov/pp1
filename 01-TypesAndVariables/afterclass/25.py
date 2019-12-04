NR = input('Podaj numer karty bankowej:')
NR = str(NR)
p_NR = NR[0:2] + " " + NR[2:6] + " " + NR[6:10] + " " + NR[10:14] + " " + NR[14:18] + " " + NR[18:22] + " " + NR[22:26]
if len(NR) < 26:
    print('Nie prawidlowy numer')
elif len(NR) > 26:
    print('Nie prawidlowy numer')
elif len(NR) == 26:
    print ("Numer kartki: ",p_NR)
    
for x in range(26):
    print(1, end= '')