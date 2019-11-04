def suma(n):
    if n==0 or n==1:
        return 1
    if n > 1:
        return n + suma(n-1)
print(suma(500))