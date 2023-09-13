# Python Finding Prime Factors
# StackOverflow.com

# the largest prime factor
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def lpf(a):
    ''' Largest Prime Factor @ slothparadise.com'''
    b = 2
    while (a > b):
        if (a % b == 0):
            a = a / b;
            b = 2;
        else:
            b += 1;
    return b

def prime_factors(n):
    '''Find the prime factors of an integer'''
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


n = int(input('n = '))
nlpf = lpf(n)
print('Larget prime factor of ', n, ' : ', nlpf)
nlpf = largest_prime_factor(n)
print('Larget prime factor of ', n, ' : ', nlpf)

print('Prime factors of ', n, ' : ', prime_factors(n))
