tab = [32, 16, 5, 8, 24, 7]
with open("C:/Users/1/Desktop/pp1/03-FileHandling/tablica.txt" ,'a') as file:
    for i in tab:
        file.write(f'{i}\n')
