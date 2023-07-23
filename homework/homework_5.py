# def rev(s, i = None):
#     if i is None:
#         i = len(s)
#     if i <= 0:
#         return
#     print(s[i-1], end = '')
#     rev(s, i-1)

# rev(input('введ текст: '))


# def f(a = None, b = None):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a * f(a, b - 1)

# print(f(a = 3, b = 5))

# def sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return sum(a - 1, b + 1)


# print(sum(a = 2, b = 2))


def sum(a, b):
    return b

print(sum(2, 2))