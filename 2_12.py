'''ЛР 3, 2 уровень
12. Первый отрицательный элемент массива заменить суммой эле-
ментов, расположенных после максимального.'''
def arr(b):

    b2 = b.copy()
    cur = 0
    maxb = max(b)

    for i in range(len(b)):
        if b[i] < 0:
            cur = i
            break
    for i in range(len(b)):
        if b[i] == maxb:
            b2[cur] = sum(b[i + 1:])
    return b2


if arr([-1, 5, 4, 3, 2, 1]) == [10, 5, 4, 3, 2, 1]:
    print('Тест пройден')

#теперь пользователь может ввести свой массив для теста

b = [int(x) for x in input('Введите числа из массива через пробел: ').split()]
print(arr(b))