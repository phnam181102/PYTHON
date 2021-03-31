for i in range(10000, 99999):
    count = 0
    for v in range(1, i + 1):
        if i % v == 0:
            count += 1
    if count == 2:
        print(str(i))
