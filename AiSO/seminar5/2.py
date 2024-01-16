print('Введите предложение:')
s=input()
s1=s.lower()
alf='abcdefghijklmnopqrstuvwxyz'
for i in s1:
    if not(i in alf):
        k=s1.find(i)
        break
print(s[:k])
