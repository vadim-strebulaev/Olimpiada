k, n = map(int, input().split())
commands = [[0, 0]]
now_cords = [0, 0]
all_cords = [[0, 0]]
for _ in range(n):
    commands.append(list(map(str, input().split())))
for i in range(len(commands)):
    for _ in range(int(commands[i][1])):
        if commands[i][0] == "N":
            if commands[i][1] != 0:
                now_cords[0] += 1
            print("N")
        if commands[i][0] == "S":
            if commands[i][1] != 0:
                now_cords[0] -= 1
            print("S")
        if commands[i][0] == "W":
            if commands[i][1] != 0:
                now_cords[1] -= 1
            print("W")
        if commands[i][0] == "E":
            if commands[i][1] != 0:
                now_cords[1] += 1
            print("E")

        for x in range(now_cords[0], now_cords[0] + k):
            for y in range(now_cords[1], now_cords[1] + k):
                # print([x, y])  
                # print(all_cords, [x, y] in all_cords)
                if not ([x, y] in all_cords):
                    all_cords.append([x, y])
print(len(all_cords))