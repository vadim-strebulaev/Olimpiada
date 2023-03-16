n = int(input())
time = 0
while True:
    if time * 3 + time * 2 >= n:
        print(time)
        break
    time += 1