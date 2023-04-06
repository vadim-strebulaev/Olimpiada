n = int(input())
a = []
b = [1, 1]
for i in range(n):
    a.append(int(input()))
while b[-1] * b[-2] < max(a):
    b.append(b[-1] + b[-2])
print(a, "\n", b, sep="")
count = 0
k = 0
for i in range(len(a)):
    count = 0
    k = 1
    while a[i] != k:
        if a[i] % b[count] == 0 and b[k] * b[count] < a[i]:
            k *= b[k]
        else:
            k += 1
    print(k)