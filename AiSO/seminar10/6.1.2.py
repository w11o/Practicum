from math import *
def cathetus_2(gip, kat1):
    if gip <= kat1:
        return 'Данные введены некорректно'
    return 'Длина второго катета: ' + str(sqrt(gip**2-kat1**2))
a, b = map(int, input().split())
print(cathetus_2(a, b))
