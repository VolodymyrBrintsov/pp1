a = int(input('a = '))
b = int(input('b = '))
 
def evklid(a, b): # Функція знаходження найбільшого спільного дільника
    if a % b == 0:
        return b
    else:
        return evklid(b, a%b)
 
print (evklid(a, b))