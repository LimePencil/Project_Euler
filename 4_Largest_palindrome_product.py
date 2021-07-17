largest = 0
for i in reversed(range(100,1000)):
    for j in reversed(range(100,1000)):
        num = i*j
        if num < largest:
            break
        if str(num) == str(num)[::-1]:
            largest = max(largest, num)

print(largest)