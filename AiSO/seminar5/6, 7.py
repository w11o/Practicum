def pr(s):
    a=['']*3
    if s.rfind('.')>s.rfind('@'):
        a[0]=s[:s.rfind('@')]
        a[1]=s[s.rfind('@')+1:s.rfind('.')]
        a[2]=s[s.rfind('.')+1:]
        print(s, '- корректный email')
        print('Домен:', a[1])
        return True
    return False

print('Введите строку:')
s=input()
b=s.split()
for i in b:
    if pr(i):
        print()
