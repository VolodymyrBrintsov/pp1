##1
def fib(n):
    a,b = 0,1
    count = 1
    while count != n:
        a,b = b, a+b
        count += 1
        print(f'{a}', end=" ")
print(fib(20))


##2
def fib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
        print(a, end=" ")
        
fib(20)