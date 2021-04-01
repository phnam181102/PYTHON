n = int(input())

def fibonacci(n):
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);

ans = "";
for i in range(0, n):
    if i+1 == n:
        ans = ans + str(fibonacci(i))
    else:
        ans = ans + str(fibonacci(i)) + ", ";

print(ans)