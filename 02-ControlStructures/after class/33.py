Tablica = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
podane_l = str(input('Podaj liczbe: '))
for x in range(0, len(podane_l)):
    print(Tablica[int(podane_l[x])], end=' ')