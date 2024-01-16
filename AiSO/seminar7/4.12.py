a = []
while True:
    print('Введите значение: ')
    b = input().split(',')

    for i in b:
        if i in a:
            print(f'значение {i} уже есть')


    for i in b:
        if i not in a and i != '':
            a.append(i)
            if len(a) > 5:
                print(f'был превышен лимит, извлечено: {a.pop(0)}')


    if '' in b:
        print(f'Содержимое мешка {a}')
        break

    print(a)
