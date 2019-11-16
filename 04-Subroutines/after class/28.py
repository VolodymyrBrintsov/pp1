def rysujWykres(x,y):
    for i in range(0,10):
        a=11-len(x[i])
        wartosc=int(y[i])//3
        print(' '*a+f'{x[i]}:',end=' ')
        print('#'*wartosc)
        
    
jezyki=['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
wartosci=[61,47,37,32,26,18,14,14,9,7]

rysujWykres(jezyki,wartosci)