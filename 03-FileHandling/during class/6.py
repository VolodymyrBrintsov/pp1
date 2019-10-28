i = 1
with open("C:/Users/s-115-19/Desktop/pp1/03-FileHandling/NoEducation.txt" ,'r') as file:
    for line in file:
        print(f'{i} {line}', end='')
        i += 1