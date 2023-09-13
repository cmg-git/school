# Largest Prime Factor @ slothparadise.com'''

a = int(input('n  = '))

b = 2
while (a > b):
    if (a % b == 0):
        a = a // b;
        b = 2;  # this line can be commented
    else:
        b += 1;

print('Largest factor', b)