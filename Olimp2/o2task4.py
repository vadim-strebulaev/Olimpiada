def inputTrains():
    n = int(input())
    trains = []
    for i in range(n):
        trains.append(str(input()))
    return (trains)
# def findMinMax(data):
#     min = 0
#     max = 0
#     for i in range(len(data)):
#         # print(len(set(data[i])), set(data[i]))
#         if len(set(data[i])) > len(data[max]):
#             max = i
#         if len(set(data[i])) == 0:
#             min = i
#         elif len(set(data[i])) < len(data[min]):
#             min = i
#     return (min, max)
trains = inputTrains()
def acceptAll(trains):
    for i in trains:
        if len(set(i)) > 1:
            return 0
    return 1
print(trains, min, max) 
# 1
# while acceptAll(trains) != 1:
#     MinMax = findMinMax(trains)
#     min = MinMax[0]
#     max = MinMax[1]
#     if len(trains[min]) != 0:
#         if trains[max][0] == trains[min][0]:
#             count = 0
#             for i in range(len(trains[max])):
#                 if trains[max][i] == trains[min][0]:
#                     count += 1
#                 else:
#                     break
#             trains[min] = trains[max][0:count] + trains[min]
#             trains[max] = trains[max][count:]
#         else:
#             count = 0
#             for i in range(len(trains[max])):
#                 reversedMax = trains[max][::-1]
#                 if reversedMax[i] == trains[min][-1]:
#                     count += 1
#                 else:
#                     break
#             trains[min] = trains[min] + trains[max][len(trains[max]) - count:]
#             trains[max] = trains[max][:count - 1]
#     else:
#         count = 0
#         for i in range(len(trains[max])):
#             if trains[max][i] == trains[max][0]:
#                 count += 1
#             else:
#                 break
#         trains[min] = trains[max][:count]
#         trains[max] = trains[max][count:]
#     print(trains, min, max) 



# 2 
# def StartToCount(firstStr, secondStr):
#     for i in range(len(firstStr)):
#         if firstStr[i] != firstStr[0]:
#             break
#     secondStr = firstStr[0:i] + secondStr
#     firstStr = firstStr[i:]
#     # print(firstStr, secondStr, "first, second strs")
#     # print(i, len(secondStr))
#     return firstStr, secondStr
# def CountToEnd(firstStr, secondStr):
#     firstStr = firstStr[::-1]
#     secondStr = secondStr[::-1]
#     Strs = StartToCount(firstStr, secondStr)
#     firstStr, secondStr = Strs[0], Strs[1]
#     return firstStr[::-1], secondStr[::-1]


# while acceptAll(trains) != 1:
#     MinMax = findMinMax(trains)
#     min = MinMax[0]
#     max = MinMax[1]
#     if len(trains[min]) != 0:
#         if trains[min][0] == trains[max][0]:
#             Strings = StartToCount(trains[max], trains[min])
#         elif trains[min][-1] == trains[max][-1]:
#             Strings = CountToEnd(trains[max], trains[min])
#             # print(trains[max], trains[min], Strings, "\n", "min max strings")
#         else:
#             pass
#         trains[min] = Strings[1]
#         trains[max] = Strings[0]
#     else:
#         # print("ну ты лох конечно, если ты сюда попал, то у тебя ошибка сверху")
#         for i in range(len(trains[max])):
#             if trains[max][i] != trains[max][0]:
#                 break
#         trains[min] = trains[max][:i]
#         trains[max] = trains[max][i:]
#     print(trains, MinMax)

# 4 
def findMinMaxNotNull(trains):
    max = 0
    min = 0
    for i in range(len(trains)):
        if len(set(trains[i])) >= len(set(trains[max])):
            max = i
        elif len(set(trains[i])) < len(set(trains[min])) and len(trains[i]) > 0:
            min = i
    return(min, max)
def StartToCount(MaxStr, MinStr):
    for i in range(len(MaxStr)):
        if MaxStr[i] != MinStr[0]:
            break
    MinStr = MaxStr[0:i] + MinStr
    MaxStr = MaxStr[i:]
    return(MaxStr, MinStr)
def CountToEnd(MaxStr, MinStr):
    MaxStr = MaxStr[::-1] 
    MinStr = MinStr[::-1] 
    Strings = StartToCount(MaxStr, MinStr)
    MaxStr = Strings[0]
    MinStr = Strings[1]
    return(MaxStr[::-1], MinStr[::-1])
Strings = []
while acceptAll(trains) != 1:
    MinMax = findMinMaxNotNull(trains)
    min = MinMax[0]
    max = MinMax[1]
    if len(trains[min]) != 0:
        if trains[max][0] == trains[min][0]:
            Strings = StartToCount(trains[max], trains[min])
        else:
            Strings = CountToEnd(trains[max], trains[min])
        trains[max] = Strings[0]
        trains[min] = Strings[1]
    print(trains, min, max)

for i in range(len(trains)):
    for j in range(i + 1, len(trains)):
        if trains[i][0] == trains[j][0]:
            trains[i] = trains[i] + trains[j]
            trains[j] = " "
print(trains)
