i = 1
with open("C:/Users/1/Desktop/pp1/03-FileHandling/NoEducation.txt" ,'r') as file:
    for line in file:
        print(f'{i} {line}', end='')
        i += 1