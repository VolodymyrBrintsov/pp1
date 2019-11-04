def suma(N):
    Liczby = []
    l = 1
    while l != N+1:
        Liczby.append(l)
        l += 1
    print(sum(Liczby))
print(suma(500))