from operator import sub
k = int(input())
mas = []
for i in range(k):
    a = int(input())
    mas.append(list(map(int, input().split())))
data = []
for test in range(len(mas)):
    data = []
    field = mas[test]
    a = len(field)
    while field != [0] * a:
        min1 = max(field)
        first = a - 1
        second = 0
        for i in range(a):
            if field[i] <= min1 and field[i] != 0:
                min1 = field[i]
        for i in range(a):
            if field[i] >= min1 and first == a - 1 and field[i] != 0:
                first = i 
            if field[i] == 0 and first < i:
                break
            else:
                second = i
        data.append([first + 1, second + 1, min1])
        field = list(map(sub, field, [min1 if i >= first and i <= second else 0 for i in range(a)]))
    print(len(data))
    for i in range(len(data)):
        print(*data[i])