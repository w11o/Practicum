def get_rows_by_number(table_name: str, start: int, stop: int, copy_table=False):
    with open(table_name, 'r', encoding='utf-8') as f:
        table = f.readlines()
        table_new = []
        for i in range(start, stop + 1):
            table_new.append(table[i - 1])

    if copy_table:
        with open(f'{table_name}_copy', 'w', encoding='utf-8') as f:
            for row in table_new:
                f.write(''.join([str(i) for i in row]))

    else:
        with open(table_name, 'w', encoding='utf-8') as f:
            for row in table_new:
                f.write(''.join([str(i) for i in row]))

#get_rows_by_number('test.csv', 1,2,1)


def get_rows_by_index(table_name: str, *args: str|int, copy_table=False):
    with open(table_name, 'r', encoding='utf-8') as f:
        column = []
        table = f.readlines()

        for i in range(len(table[0].split(','))):
            for j in table:
                column.append(j.split(',')[i].strip('"\n""\t"'))
    if copy_table:
        flag=0
        with open(f'{table_name}_copy', 'w', encoding='utf-8') as f:
            for c in args:
                if c in column and flag == 0:
                    f.write(f'{c}')
                    flag = 1
                else:
                    f.write(''.join(f',\n{c}'))

    else:
        flag = 0
        with open(f'{table_name}', 'w', encoding='utf-8') as f:
            for c in args:
                if c in column and flag == 0:
                    f.write(f'{c}')
                    flag = 1
                else:
                    f.write(''.join(f',\n{c}'))


#get_rows_by_index('test_txt', 'Анна','Иван','28',copy_table=True)


def get_column_types(table_name: str, by_number=True):
    with open(table_name, 'r', encoding='utf-8') as f:
        values = {}
        column = []
        table = f.readlines()

        for i in range(len(table[0].split(','))):
            for j in table[1:]:
                column.append(type(j.split(',')[i].strip('"\n""\t"')))
            if by_number:
                values[i + 1] = column
            else:
                values[table[0].split(',')[i].strip('"\n""\t"')] = column
            column = []
        return values
#print(get_column_types('test_txt', False))


def set_column_types(table_name: str, by_number=True, *types_dict:str):
    with open(table_name, 'r', encoding='utf-8') as f:
        values = {}
        column = []
        table = f.readlines()

        try:
            for i in range(len(table[0].split(','))):
                for j in table[1:]:
                    column.append(j.split(',')[i].strip('"\n""\t"'))
                if by_number:
                    values[i + 1] = types_dict[i]
                else:
                    values[table[0].split(',')[i].strip('"\n""\t"')] = types_dict[i]
                column = []
            return values

        except IndexError:
            return 'Ошбика!Вы задали недостаточно типов для столбцов'
#print(set_column_types('test_txt', True, 'str', 'boolean','int'))


def get_values(table_name, column=0):
    with open(table_name, 'r', encoding='utf-8') as f:
        values = {}
        clmn = []
        table = f.readlines()

        for i in range(len(table[0].split(','))):
            for j in table[1:]:
                clmn.append(j.split(',')[i].strip('"\n""\t"'))
            if type(column) == int:
                values[i + 1] = clmn

            else:
                values[table[0].split(',')[i].strip('"\n""\t"')] = clmn

            clmn = []
        return values[column]
#print(get_values('test_txt',column='Возраст'))


def get_value(table_name, column=0):
    with open(table_name, 'r', encoding='utf-8') as f:
        values = {}
        clmn = []
        table = f.readlines()

        for i in range(len(table[0].split(','))):
            for j in table[1:]:
                clmn.append(j.split(',')[i].strip('"\n""\t"'))
            if type(column) == int:
                values[i + 1] = clmn

            else:
                values[table[0].split(',')[i].strip('"\n""\t"')] = clmn

            clmn = []
        return values[column]


def set_values(table_name, column=0,*values):
    with open(table_name, 'r', encoding='utf-8') as f:
        values = {}
        clmn = []
        table = f.readlines()

        for i in range(len(table[0].split(','))):
            for j in table[1:]:
                clmn.append(j.split(',')[i].strip('"\n""\t"'))
            if type(column) == int:
                values[i + 1] = clmn

            else:
                values[table[0].split(',')[i].strip('"\n""\t"')] = clmn

            clmn = []
    with open(f'{table_name}_fnction_test', 'w', encoding='utf-8') as f:
        temp = list(values.values())
        string = ''
        for c in list(values.keys()):
            string += c + ','
        f.write(f'{string.strip(",")}\n')
        string = ''

        for j in range(len(list(values.keys()))):
            for i in range(len(list(values.keys()))):
                string += temp[i][j] + ','
            f.write(f'{string.strip(",")}\n')
            string=''




print(set_values('test_txt',column='Возраст'))