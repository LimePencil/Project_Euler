# Finished on 2020.07.17

# returns the list of boolean value that index is corresponding whether the number is prime or not

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


list_of_primes = sieve_of_eratosthenes(5)
total = 0
for x in range(len(list_of_primes)):
    if list_of_primes[x]:
        total += x

print(total)
