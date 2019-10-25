for i in range(10):
    if i < 5:
        print(i*'*')
    elif i > 5:
        while i != 1:
            i -= 1
            print(i * '*')