number_dict = {
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,

    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,

    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,

    'тысяча': 1000,
    'две-тысячи': 2000,
    'три-тысячи': 3000,
    'четыре-тысячи': 4000,
    'пять-тысяч': 5000,
    'шесть-тысяч': 6000,
    'семь-тысяч': 7000,
    'восемь-тысяч': 8000,
    'девять-тысяч': 9000,

    'одна десятая': 0.1,
    'две десятые': 0.2,
    'три десятых': 0.3,
    'четыре десятых': 0.4,
    'пять десятых': 0.5,
    'шесть десятых': 0.6,
    'семь десятых': 0.7,
    'восемь десятых': 0.8,
    'девять десятых': 0.9,

    'одна сотая': 0.01,
    'две сотые': 0.02,

    'одна тысячная': 0.001,
    'две тысячные': 0.002,
    }


def get_key(value):    #получение ключа через значение
    for i, j in number_dict.items():
        if j == value: return i


def convert_digit(answer):
    #блок для чисел типа float
    if type(answer) == float: #для дробных чисел
        if len(str(answer % 1))  == 1:
            int_part = int(answer)
            div_part = round(round(answer, 3 ) - int(answer), 3)

            if int_part == 0:
                return print(f'ноль целых и {get_key(div_part)}')

            return print(f'{int_block(int_part)} и {get_key(div_part)}')

        if len(str(answer % 1))  == 2:
            int_part = int(answer)
            div_part = int(round(round(answer, 3) - int(answer), 3) * 100)
            if int_part == 0:
                return print(f'ноль целых и {int_block(div_part)} сотых')

            return print(f'{int_block(int_part)} и {int_block(div_part)} сотых')

        else:
            int_part = int(answer)
            div_part = int(round(round(answer, 3) - int(answer), 3) * 1000)
            if int_part == 0:
                return print(f'ноль целых и {int_block(div_part)} тысячных')

            return print(f'{int_block(int_part)} и {int_block(div_part)} тысячные')

    #блок для чисел типа int
    if 20 < answer < 100 and answer % 10 != 0: #с 20 до 100
        tens, units = divmod(answer, 10)  # answer // 10, answer % 10
        return print(get_key(tens * 10), get_key(units))

    elif 100 < answer < 1000 and answer % 100 != 0: #c 100 до 1000
        if answer % 10 == 0:
            return print(get_key(answer // 100 * 100), get_key(answer % 100))

        if answer % 100 < 10:
            return print(get_key(answer // 100 * 100), get_key(answer % 10))

        else:
            return print(get_key(answer // 100 * 100), get_key(answer % 100 // 10 * 10), get_key(answer % 10) )

    elif 1000 < answer < 10000: #с 1000 до 10000
        if answer % 100 == 0:
            return print(get_key(answer // 1000 * 1000), get_key(answer % 1000))

        elif answer % 10 == 0:
            return print(get_key(answer // 1000 * 1000), get_key(answer % 1000 // 100 * 100),get_key(answer % 100 // 10 * 10))

        elif answer % 100 // 10 * 10 == 0:
            return print(get_key(answer // 1000 * 1000), get_key(answer % 1000 // 100 * 100), get_key(answer % 10))

        else:
            return print(get_key(answer // 1000 * 1000), get_key(answer % 1000 // 100 * 100),
                         get_key(answer % 100 // 10 * 10), get_key(answer % 10))

    else: # c 1 до 19
        return print((get_key(answer)))





def int_block(answer):
    # блок для чисел типа int
    if 20 < answer < 100 and answer % 10 != 0:  # с 20 до 100
        tens, units = divmod(answer, 10)  # answer // 10, answer % 10
        return get_key(tens * 10) + ' ' + get_key(units)

    elif 100 < answer < 1000 and answer % 100 != 0:  # c 100 до 1000
        if answer % 10 == 0:
            return get_key(answer // 100 * 100) + ' ' +  get_key(answer % 100)

        if answer % 100 < 10:
            return  get_key(answer // 100 * 100) + ' ' + get_key(answer % 10)

        else:
            return get_key(answer // 100 * 100) + ' ' +  get_key(answer % 100 // 10 * 10) + ' ' + get_key(answer % 10)

    elif 1000 < answer < 10000:  # с 1000 до 10000
        if answer % 100 == 0:
            return get_key(answer // 1000 * 1000) + ' ' +  get_key(answer % 1000)
        elif answer % 10 == 0:
            return get_key(answer // 1000 * 1000) + ' ' +  get_key(answer % 1000 // 100 * 100) + ' ' +  get_key(answer % 100 // 10 * 10)

        elif answer % 100 // 10 * 10 == 0:
            return get_key(answer // 1000 * 1000) + ' ' +  get_key(answer % 1000 // 100 * 100) + ' ' +  get_key(answer % 10)

        else:
            return get_key(answer // 1000 * 1000) + ' ' +  get_key(answer % 1000 // 100 * 100) + ' ' +  get_key(answer % 100 // 10 * 10) + ' ' +  get_key(answer % 10)

    else:  # c 1 до 19
        return get_key(answer)





def addition(string):       #реализация операции сложения
    answer = 0

    for i in range(0, len(string)):
        if string[i] != 'плюс': answer += number_dict[string[i]]

    return convert_digit(answer)


def minus(string):       #реализация операции вычитания
    answer = 0

    for i in range(0, len(string)):
        stop = 0
        if string[i] == 'минус':
            stop = i
            break
        answer += number_dict[string[i]]

    for i in range(stop + 1, len(string)):
        answer -= number_dict[string[i]]

    return convert_digit(answer)


def multipl(string):       #реализация операции умножения
    answer = 0
    answer_1 = 0

    for i in range(0, len(string)):
        stop = 0
        if string[i] == 'умножить':
            stop = i
            break
        answer += number_dict[string[i]]

    for i in range(stop + 2, len(string)):
        answer_1 += number_dict[string[i]]

    return convert_digit(answer * answer_1)

def division(string):   #реализация операции деления
    answer = 0
    answer_1 = 0

    for i in range(0, len(string)):
        stop = 0
        if string[i] == 'разделить':
            stop = i
            break
        answer += number_dict[string[i]]

    for i in range(stop + 2, len(string)):
        answer_1 += number_dict[string[i]]

    return convert_digit(answer / answer_1)



while True:                 #основная программа
    string = input().lower().split()

    if 'плюс' in string: addition(string)

    if 'минус' in string:  minus(string)

    if 'умножить' in string: multipl(string)

    if 'разделить' in string: division(string)
