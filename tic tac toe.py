maps = ['1','2','3','4','5','6','7','8','9']
end=False
moves=0
draw=False
def field():
    for i in range(0, 9, 3):
        a = ' '.join(maps[i:i+3])
        print(a)
field()

print('Введите имя игрока 1:')
name_1= input()
print('Введите имя игрока 2:')
name_2 = input()

while end < 1:

    print(f'ходит {name_1}| выбери клетку:')
    move = int(input())
    maps[move - 1] = 'X'
    moves += 1
    field()

    for i in range(0, 9, 3):
        if ''.join(maps[i:i + 3]) == 'XXX' or ''.join(maps[i:i + 3]) == 'OOO':
            end = True
    if ''.join(maps[0::3]) == 'XXX' or ''.join(maps[0::3]) == 'OOO':
        end = True
    if ''.join(maps[1::3]) == 'XXX' or ''.join(maps[1::3]) == 'OOO':
        end = True
    if ''.join(maps[2::3]) == 'XXX' or ''.join(maps[2::3]) == 'OOO':
        end = True
    if (maps[0] + maps[4] + maps[8]) == 'XXX' or (maps[0] + maps[4] + maps[8]) == 'OOO':
        end = True
    if (maps[2] + maps[4] + maps[6]) == 'XXX' or (maps[2] + maps[4] + maps[6]) == 'OOO':
        end = True

    if end == True:
        break
    if moves >= 9:
        draw = True
        break

    print(f'ходит {name_2}| выбери клетку:')
    move = int(input())
    maps[move - 1] = 'O'
    moves += 1
    field()

    for i in range(0, 9, 3):
        if ''.join(maps[i:i + 3]) == 'XXX' or ''.join(maps[i:i + 3]) == 'OOO':
            end = True
    if ''.join(maps[0::3]) == 'XXX' or ''.join(maps[0::3]) == 'OOO':
        end = True
    if ''.join(maps[1::3]) == 'XXX' or ''.join(maps[1::3]) == 'OOO':
        end = True
    if ''.join(maps[2::3]) == 'XXX' or ''.join(maps[2::3]) == 'OOO':
        end = True
    if (maps[0] + maps[4] + maps[8]) == 'XXX' or (maps[0] + maps[4] + maps[8]) == 'OOO':
        end = True
    if (maps[2] + maps[4] + maps[6]) == 'XXX' or (maps[2] + maps[4] + maps[6]) == 'OOO':
        end = True

    if moves >= 9:
        draw = True
        break
if draw == True:
    print('Ничья!')
else:
    print('Игра окончена!')

while True:
    m = 1
