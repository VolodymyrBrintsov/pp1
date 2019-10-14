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