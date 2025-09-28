import math

a = int(input('Zadaj cislo a zisti ci je delitelne 4 alebo 7 alebo nie '))

if a % 4 == 0 and a % 7 == 0:
    print(a,'je delitelne aj 4 aj 7')
else:
    if a % 4 == 0:
        print(a,'je delitelne 4')
    else:
        if a % 7 == 0:
            print(a,'je delitelne 7')
        else:
            print(a,'neni delitlen ani 4 ani 7')
            