# Создайте список, состоящий из 6 элементов. Напишите условие проверки уникальности элементов списка. Если есть повторяющиеся – выписать их значения. Если повторов нет – «список уникальный».

def checkArray(a):
    result = []
    uniques = set(a)

    for i in uniques:
        count = 0
        
        for f in a:
            if f == i:
                count = count + 1

        if count > 1:
            result.append(i)

    if len(result) == 0:
        print("List is unique")
    else:
        print(result)
        

if __name__ == "__main__":
    data = []
    for i in range(6):
        print(f'Enter {i + 1} num: \t', end='')
        data.append(int(input()))

    checkArray(data)

