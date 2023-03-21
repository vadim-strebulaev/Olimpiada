n = int(input())
m = int(input())
a = max(n, m)
b = min(n, m)
if n % 2 == 0:
    print((m - n + 2) * 2)
else:
    print(m - n + 1)