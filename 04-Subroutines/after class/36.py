tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
def oshuk(tab):
    rezultat = []
    for i in tab:
        if type(i) == list:
            rezultat.append(i)
            oshuk(i)
    print(**rezultat)
oshuk(tab)