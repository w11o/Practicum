import random
r_digit = random.randint(1, 9999)
r_digit = str(r_digit)
if len(r_digit) < 4:
    while len(r_digit) != 4:
        r_digit = '0' + r_digit
bik = 0
korova = 0
print(r_digit)
while bik != 4:
    bik, korova = 0, 0
    print('Введите четырехзначное число:')
    t = str(input())
    while True:
        if len(t) != 4:
            print('Число должно быть четырехзначным')
            print('Введите число еще раз:')
            t = str(input())
        if len(t) == 4:
            break
    for i in range (0, len(r_digit)):
        if t[i] == r_digit[i]:
            bik += 1
        if t[i] in r_digit:
            korova += 1
    print('Быки =', bik, 'Коровы =', korova)
print('Win')

while True:
    m = 1
