n = int(input())
m = int(input())
sum = 0
a = []
sum1 = 0
for i in range(n, 0, -1):
    sum1 += i
    if sum + i > m:
        continue
    sum += i
    a.append(i)
if sum1 < m:
    print(0)
else:
    print(*a, sep="\n")