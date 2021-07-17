import math


def sieve_of_eratosthenes(num):
    primes = [True] * (num + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, num + 1):
        if primes[i]:
            j = i * 2
            while j < num + 1:
                primes[j] = False
                j += i

    return primes


given = 600851475143
num = math.ceil(math.sqrt(600851475143))
primes = sieve_of_eratosthenes(num)
for i in reversed(range(0, num)):
    if primes[i] and given % i == 0:
        print(i)
        break
