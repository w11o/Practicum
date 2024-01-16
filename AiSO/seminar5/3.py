print('Введите предложение:')
s=input()
s1=s.lower()
alf='abcdefghijklmnopqrstuvwxyz'
k=0
for i in s1[s.rfind(' ')+1:]:
    if not(i in alf):
        k=s1.find(i)
        break
if k==0:
    k=len(s)
print(s[s.rfind(' ')+1:k])
