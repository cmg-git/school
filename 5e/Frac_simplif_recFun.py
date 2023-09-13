# Fraction simplification
# https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
# https://proofwiki.org/wiki/Euclidean_Algorithm


def gcd(a, b):
    # greatest common divisor GCD
    # Euclidean algorithm, GCD, Khan Academy
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


x = int(input('Input numerator = '))
y = int(input('Input denominator = '))
print(x, '/', y, ' = ',
      x // gcd(x, y), '/', y // gcd(x, y))
print('Greatest common devisor = ', gcd(x, y))
