dct = {1: 'яблоки', 2: 'бананы', 3: 'груши'}
lst = ['груши', 'яблоки']
res = []

for c in lst:
    for i, j in dct.items():
        if c ==  j:
            res.append(c)

print(*res)


