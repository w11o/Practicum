dict1 = {1: 'яблоки', 2: 'бананы', 3: 'груши'}
dict2 = {'молоко': 1, 'яйца': 2}
dict3 = {'продукты': 'творог', 'все для дома': 'мочалка'}
dict4 = {}

for i in dict1, dict2, dict3:
    for key in i:
        dict4[key] = i[key]

print(dict4)