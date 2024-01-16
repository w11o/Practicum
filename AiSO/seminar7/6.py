dic4 = {'t': 1, 'd': 7}; a = 0; b = 1

for key in dic4:
    a += dic4.get(key)
    b *= dic4.get(key)

print(a); print(b)