print('Введите строку:')
s=input()
a=['']*4
a[0]=s[:s.find('-')]
a[1]=s[s.rfind('-')+1:s.find('=')]
a[2]=s[s.rfind('=')+1:s.find('_')]
a[3]=s[s.rfind('_')+1:]
print(a)
