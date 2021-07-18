# Finished on 2020.07.18

for m in range(1,33):
    for n in range(1, 33):
        if m > n:
            a = 2 * m * n
            b = m ** 2 - n ** 2
            c = m ** 2 + n ** 2
            if a + b + c == 1000:
                print(a*b*c)
                quit()
