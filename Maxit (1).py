from random import randint
import time
sum_1, sum_2 = 0, 0
fld = []
#name_1, name_2 = input(), input()
print('|M A X I T|')
for i in range(4):
    print('loading', 25 * i, '%' )
    time.sleep(1)
print()
print('Please, enter your names')
print()

print('Player 1:')
name_1 = input()

print('Player 2:')
name_2 = input()

print(100 * '\n')

for i in range(9):
    fld.append(randint(0, 9))
end=0
lose_p1, lose_p2 = 0, 0
def field():                  #создание поля
    print(100 * '\n')
    b=0
    print('   ',1, 2 , 3)
    print()
    for j in range(0, 9, 3):
        b+=1
        print(b,' ', *fld[j:j + 3])

field()                                  #задание координат
print(f'{name_1}|Enter coordinates:')
move_1 = input().split()

while True:
    if len(move_1) != 2:
        print(f'{name_1}|Enter coordinates like 1 2:')
        move_1 = input().split()
    else:
        break

a = int(move_1[0]) * 3 - 4 + int(move_1[1])         #ход первого игрока
sum_1 += fld[a]
fld [a] = '-'
field()


while end == 0:
                    #ход второго игрока
    print(f'{name_2}|Enter coordinates:')
    move_2 = input().split()

    while True:
        if len(move_2) != 2:
            print(f'{name_1}|Enter coordinates like 1 2:')
            move_2 = input().split()
        else:
            break

    while True:
        d = int(move_2[0]) * 3 - 4 + int(move_2[1])

        if a + 3 == d or a - 3 == d or a + 6 == d or a - 6 == d:
            sum_2 += fld[d]
            fld [d] = '-'
            field()
            break

        else:
            print('Take another digit :)')
            move_2 = input().split()

            while True:
                if len(move_2) != 2:
                    print('user_name_2,enter coordinates like 1 2')
                    move_2 = input().split()
                else:
                    break

            field()

        # проверка на наличие ходов
    stroka = fld[int(move_2[0]) * 3 - 3:int(move_2[0]) * 3]
    if stroka == ['-', '-', '-']:
        break


                    #ход первого игрока
    print(f'{name_1}|Enter coordinates:')
    move_1 = input().split()

    while True:
        if len(move_1) != 2:
            print(f'{name_1}|Enter coordinates like 1 2:')
            move_1 = input().split()
        else:
            break


    while True:
        a = int(move_1[0]) * 3 - 4 + int(move_1[1])

        stroka = fld[int(move_2[0]) * 3 - 3:int(move_2[0]) * 3]

        if fld[a] in stroka:
            sum_1 += fld[a]
            fld[a] = '-'
            field()
            break

        else:
            print('Take another digit :)')
            move_1 = input().split()

            while True:
                if len(move_1) != 2:
                    print(f'{name_1}|Enter coordinates like 1 2:')
                    move_1 = input().split()
                else:
                    break

            field()
    #проверка столбца

    if a < 3:
        if str(fld[a]) + str(fld[a+3]) + str(fld[a+6]) == '---':
            end = 1

    if 3 <= a < 6:
        if str(fld[a - 3]) + str(fld[a]) + str(fld[a + 3]) == '---':
            end = 1

    if a > 5:
        if str(fld[a - 6]) + str(fld[a - 3]) + str(fld[a]) == '---':
            end = 1



if sum_1 > sum_2:
    print(f'{name_1}, your sum is {sum_1}, you win!')
    print()
    print(f'Sum {name_2} was {sum_2}')
if sum_1 < sum_2:
    print(f'{name_2}, your sum is {sum_2}, you win!')
    print()
    print(f'Sum {name_1} was {sum_1}')
if sum_1 == sum_2:
    print('Draw')
    print()
    print(f'Your sum was {sum_1}')
while True:
    a = True
