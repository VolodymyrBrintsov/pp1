def potenga(x,n):
    if n == 1:
        return 1
    if n > 1:
        return x * x**(n-1)
print(print(f'5 do potęgi 3 wynosi {potenga(5,3)}'))