import math


def isPrime(n):
    if n == 2:
        return True
    # one and even nums > 2 are not prime
    elif n == 1 or (n & 1) == 0: # Binary multiplication(like 0001 & 1010)
        return False
    for i in range(3, math.ceil((math.sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())
    s = 'Prime' if isPrime(num) else 'Not Prime'
    print(s)
