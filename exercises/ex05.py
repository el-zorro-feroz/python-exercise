# Найти площадь и периметр прямоугольного треугольника. Длины катетов вводятся с клавиатуры. (C использованием модуля math).

import math


def getS(a, b):
    return a * b / 2


def getP(a, b):
    c = math.sqrt(a * a + b * b)
    return a + b + c    


if __name__ == "__main__":
    a, b = int(input("Enter a side: \t")), int(input('Enter b side: \t'))

    s = getS(a, b)
    p = getP(a, b)
    
    print('S = \t{:.2f}'.format(s))
    print('P = \t{:.2f}'.format(p))

