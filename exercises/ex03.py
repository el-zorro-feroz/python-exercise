# Найдите символ “k” в строке “Hello World”. Если символ найден – вывод “TRUE”. (Подсказки: в решении могут использоваться for/else/in/true/false

def findK(s):
    if (s.count('k') > 0):
        print('TRUE')
    else:
        print('FALSE')


if __name__ == "__main__":
    data = 'Hello World'
    findK(data)

