# Имеется список a = [0, 5, 12, 45, 33, 100, 144]. Выведите все значения, которые меньше 42.

def printResult(list):
    for e in list:
        if e < 42:
            print(e)


if __name__ == "__main__":
    a = [0, 5, 12, 45, 33, 100, 144]
    printResult(a)

