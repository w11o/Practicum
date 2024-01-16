print('Введите предложение:')
s=input().lower()
a=[' ']*(s.count(' ')+1)
alf='abcdefghijklmnopqrstuvwxyz'
alf1='aeiouy'
n=0
for i in s:
    if i in alf:
        a[n]+=i
    elif i==' ':
        n+=1
for i in a:
    if i[0] in alf1:
        print(i)
print(a)
