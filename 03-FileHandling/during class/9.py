with open("C:/Users/s-115-19/Desktop/pp1/03-FileHandling/shoppinglist.txt", "a") as file:
    x = 'x'
    while x != "":
        x = input('Podaj nazwe produktu: ')
        file.write(f"{x}\n")
    file.close()