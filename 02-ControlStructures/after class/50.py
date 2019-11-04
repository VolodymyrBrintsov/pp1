def dec_to_bin():
    ld = int(input('Напиши сюда свой десятичный код: '))
    ld10 = ld
    wynik = []
    wynik = wynik[::-1]

    if ld > 4:
        while ld > 1:
            wynik.append(int(ld%2))
            ld = ld/2
    elif ld < 5:
        while ld > 0.5:
            wynik.append(int(ld%2))
            ld = ld/2
    print('успешное превращение из {}(10) в {}(2)'.format(ld10, "".join(map(str, wynik[::-1]))))
dec_to_bin()