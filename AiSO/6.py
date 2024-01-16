print('Введите строку:')
c=input()
s=''
k=len(c)
for i in c:
    if k%(c.find(i)+1) == 0:
        s+=i
print(s)
