"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
n = [1.1, 1.2, 3.1, 5, 10.01]
def average(n):
    max = 0
    min = 1  
    for i in n:
        temp = round(i % 1, 3)  
        if temp > max:
            max = temp
        elif temp < min:
            min = temp
    print(f"max {max} min {min}")
    res = max - min
    return res


print(average(n))


