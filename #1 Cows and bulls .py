from random import randint
r_digit = random.randint(1, 9999)
r_digit = str(r_digit)
if len(r_digit) < 4:
    while len(r_digit) != 4:
        r_digit = '0' + r_digit