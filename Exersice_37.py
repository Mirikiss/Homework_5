'''
Задача №37. Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''
def rev(s, i = None):
    if i is None:
        i = len(s)
    if i <= 0:
        return
    print(s[i-1], end = '')
    rev(s, i-1)

rev(input('введ текст: '))