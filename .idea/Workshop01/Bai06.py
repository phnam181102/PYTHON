n = int(input())

def check(n):
    if (n >= 1):
        ans = ""
        for i in range(2, n):
            count = 0
            for v in range(1, i+1):
                if i % v == 0:
                    count += 1
            if count == 2 and (i+2<n):
                ans = ans + str(i) + ", "
            elif count == 2:
                ans = ans + str(i)
        return ans
    else:
        ans = "n khong hop le!!!"
        return ans

print(check(n))