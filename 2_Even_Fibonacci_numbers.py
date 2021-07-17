# Finished on 2020.07.17

fibonacci = [1, 2]
first_term = 1
second_term = 2
total = 2
while first_term+second_term<=4000000:
    new_term = first_term + second_term
    fibonacci.append(first_term+second_term)
    first_term = second_term
    second_term = new_term
    if new_term % 2 == 0:
        total += new_term
print(total)