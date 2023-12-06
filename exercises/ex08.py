# Создайте функцию для определения того, каким является число: положительным, отрицательным или нулем.

def printState(n):
    if n == 0:
        print("Number is zero")
    elif n > 0:
        print("Number is positive")
    elif n < 0:
        print("number is negative")


if __name__ == "__main__":
    num = int(input())
    printState(num)

