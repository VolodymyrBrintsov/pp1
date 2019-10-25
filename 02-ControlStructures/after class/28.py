for i in range(10):
        if i==0 or i==9:
            for j in range(20):
                print('-',end='')
        else:
            print('|',end='')
            for j in range(1,19):
                print(' ',end='')
            print('|',end='')
        print()

    