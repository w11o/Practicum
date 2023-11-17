from random import randint

field = []          #создаем переменные
for i in range(64):
    field.append('-')
end = True
dots = randint(15, 64)
dist = randint(1, 2)
begin = randint(0, 10)
win_p1 = False
win_p2 = False

def fld():          #создаем поле
    b = 0
    for i in range(0, 64, 8):
        b += 1
        print(b, ' '.join(field[i:i + 8]))
    print('  ', end = '')
    for i in range(97, 105):
        print(chr(i), end = ' ')
    print()
    print()

for i in range (begin, dots, dist):         #создаем рандомайзер для игрового поля
    field[i] = 'O'

print('Enter player 1 name:')
name_1 = input()

print('Enter player 2 name:')
name_2 = input()

fld()
while True:
    print(f'|move {name_1}|')
    print('Enter horizontal(vertical):')
    move = input()

    if move in '0123456789':            #удаление горизонталей
        move = int(move)
        field[move * 8 - 8 : move * 8] = '-' * 8

    elif move in 'abcdefgh':            #удаление вертикалей
        for i in range(0, 64, 8):
            if move == 'a':
                field[i] = '-'
            if move == 'b':
                field [i + 1] = '-'
            if move == 'c':
                field [i + 2] = '-'
            if move == 'd':
                field [i + 3] = '-'
            if move == 'e':
                field [i + 4] = '-'
            if move == 'f':
                field [i + 5] = '-'
            if move == 'g':
                field [i + 6] = '-'
            if move == 'h':
                field [i + 7] = '-'

    if ''.join(field) == '-' * 64:          #проверка на окончание игры
        fld()
        win_p1 += 1
        break
    fld()




    print(f'|move {name_2}|')
    print('Enter horizontal(vertical):')
    move = input()

    if move in '0123456789':            #удаление горизонталей
        move = int(move)
        field[move * 8 - 8 : move * 8] = '-' * 8

    elif move in 'abcdefgh':            #удаление вертикалей
        for i in range(0, 64, 8):
            if move == 'a':
                field[i] = '-'
            if move == 'b':
                field [i + 1] = '-'
            if move == 'c':
                field [i + 2] = '-'
            if move == 'd':
                field [i + 3] = '-'
            if move == 'e':
                field [i + 4] = '-'
            if move == 'f':
                field [i + 5] = '-'
            if move == 'g':
                field [i + 6] = '-'
            if move == 'h':
                field [i + 7] = '-'

    if ''.join(field) == '-' * 64:          #проверка на окончание игры
        fld()
        win_p2 += 1
        break
    fld()
if win_p1 == 1:
    print(f'{name_1} won')
if win_p2 == 1:
    print(f'{name_2} won')

while True:
    m = 1
