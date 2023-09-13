# Check if a number is prime
num = int(input('Input an integer number = '))

numIsPrime = True
for i in range(2, num):
    if (num % i) == 0:
        print(num, '=', i, '*', num // i)
        numIsPrime = False
if numIsPrime:
    print(num, ' is prime')
else:
    print(num, ' is not prime')
