tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
maximus = max(tab, key = tab.count)
tab.sort()
mediana = len(tab)/2
print(f'Mediana: {tab[int(mediana)]}, dominanta: {maximus}')