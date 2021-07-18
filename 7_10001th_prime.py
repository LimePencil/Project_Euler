# Finished on 2020.07.18

number_of_primes = 0
num = 1000000
primes = [True] * (num + 1)
primes[0] = False
primes[1] = False
for i in range(2, num + 1):
    if primes[i]:
        number_of_primes += 1
        if number_of_primes == 10001:
            print(str(i))
        j = i * 2
        while j < num + 1:
            primes[j] = False
            j += i
