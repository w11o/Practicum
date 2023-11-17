field = ('- ' * 100).split()
#for i in range(21):
#    field.append(' ')
end = False
lose_1, lose_2 = 0, 0
nine = []

for j in range(9, 90, 10):
    nine.append(j)
print(nine)

def fld():
    print('  ', end = '')

    for i in range(1, 11):
        print(i, end = ' ')

    print()

    b=-1
    for i in range(0, 100, 10):
        b+=1
        print(b, *field[i:i+10])

    print()
    print()
fld()
print('Enter player 1 name:')
name_1 = input()

print('Enter player 2 name:')
name_2 = input()

while True:
    #игрок 1
    print(f'{name_1}, enter coordinates:')
    move_1 = (input()).split()

    while len(move_1) != 2:
        print(f'{name_1}, enter coordinates, like: 1 2:')
        move_1 = ((input()).split())

    field[int(move_1[0]) * 10 + int(move_1[1]) - 1] = 'X'
    fld()

    #проверка вправо влево
    for i in range(0, 98):
       if (field[i] != '-' and field[i + 1] != '-' and field[i + 2] != '-') and i not in nine :
           end = 1
           lose_1 += 1
           print('ENDGAME')

    #проверка вверх вниз
    for j in range(0, len(field) - 20):
        if field[j] != '-' and field[j + 10] != '-' and field[j + 20] != '-':
            end = 1
            lose_1 += 1
            print('ENDGAME')

    #проверка по диагонали
    for j in range(0, len(field) - 21):
        if field[j] != '-' and field[j + 11] != '-' and field[j + 22] != '-':
            end = 1
            lose_1 += 1
            print('ENDGAME')

        if field[j] != '-' and field[j + 9] != '-' and field[j + 18] != '-':
            end = 1
            lose_1 += 1
    if end == 1:
        break


    #игрок 2

    print(f'{name_2}, enter coordinates:')
    move_2 = (input()).split()

    while len(move_2) != 2:
        print(f'{name_1}, enter coordinates, like: 1 2:')
        move_2 = ((input()).split())

    field[int(move_2[0]) * 10 + int(move_2[1]) - 1] = 'Y'
    fld()

    # проверка вправо влево
    for i in range(0, 98):
        if (field[i] != '-' and field[i + 1] != '-' and field[i + 2] != '-') and i not in nine:
            end = 1
            lose_2 += 1
            print('ENDGAME')

    # проверка вверх вниз
    for j in range(0, len(field) - 20):
        if field[j] != '-' and field[j + 10] != '-' and field[j + 20] != '-':
            end = 1
            lose_2 += 1
            print('ENDGAME')

    # проверка по диагонали
    for j in range(0, len(field) - 21):
        if field[j] != '-' and field[j + 11] != '-' and field[j + 22] != '-':
            end = 1
            lose_2 += 1
            print('ENDGAME')

        if field[j] != '-' and field[j + 9] != '-' and field[j + 18] != '-':
            end = 1
            lose_2 += 1
    if end == 1:
        break


if lose_1 == 1:
    print(f'{name_2} wins!')
if lose_2 == 1:
    print(f'{name_1} wins!')
if lose_1 == lose_2:
    print('draw')
