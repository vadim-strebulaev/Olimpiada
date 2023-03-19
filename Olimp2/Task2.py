from datetime import datetime
import random
random.seed(10)
geometry = [random.randint(0,5) for _ in range(1_000_000)]
a = len(geometry)

def find_hill(geometry, firstIndex, lastIndex,  base, hills):
    max = 0
    leftBoundary = -1
    rightBoundary = -1
    height = -1
    for i in range(firstIndex, lastIndex):
        localHeight = geometry[i] - base
        if localHeight > 0:
            if height == -1:
                height = localHeight
            elif height > localHeight:
                height = localHeight
            else:
                max = localHeight
            if leftBoundary < 0:
                leftBoundary = i
        elif leftBoundary >= 0:
                rightBoundary = i
                break
    if rightBoundary == -1:
        rightBoundary = lastIndex
    if height > 0:
        hills.append([leftBoundary + 1, rightBoundary, height])
        # print(firstIndex, rightBoundary, lastIndex, height)
        if height < max:
            find_hill(geometry, firstIndex, rightBoundary, base + height, hills)
    return rightBoundary

def impl1():
    hills = []
    rightBoundary = 0
    while True:
        rightBoundary = find_hill(geometry, rightBoundary, a, 0, hills)
        if rightBoundary >= a:
            break
    return hills

start = datetime.now()
hills = impl1()
duration = datetime.now() - start
print(hills)

print(duration)