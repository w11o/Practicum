field=('- ' * 20).split()
for i in range(0, 6):
    field.append(i)
fine_p1=0
fine_p2=0
fine_p3=0
def fld():
    b=0
    print('  ', end='')
    for i in range(1, 6):
        print(i, end = ' ')
    print()

    for i in range(0, 16, 5):
        b+=1
        print(b, *field[i:i+5])

    print()
    print()
fld()


print('Player 1|Enter name:')
name_1 = input()
print('Player 1|Enter your symbol:')
symbol_1 = input()

print('Player 2|Enter name:')
name_2 = input()
print('Player 2|Enter your symbol:')
symbol_2 = input()

print('Player 3|Enter name:')
name_3 = input()
print('Player 3|Enter your symbol:')
symbol_3 = input()

fld()

while True:
    #первый игрок
    print('Player 1|Enter coordinates:')
    move_1 = input()
    while len(move_1.split()) != 2:
        print('Please, enter coordinates like 1 2:')
        move_1 = input()
    b = move_1.split() #coordinates
    a = int(b[0]) * 5 + int(b[1]) - 6 #position of symbol
    field[a] = symbol_1
    fld()

    if field[a] == field[a + 1] or field[a] == field[a - 1] or field[a] == field[a - 5] or field[a] == field[a + 5]:
        fine_p1 += 1
    if field[a] == field[a - 6] or field[a] == field[a + 6]:
        fine_p1 += 1
    if '-'not in field:
        break

    #второй игрок


    print('Player 2|Enter coordinates:')
    move_2 = input()
    while len(move_2.split()) != 2:
        print('Please, enter coordinates like 1 2:')
        move_2 = input()
    b = move_2.split() #coordinates
    a = int(b[0]) * 5 + int(b[1]) - 6 #position of symbol
    field[a] = symbol_2
    fld()

    if field[a] == field[a + 1] or field[a] == field[a - 1] or field[a] == field[a - 5] or field[a] == field[a + 5]:
        fine_p1 += 1
    if field[a] == field[a - 6] or field[a] == field[a + 6]:
        fine_p1 += 1
    if '-'not in field:
        break

    #третий игрок

    print('Player 3|Enter coordinates:')
    move_3 = input()
    while len(move_3.split()) != 2:
        print('Please, enter coordinates like 1 2:')
        move_3 = input()
    b = move_3.split()  # coordinates
    a = int(b[0]) * 5 + int(b[1]) - 6  # position of symbol
    field[a] = symbol_3
    fld()

    if field[a] == field[a + 1] or field[a] == field[a - 1] or field[a] == field[a - 5] or field[a] == field[a + 5]:
        fine_p3 += 1
    if field[a] == field[a - 6] or field[a] == field[a + 6]:
        fine_p3 += 1

    if '-'not in field:
        break
#проверка выйгрыша

if min(fine_p1, fine_p2, fine_p3) == fine_p1:
    print(f'{name_1} win')

if min(fine_p1, fine_p2, fine_p3) == fine_p2:
    print(f'{name_2} win')

if min(fine_p1, fine_p2, fine_p3) == fine_p3:
    print(f'{name_3} win')

if fine_p1 == fine_p2 == fine_p3:
    print('draw')
while True: #чтобы работало в консоли
    m = 1

