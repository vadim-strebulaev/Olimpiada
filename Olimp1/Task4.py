n = int(input())
m = int(input())
sum = n
for i in range(1, n + n % 2, 2):
    sum += n - i + m - i
print(sum)
# не конечный вариант