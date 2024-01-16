a = [1, 1, 1, 2, 2, 3, 7, 7, 9, 0, 1.5]; b = []
for i in a:
    if i not in b:
        b.append(i)
b = sorted(b)
print(b)