x = float(input('Podaj kropku x: '))
y = float(input('Podaj kropku y: '))
if x > 0 and y > 0:
    print(f'Punkt{x, y} znajduje sie w Pierwszej ćwiartce układu współrzędnych.')
elif x > 0 and y < 0:
    print(f'Punkt{x, y} znajduje sie w Czwartej ćwiartce układu współrzędnych.')
elif x < 0 and y > 0:
    print(f'Punkt{x, y} znajduje sie w Drugiej ćwiartce układu współrzędnych.')
elif x < 0 and y < 0:
    print(f'Punkt{x, y} znajduje sie w Trzecziej ćwiartce układu współrzędnych.')