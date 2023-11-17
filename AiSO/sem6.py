#1
'''
main = [31, 24, 17]

first = main.copy(); print(f'первый список:{main}')

second = [i for i in main]; print(f'второй список: {second}')

third = first + second; print(f'первый + второй список: {third}')
'''


#2.1/2.2/2.3
'''
a = input()

print(list(a))

print(a.split())

print([i for i in a if i.isdigit()])
'''




#3
'''
a = input().split()
if a[-1].isdigit(): a[-1] = int(a[-1])

b = []

if a[-2] == 'repeat' and str(a[-1]).isdigit():
    for _ in range(a[-1]):
        b.extend(a[:-2])

    b.append(a[-2]); b.append(a[-1])
    print(b)
'''




#4


#5.1/5.2
'''
print('Enter two integers')

max_val = int(input())
repeat = int(input())
a, b, c = [], [], []

for i in range(repeat):
    for j in range(1, max_val + 1):
        a.append(j)
print(f'5.1 solve: {a}')

if max_val == 10:
    print()
    left = repeat
    right = - repeat
    b.extend(a[:left]); b.extend(a[right:])
    c.extend(a[left:right])
    print(f'5.2 solve:\nbegin and end of list: {b}\nmiddle of list: {[i * 10 for i in c]}')
'''

#8
'''
a = input().split()
b = input().split()
c = []

for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])
print(c)
'''



#9
'''a = input().split()
b = input().split()
c = list(zip(a, b))

for i in range(len(c)):
    print(*c[i], end = ' ')'''



#10
'''
a = input().split()

n = int(input())

b = a[: n]

a = a[n:]; a.extend(b); print(*a)
'''

#12 не закончено
'''
a = input().split()
for i in range(len(a)):
    for j in range(len(a)):
        if int(a[i]) <= int(a[j]) and i != j:
            print(a[i], a[j])
'''


#17
'''print(sorted(input().split()))'''
