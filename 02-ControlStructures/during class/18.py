import random
Pogo = random.randint(1,30)
if Pogo%3 == 0 and Pogo%5 == 0:
    print(f'{Pogo} BINGO')
elif Pogo%3 == 0:
    print(f'{Pogo} THREE')
elif Pogo%5 == 0:
    print(f'{Pogo} FIVE')
print(Pogo)