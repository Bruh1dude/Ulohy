import math
a = int(input('Zadaj cislo a'))
b = int(input('Zadaj cislo b'))
x = int(input('Zadaj cislo a zisti ci je v intervale a,b'))

if a>x and b<x or b>x and a<x:
    print(x,'je v intervale',a,b)
else:
    print(x,'neni v intervale',a,b)

