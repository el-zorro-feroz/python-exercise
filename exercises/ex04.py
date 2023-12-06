# Даны списки:
# a = [3 ,2, -13, 4, 12, -8, 9];
# b = [0, 5, 16, -22].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков. 
# Отсортируйте список по возрастанию чисел.
# С помощью функции, определите наименьшее число из общих двух списков.

def getSummarySortedArray(a, b):
    result = []

    ### Hand-made extend method
    #
    # def addToResult(e):
    #     for i in e:
    #         result.append(i)

    # addToResult(a)
    # addToResult(b)

    result.extend(a)
    result.extend(b)

    result.sort()

    return result


def getMinElement(a, b):
    minA, minB = min(a), min(b)
    return minA if minA < minB else minB


if __name__ == "__main__":
    a = [3 ,2, -13, 4, 12, -8, 9]
    b = [0, 5, 16, -22]

    c = getSummarySortedArray(a, b)
    d = getMinElement(a, b)

    print('Result array: \t', c, '\nMin element: \t', d)

