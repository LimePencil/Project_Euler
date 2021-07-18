# Finished on 2020.07.18
num = 2
found = False
while not (found):
    for i in range(3, 21):
        if i == 20 and num%i ==0:
            print(num)
            found = True
            break
        elif num % i == 0:
            continue
        else:
            break
    num += 2
