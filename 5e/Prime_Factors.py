# Prime Factors @ slothparadise.com'''

a = int(input('n  = '))

b = 2
factors = []
while (a >= b):
    if (a % b == 0):
        a = a // b;
        factors.append(b)
        b = 2;  # this line can be commented
    else:
        b += 1;

print('Factors ', factors)
