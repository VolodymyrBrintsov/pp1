x1 = int(input('Podaj kwote w zlotych: '))
j=[]
d=[]
p=[]
x = x1
while x != 0:
    if x>4:
        p.append(x//5)
        x = x%5
    elif x == 1:
        j.append(x//1)
        x = x%1
    else:
        d.append(x//2)
        x = x%2        
print(f'''Kwota {x1} zl w monetach:
5 zl - {', '.join(map(str, p))} szt
2 zl - {', '.join(map(str, d))} szt
1 zl - {', '.join(map(str, j))} szt''')    