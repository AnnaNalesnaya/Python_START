"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.

Ввод: значение типа <int>
Вывод: единственное значение типа <bool> (True либо False)

Пример:
6
True

7
True

1
False
"""
num_dey = int(input("введите день недели "))
if  num_dey  == 6 or  num_dey == 7:
     print("выходной")
elif (num_dey >= 1 and num_dey <= 5):
     print ("рабочий")
else: 
    print (False)



