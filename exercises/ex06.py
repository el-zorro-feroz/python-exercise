# Возведите число в степень до заданного предела. Показатель степени и предел вводятся с клавиатуры.

def getMaxPow(a, b):
    i = 1

    while True:
        if (i ** a > b):
            return i - 1

        i = i + 1
        

if __name__ == "__main__":
    a, b = int(input("Enter pow: \t")), int(input("Enter pow limit: \t"))
    print(getMaxPow(a, b))

