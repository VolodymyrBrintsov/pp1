def f():
    x = y
    x[1] = y[0] + x[1]
x = [1,2,3]
y = [4,5]
f()
print(x,y)