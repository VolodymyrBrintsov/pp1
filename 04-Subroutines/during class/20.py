def potenga(x,n):
    if n == 1:
        return 1
    if n > 1:
        return x * x**(n-1)
print(potenga(5,3))