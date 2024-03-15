def generate_desk():
    return ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', ] + ['p']*8 + ['.']*32 + ['P']*8 + ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', ]


def print_desk(desk):
    print(*[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], end='\n')
    y_coord = 9
    for i in range(0, 57, 8):
        y_coord-=1
        print(y_coord, *desk[i: i+8], y_coord)
    print(*[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], end='\n')


def is_your_figure(desk: list, side: str):
    x = input()
    if side == 'white': #for white
        if desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] not in 'PRNBQK':
            while desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] not in 'PRNBQK':
                print('Input Error!')
                x = input()
        if desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] in 'PRNBQKBNR':
            return x

    if side == 'black': #for black
        if desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] not in 'prnbqk':
            while desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] not in 'prnbqk':
                print('Input Error!')
                x = input()
        if desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] in 'prnbqk':
            return x


def eat_or_move(desk: list, side: str):
    x = input()
    if side == 'white': #for white
        if desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] in 'PRNBQKBNR':
            while desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] in 'PRNBQKBNR':
                print('Input Error!')
                x = input()
        if desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] not in 'PRNBQKBNR':
            return x

    if side == 'black': #for black
        if desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] in 'prnbqk':
            while desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] in 'prnbqk':
                print('Input Error!')
                x = input()
        if desk[-(int(x[1]) * 8) + (int(x[0], 18) - 10)] not in 'prnbqk':
            return x

def pawn_move(point_1, desk, move_counter):
    #[-(int(x1[1]) * 8) + (int(x1[0], 18) - 10)], -(int(x1[1]) * 8) + (int(x1[0], 18) - 10)| курсор для выбора фигуры(Белые)
    if move_counter % 2 == 1: # для белых

        print('select the second cell|white')
        while True:
            x2 = eat_or_move(desk, 'white')
            point_2 = -(int(x2[1]) * 8) + (int(x2[0], 18) - 10)
            if point_1 - 8 == point_2 and desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter
            if point_1 - 7 == point_2 and  desk[point_2] in 'prnbqk':
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

            print('Wrong Pawn move!')
            return figure(desk, move_counter)

    if move_counter % 2 == 0:   #для черных

        print('select the second cell|black')
        while True:
            x2 = eat_or_move(desk, 'black')
            point_2 = -(int(x2[1]) * 8) + (int(x2[0], 18) - 10)
            if point_1 + 8 == point_2 and desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter
            if point_1 + 7 == point_2 and desk[point_2] in 'PRNBQK':
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

            print('Wrong Pawn move!')
            return figure(desk, move_counter)


def bishop_move(x1, point_1, desk, move_counter, side, figures):
    #[-(int(x1[1]) * 8) + (int(x1[0], 18) - 10)], -(int(x1[1]) * 8) + (int(x1[0], 18) - 10)| курсор для выбора фигуры(Белые)

    print(f'select the second cell|{side}')
    while True:
        x2 = eat_or_move(desk, side)
        point_2 = -(int(x2[1]) * 8) + (int(x2[0], 18) - 10)
        start = min(point_1, point_2)
        end = max(point_1, point_2)


        if abs(point_1 - point_2) % 8 == 0:

            for i in range(start + 8, end, 8):
                if desk[i] != '.':
                    print('Wrong Bishop move!')
                    return figure(desk, move_counter)
            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        if int(x1[1]) * 8 - 7 <= abs(point_2) <= int(x1[1]) * 8:
            for i in range(start + 1, end):
                if desk[i] != '.':
                    print('Wrong Bishop move!')
                    return figure(desk, move_counter)

            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        print('Wrong Bishop move!')
        return figure(desk, move_counter)


def B_move(x1, point_1, desk, move_counter, side, figures):

    print(f'select the second cell|{side}')
    while True:
        x2 = eat_or_move(desk, side)
        point_2 = -(int(x2[1]) * 8) + (int(x2[0], 18) - 10)
        start = min(point_1, point_2)
        end = max(point_1, point_2)


        if abs(point_1 - point_2) % 7 == 0:

            for i in range(start + 7, end, 7):
                if desk[i] != '.':
                    print('Wrong B move!')
                    return figure(desk, move_counter)
            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        if abs(point_1 - point_2) % 9 == 0:
            for i in range(start + 9, end, 9):
                if desk[i] != '.':
                    print('Wrong B move!')
                    return figure(desk, move_counter)

            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        print('Wrong B move!')
        return figure(desk, move_counter)


def N_move(x1, point_1, desk, move_counter, side, figures):

    print(f'select the second cell|{side}')
    while True:
        x2 = eat_or_move(desk, side)
        point_2 = -(int(x2[1]) * 8) + (int(x2[0], 18) - 10)
        check = abs(point_1 - point_2)


        if check == 17 or check == 15 or check == 10 or check == 6:

            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        print('Wrong Knight move!')
        return figure(desk, move_counter)


def K_move(x1, point_1, desk, move_counter, side, figures):
    print(f'select the second cell|{side}')
    while True:
        x2 = eat_or_move(desk, side)
        point_2 = -(int(x2[1]) * 8) + (int(x2[0], 18) - 10)
        check = abs(point_1 - point_2)


        if check == 8 or check == 7 or check == 9:

            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        print('Wrong Queen move!')
        return figure(desk, move_counter)


def Q_move(x1, point_1, desk, move_counter, side, figures):
    print(f'select the second cell|{side}')
    while True:
        x2 = eat_or_move(desk, side)
        point_2 = -(int(x2[1]) * 8) + (int(x2[0], 18) - 10)
        start = min(point_1, point_2)
        end = max(point_1, point_2)
        check = abs(point_1 - point_2)
        #block R
        if abs(point_1 - point_2) % 8 == 0:

            for i in range(start + 8, end, 8):
                if desk[i] != '.':
                    print('Wrong Queen move!')
                    return figure(desk, move_counter)
            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        if int(x1[1]) * 8 - 7 <= abs(point_2) <= int(x1[1]) * 8:
            for i in range(start + 1, end):
                if desk[i] != '.':
                    print('Wrong Queen move!')
                    return figure(desk, move_counter)

            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        #block B
        if abs(point_1 - point_2) % 7 == 0:

            for i in range(start + 7, end, 7):
                if desk[i] != '.':
                    print('Wrong Queen move!')
                    return figure(desk, move_counter)
            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        if abs(point_1 - point_2) % 9 == 0:
            for i in range(start + 9, end, 9):
                if desk[i] != '.':
                    print('Wrong Queen move!')
                    return figure(desk, move_counter)

            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter

        #block K
        if check == 8 or check == 7 or check == 9:

            if desk[point_2] == '.':
                desk[point_1], desk[point_2] = desk[point_2], desk[point_1]
                return desk, move_counter

            if desk[point_2] in figures:
                desk[point_2] = desk[point_1]
                desk[point_1] = '.'
                return desk, move_counter



        print('Wrong Queen move!')
        return figure(desk, move_counter)

def figure(desk, move_counter):    #определение выбранной фигуры
    if move_counter % 2 == 1:  # для белых
        print('select the first cell|white')
        x1 = is_your_figure(desk, 'white')
        point_1 = -(int(x1[1]) * 8) + (int(x1[0], 18) - 10)
        if desk[point_1] == 'R':
            bishop_move(x1, point_1, desk, move_counter, side='white', figures ='prnbqk')

        if desk[point_1] == 'P':
            pawn_move(point_1, desk, move_counter)

        if desk[point_1] == 'B':
            B_move(x1, point_1, desk, move_counter, side='white', figures ='prnbqk')

        if desk[point_1] == 'N':
            N_move(x1, point_1, desk, move_counter, side='white', figures ='prnbqk')

        if desk[point_1] == 'K':
            K_move(x1, point_1, desk, move_counter, side='white', figures ='prnbqk')

        if desk[point_1] == 'Q':
            Q_move(x1, point_1, desk, move_counter, side='white', figures ='prnbqk')

    if move_counter % 2 == 0:  # для черных
        print('select the first cell|black')
        x1 = is_your_figure(desk, 'black')
        point_1 = -(int(x1[1]) * 8) + (int(x1[0], 18) - 10)
        if desk[point_1] == 'r':
            bishop_move(x1, point_1, desk, move_counter, side='black', figures ='PRNBQK')

        if desk[point_1] == 'p':
            pawn_move(point_1, desk, move_counter)

        if desk[point_1] == 'b':
            B_move(x1, point_1, desk, move_counter, side='black', figures ='PRNBQK')

        if desk[point_1] == 'n':
            N_move(x1, point_1, desk, move_counter, side='black', figures ='PRNBQK')

        if desk[point_1] == 'k':
            K_move(x1, point_1, desk, move_counter, side='black', figures ='PRNBQK')

        if desk[point_1] == 'Q':
            Q_move(x1, point_1, desk, move_counter, side='black', figures ='PRNBQK')


desk = generate_desk()
print_desk(desk)
move_counter = 1
print()
while True:
    figure(desk, move_counter)
    print_desk(desk)
    move_counter = 1



