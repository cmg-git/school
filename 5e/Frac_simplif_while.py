# Fraction simplification
# https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm


def gcd(a, b):
    # greatest common divisor GCD
    # Euclidian algorithm
    while b:
        a, b = b, a % b
    return a


x = int(input('Input numerator = '))
y = int(input('Input denominator = '))
print(x, '/', y, ' = ',
      x // gcd(x, y), '/', y // gcd(x, y))
print('Greatest common devisor = ', gcd(x, y))
