import collections

rect = collections.namedtuple('rect', 'x1 y1 x2 y2')


def getVoids(index, line):
    result = []

    length = len(line)
    if length > 0:
        for i, item in enumerate(line):
            if item == '.':
                if len(result) > 0 and result[-1].x2 + 1 == i:
                    result[-1] = rect(result[-1].x1, index, i, index)
                else:
                    result.append(rect(i, index, i, index))

    return result

def shminput():
    o = [
        "xxxxx",
        "x...x",
        "x...x",
        "x...x",
        "xxxxx"
    ]
    c = [
        "xxxxx",
        "x....",
        "x....",
        "x....",
        "xxxxx"
    ]
    h = [
        "x...x",
        "x...x",
        "xxxxx",
        "x...x",
        "x...x"
    ]
    p = [
        "xxxxx",
        "x...x",
        "xxxxx",
        "x....",
        "x...."
    ]
    l = [
        "x....",
        "x....",
        "x....",
        "x....",
        "xxxxx"
    ]
    i1 = [
        "xxx..",
        "xxx..",
        "xxx..",
        "xxx..",
        "....."
    ]
    i2 = [
        ".....",
        "xxx..",
        "xxx..",
        "xxx..",
        "....."
    ]
    i3 = [
        ".....",
        "xxx..",
        "xxx..",
        "xxx..",
        "xxx.."
    ]
    i4 = [
        ".xxx.",
        ".xxx.",
        ".xxx.",
        ".xxx.",
        "....."
    ]
    i5 = [
        ".....",
        ".xxx.",
        ".xxx.",
        ".xxx.",
        "....."
    ]
    i6 = [
        ".....",
        ".xxx.",
        ".xxx.",
        ".xxx.",
        ".xxx."
    ]
    i7 = [
        "..xxx",
        "..xxx",
        "..xxx",
        "..xxx",
        "....."
    ]
    i8 = [
        ".....",
        "..xxx",
        "..xxx",
        "..xxx",
        "....."
    ]
    i9 = [
        ".....",
        "..xxx",
        "..xxx",
        "..xxx",
        "..xxx"
    ]
    # return [
    #     "../",
    #     "../",
    #     "/.."
    # ]
    
    return [
        o,
        c,
        l,
        p,
        h,
        i1,
        i2,
        i3,
        i4,
        i5,
        i6,
        i7,
        i8,
        i9
    ]

def reduce(lines):
    if len(lines) > 1:
        reducedLine = []
        for void in lines[-1]:
            previousVoid: rect

            appended = False

            for i, previousVoid in enumerate(lines[-2]):
                if void.x1 == previousVoid.x1 and void.x2 == previousVoid.x2 and \
                    previousVoid.y2 + 1 == void.y1:
                    lines[-2][i] = rect(previousVoid.x1, previousVoid.y1, previousVoid.x2, previousVoid.y2 + 1)
                    appended = True
            
            if not appended:
                reducedLine.append(void)

        if len(reducedLine) == 0:
            lines.pop()

def isI(voids, boundary):
    def spansOrAdjoins(voids):
        return \
            len(voids) == 1 \
                and voids[0].x1 == 0 and voids[0].x2 == boundary - 1 \
            or len(voids) == 2 \
                and all(void.x1 == 0 or void.x2 == boundary - 1 for void in voids)
    
    return len(voids) == 0 or \
        len(voids) == 1 and spansOrAdjoins(voids[0]) \
        or len(voids) == 2 and \
            ( \
            len(voids[0]) == 2 \
            and len(voids[1]) == 1 \
            or len(voids[0]) == 1 \
            and len(voids[1]) == 2 \
            ) \
            and all(spansOrAdjoins(void) for void in voids) \
        or len(voids) == 3 and \
            len(voids[0]) == 1 and len(voids[1]) in [1, 2] and len(voids[2]) == 1 \
            and all(spansOrAdjoins(void) for void in voids) \
        or len(voids) == 2 and \
            voids[0][0].x1 == 0 \
            and ( \
            voids[1][0].x2 == boundary - 1 \
            or voids[1][0].x1 == 0
            ) \
        or len(voids) == 2 and \
            voids[1][0].x1 == 0 \
            and voids[1][0].x2 == boundary - 1 \
            and voids[0][0].x2 == boundary - 1 \
        or len(voids) == 2 and \
            voids[0][0].x1 == 0 \
            and voids[0][0].x2 == boundary - 1 \
            and voids[1][0].x1 == 0 \
            and voids[1][0].x2 == boundary - 1 \
        or len(voids) == 3 and \
            voids[0][0].x1 == 0 \
            and voids[0][0].x2 == boundary - 1 \
            and voids[2][0].x1 == 0 \
            and voids[2][0].x2 == boundary - 1 \
            and ( \
            voids[1][0].x1 == 0 \
            or voids[1][0].x2 == boundary - 1 \
            ) \
        or len(voids) == 1 \
        and voids[0][0].y1 == 0 \
        and voids[0][0].y2 == boundary - 1


def isC(voids: list[list[rect]], boundary):
    return len(voids) == 1 and len(voids[0]) == 1 \
        and voids[0][0].x1 > 0 \
        and voids[0][0].y1 > 0 \
        and voids[0][0].x2 == boundary - 1 \
        and voids[0][0].y2 < boundary - 1 \

def isH(voids, boundary):
    return len(voids) == 2 and len(voids[0]) == 1 \
        and voids[0][0].y1 == 0 \
        and voids[1][0].y2 == boundary - 1 \
        and voids[0][0].x1 == voids[1][0].x1 \
        and voids[0][0].x2 == voids[1][0].x2 \
        and voids[0][0].x1 != 0 \
        and voids[0][0].x2 != boundary - 1

def isP(voids, boundary):
    return len(voids) == 2 \
        and len(voids[0]) == 1 \
        and len(voids[1]) == 1 \
        and voids[0][0].x1 != 0 \
        and voids[0][0].y1 != 0 \
        and voids[0][0].x2 != boundary - 1 \
        and voids[1][0].x2 == boundary - 1 \
        and voids[1][0].y2 == boundary - 1
def isO(voids: list[list[rect]], boundary):
    return len(voids) == 1 and len(voids[0]) == 1 \
        and voids[0][0].x1 > 0 \
        and voids[0][0].y1 > 0 \
        and voids[0][0].x2 < boundary - 1 \
        and voids[0][0].y2 < boundary - 1 \

def isL(voids, boundary):
    return len(voids) == 1 \
    and len(voids[0]) == 1 \
    and voids[0][0].x1 != 0 \
    and voids[0][0].x2 == boundary - 1 \
    and voids[0][0].y1 == 0


input = shminput()
a = int(5)

for dataIndex, data in enumerate(input):
    voids = []
    isX = False
    for i in range(a):
        line = list(data[i])
        localVoids = getVoids(i, line)
        if len(localVoids) > 0:
            voids.append(localVoids)
        reduce(voids)

        if len(voids) > 0 and len(voids[-1]) > 2:
            isX = True
            break

    print(dataIndex, end=" ")
    if isX:
        print("X", voids)
    elif isI(voids, a):
        print("I")
    elif isC(voids, a):
        print("C")
    elif isH(voids, a):
        print("H")
    elif isP(voids, a):
        print("P")
    elif isO(voids, a):
        print("O")
    elif isL(voids, a):
        print("L")
    else:
        print("X", voids)


"""
Задача 5. Надпись на табло
Ограничение по времени: 1 секунда
Вы получили доступ к одной из камер наблюдения в особо секретной огранизации. В зоне видимости камеры находится табло, с которого вы постоянно считываете информацию. Теперь вам
нужно написать программу, которая по состоянию табло определяет, какая буква изображена на
нём в данный момент. Табло представляет из себя квадратную таблицу, разбитую на n × n равных
квадратных светодиодов. Каждый диод либо включён, либо выключен. Введём систему координат,
направив ось OX вправо, а ось OY — вверх, приняв сторону диода равной 1.
На табло могут быть изображены только следующие буквы:
• I — прямоугольник из горящих диодов.
• O — прямоугольник из горящих диодов с углами (x1, y1) и (x2, y2), внутри которого есть прямоугольник из выключенных диодов с координатами углов (x3, y3) и (x4, y4). При этом границы
выключенного прямоугольника не должны касаться внешнего, то есть x1 < x3 < x4 < x2 и
y1 < y3 < y4 < y2.
• C — прямоугольник из горящих диодов с углами (x1, y1) и (x2, y2), внутри которого есть прямоугольник из выключенных диодов с координатами углов (x3, y3) и (x4, y4). При этом правая
граница выключенного прямоугольника находится на правой границе внешнего прямоугольника, то есть x1 < x3 < x4 = x2 и y1 < y3 < y4 < y2.
• L — прямоугольник из горящих диодов с углами (x1, y1) и (x2, y2), внутри которого есть прямоугольник из выключенных диодов с координатами углов (x3, y3) и (x4, y4). При этом правые
верхние углы выключенного прямоугольника и внешнего прямоугольника совпадают, то есть
x1 < x3 < x4 = x2 и y1 < y3 < y4 = y2.
• H — прямоугольник из горящих диодов с углами (x1, y1) и (x2, y2), внутри которого находятся
2 прямоугольника из выключенных диодов с координатами углов (x3, y3), (x4, y4) у первого и
(x5, y5), (x6, y6) у второго. При этом выключенные прямоугольники должны иметь одинаковую
ширину, находиться строго один под другим, один прямоугольник должен касаться верхней
стороны, а другой прямоугольник должен касаться нижней стороны внешнего прямоугольника, то есть x1 < x3 = x5 < x4 = x6 < x2 и y1 = y3 < y4 < y5 < y6 = y2.

• P — прямоугольник из горящих диодов с углами (x1, y1) и (x2, y2), внутри которого находятся
2 прямоугольника из выключенных диодов с координатами углов (x3, y3), (x4, y4) у первого
и (x5, y5), (x6, y6) у второго. При этом правый нижний угол первого выключенного прямоугольника должен совпадать с правым нижним углом внешнего прямоугольника, а другой
выключенный прямоугольник должен находиться строго выше и не касаться границ других
прямоугольников, также левые границы двух выключенных прямоугольников должны совпадать, то есть x1 < x3 = x5 < x6 < x4 = x2 и y1 = y3 < y4 < y5 < y6 < y2.
• Любое другое состояние табло считается буквой X.
По виду табло определите, какая буква на нём изображена.
Формат входных данных
В первой строке входных данных находится одно число n (1 6 n 6 10) — сторона табло.
В следующих n строках находятся строки длины n из символов «.» и «#» — строки таблицы.
«.» обозначает выключенный квадратный диод табло, а «#» — горящий.
Формат выходных данных
Программа должна вывести единственный символ: если данная таблица подходит под одно из
описаний букв I, O, C, L, H, P, то выведите её (все буквы — английские). Если же данная таблица
не подходит ни под какие условия, то выведите X.


"""