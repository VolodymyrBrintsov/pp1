#zadanie 6
x = [50, 'Janusz', True, 149.17, 4*7, 4.0*7, 2>5]
for y in x:
    print(type(y))
    
#zadanie 7
x = [5 + 10*5, 3-2+1, 2+-3, 2**8, 4+4/2**2, 4%3%2%1, 1+2%3**4*5, True!=False, 2<=3 or False, not True or not False and not True,
     2<3 and 4/5 and 6+7 < 8 or not 9+10 == 19, 0b11111 >> 1 >> 1 >> 1, 0x11 + 0b11 + 11, 2 << 3 >> 4]
for y in x:
    print(y)

#zadanie 8
x = [15*38, (3+4)*(5+9), 7//2, 48%5, (8+7+4+2)/4, 2**10, 49**0.5, 80*0.25]
for y in x:
    print(y)
    
#zadanie 10
x = 7
y = 34
z = y
y = x
x = z
print(x, y)

#zadanie 11
liczba1 = 5
liczba2 = 1
liczba3 = 8
liczba4 = 6 
liczba5 = 3
x = [liczba1, liczba2, liczba3, liczba4, liczba5]
print(x[0] + x[1] + x[2] + x[3] + x[4], x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2, x[2]/x[4], x[0]%x[4],
          (x[0]+x[1])/(x[3]+x[4]),x[0]%x[2], bool(x[2] == x[4]))

#zadanie 12
uczelnia = 'Uniwersytet Ekonomiczny w Krakowie'
print(uczelnia, len(uczelnia), uczelnia[0], uczelnia[-1], uczelnia[3:9], uczelnia[0:11]+uczelnia[23:34])

#zadanie 13
x = ['a', 'b', 'c']
print(len(x), x[0], x[-1])

#zadanie 14
liczby = [2, 7, 3, 5]
print(liczby[1], sum(liczby), len(liczby),liczby[-2] ,sum(liczby)/len(liczby))
        


