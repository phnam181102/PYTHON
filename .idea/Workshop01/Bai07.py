n = int(input())

def check(n):
    ans = "2"
    count = 0
    i = 3
    while (count+1 < n):
        checkSNT = 0;
        for x in range(1, i + 1):
            if i % x == 0:
                checkSNT += 1
        if checkSNT == 2:
            ans += ", " + str(i)
            count += 1
        i += 1
    return ans

print(check(n))
