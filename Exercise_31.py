# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0

def fibon(n):
    if n <= 1:
        return 1
    return fibon(n - 1) + fibon(n - 2)

#print(fibon(int(input('dasdasdasd'))))

for i in range(int(input('введите число: '))+1):
    print(fibon(i))
