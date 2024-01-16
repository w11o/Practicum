print('Введите 1 строку:')
a=input().lower()
print('Введите 2 строку:')
b=input().lower()
for i in a:
    if i in b:
        b1=b.replace(i, i.upper(), 1)
        print(a.find(i)+1, 'символ встречается в строке поиска:', b1)
