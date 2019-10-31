with open('C:/Users/1/Desktop/pp1/03-FileHandling/afterclass/students.txt', 'r')as file:
    for line in file:
        line = line.split(',')
        if line[2] != 'age':
            if int(line[2]) < 30:
                print(f'{line[0]} {line[1]} {line[4]}')