nrDniaTygodnia=int(input('Podaj nr dnia tygodnia pierwszego dnia miesiąca: '))
print('| PN | WT | ŚR | CZ | PT | SB | ND |')
print(f'|    '*(nrDniaTygodnia-1), end='')
i=1

while nrDniaTygodnia+i < 9:
    print(f'|  {i} ', end='')
    i+=1
print('|')
l=0

while i < 31:
    if l != 0 and l%7 == 0:
        print('|')
    if i < 10:
        print(f'|  {i} ', end='')
        i+= 1
        l+= 1
    else:
        print(f'| {i} ', end='')
        i+= 1
        l+= 1
print('|')