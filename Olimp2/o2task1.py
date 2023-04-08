length, count = map(int, input().split())
heigth = 4
lengths = [length] * heigth
field = []
way = [[0, 0]]
for i in range(length):
    field.append([length] * 4)
field[0][0] = 0

for meteor in range(count):
    i, j = map(int, input().split())
    field[i - 1][j - 1] = "M"
nowCords = [0, 0]
def go (data, nowCords):
    if nowCords[0] != length - 1 and data[nowCords[0] + 1][nowCords[1]] != "M" and not [nowCords[0] + 1, nowCords[1]] in way:
        nowCords[0] += 1
        way.append(nowCords.copy())
    elif data[nowCords[0]][nowCords[1] - 1] != "M" and not [nowCords[0], nowCords[1] - 1] in way and nowCords[0] != 0:
        nowCords[1] -= 1
        way.append(nowCords.copy())
    elif data[nowCords[0] - 1][nowCords[1]] != "M" and not [nowCords[0] - 1, nowCords[1]] in way and nowCords[0] != 0:
        nowCords[0] -= 1
        way.append(nowCords.copy())
    elif nowCords[0] != heigth - 1 and data[nowCords[0]][nowCords[1] + 1] != "M" and not [nowCords[0], nowCords[1] + 1] in way:
        nowCords[1] += 1
        way.append(nowCords.copy())
    else:
        if nowCords[0] != length - 1 and data[nowCords[0] + 1][nowCords[1]] != "M":
            nowCords[0] += 1
            way.append(nowCords.copy())
        elif data[nowCords[0]][nowCords[1] - 1] != "M" and nowCords[0] != 0:
            nowCords[1] -= 1
            way.append(nowCords.copy())
        elif data[nowCords[0] - 1][nowCords[1]] != "M" and nowCords[0] != 0:
            nowCords[0] -= 1
            way.append(nowCords.copy())
        elif nowCords[0] != heigth - 1 and data[nowCords[0]][nowCords[1] + 1] != "M":
            nowCords[1] += 1
            way.append(nowCords.copy())
    if(nowCords[0] == length - 1):
        pass
    else:
        go(data, nowCords)
go(field, nowCords)
for i in range(len(way)):
    for j in range(i + 1, len(way)):
        if way[i] == way[j]:
            del way[i:j]
            break
word_way = []
for i in range(len(way) - 1):
    if way[i][0] == way[i + 1][0] + 1:
        word_way.append("L")
    if way[i][0] == way[i + 1][0] - 1:
        word_way.append("R")
    if way[i][1] == way[i + 1][1] + 1:
        word_way.append("U")
    if way[i][1] == way[i + 1][1] - 1:
        word_way.append("D")
countR = 0
way = []
for i in word_way:
    if(i != "R"):
        if countR != 0:
            way.append(["R", countR])
            countR = 0
        way.append([i])
    else:
        countR += 1
way.append(["R"])
if countR != 0:
    way[-1].append(countR)
for i in range(len(way)):
    for j in range(len(way[i])):
        print(way[i][j], end=" ")
    print("")


"""
Задача A. Метеориты
Игровое поле в игре «Метеориты» представляет собой полоску длиной N клеток и высотой
в 4 клетки. В некоторых клетках поля расположены метеориты, при столкновении с которыми
космический корабль, управляемый игроком, разбивается.
Для управления кораблём используется три команды: ”U” — перемещает корабль на одну клетку
вверх, ”D” — перемещает корабль на одну клетку вниз и ”R X” — перемещает корабль на X клеток
вправо (независимо от числа X это считается одной командой).
Клетки игрового поля занумерованы с верхнего левого угла, верхняя левая клетка имеет X
координату 1 и Y координату 1. В начале игры корабль также находится в верхней левой клетке
поля.
Среди игроков считается наиболее престижным достичь столбца с номером N используя наименьшее количество команд.
Вам удалось узнать карты, на которых будет проводится чемпионат по игре в «Метеориты»
и вы хотите пройти все карты, используя как можно меньше команд для управления кораблем.
Гарантируется, что на всех картах можно добраться до столбца N, используя только разрешённые
команды.
В первой строке входного файла задается число N — количество карт. Каждое описание карты состоит из чисел N и K — длины полоски и количества метеоритов на ней. В следующих K
строках задаются координаты метеоритов в виде двух чисел X и Y . Метеориты перечисляются в
произвольном порядке. Карты разделяются одной пустой строкой.
В качестве ответа необходимо вывести N описаний последовательности команд. Каждое описание последовательности команд должно состоять из числа C — количества команд и C команд по
одной в строке.
"""