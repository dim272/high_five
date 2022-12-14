# Задача «Минимум из двух чисел»
a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)

# Задача «Знак числа»
a = int(input())
if a > 0:
    print(1)
elif a < 0:
    print(-1)
else:
    print(0)

# Задача «Шахматная доска»
row1 = int(input())
col1 = int(input())
row2 = int(input())
col2 = int(input())

if (row1 % 2 == 0 and col1 % 2 == 0) or (row1 % 2 != 0 and col1 % 2 != 0):
    if (row2 % 2 == 0 and col2 % 2 == 0) or (row2 % 2 != 0 and col2 % 2 != 0):
        print('YES')
    else:
        print('NO')
else:
    if (row2 % 2 != 0 and col2 % 2 == 0) or (row2 % 2 == 0 and col2 % 2 != 0):
        print('YES')
    else:
        print('NO')

"""Объяснение:
Если первая пара чисел (row1, col1) оба чётные или оба нечётные,
то и вторая пара чисел должны быть оба чётные или оба нечётные.
Если первая пара чисел (row1, col1) одно чётное, а другое нечётное,
то и у второй пары чисел должно быть так же.

Проверить чётное число или нет можно определив его остаток после деления на 2.
Если остатка после деления нет (number % 2 == 0), то число чётное,
если остаток от деления есть (number % 2 != 0), то число нечётное.
"""

# Задача «Високосный год»
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')


# Задача «Минимум из трех чисел»
a = int(input())
b = int(input())
c = int(input())

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)


# Задача «Сколько совпадает чисел»
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)


# Задача «Ход ладьи»
row1 = int(input())
col1 = int(input())
row2 = int(input())
col2 = int(input())

if row1 == row2 or col1 == col2:
    print('YES')
else:
    print('NO')


# Задача «Ход короля»
row1 = int(input())
col1 = int(input())
row2 = int(input())
col2 = int(input())

if -1 <= row1 - row2 <= 1 and -1 <= col1 - col2 <= 1:
    print('YES')
else:
    print('NO')


# Задача «Ход слона»
row1 = int(input())
col1 = int(input())
row2 = int(input())
col2 = int(input())

if row1 - row2 == col1 - col2 or row1 - row2 == -(col1 - col2):
    print('YES')
else:
    print('NO')


# Задача «Ход ферзя»
row1 = int(input())
col1 = int(input())
row2 = int(input())
col2 = int(input())

if row1 - row2 == col1 - col2 or row1 - row2 == -(col1 - col2):
    print('YES')
elif -1 <= row1 - row2 <= 1 and -1 <= col1 - col2 <= 1:
    print('YES')
elif row1 == row2 or col1 == col2:
    print('YES')
else:
    print('NO')


# Задача «Ход коня»
row1 = int(input())
col1 = int(input())
row2 = int(input())
col2 = int(input())

if (row1 - row2 == 1 or row1 - row2 == -1) and (col1 - col2 == 2 or col1 - col2 == -2):
    print('YES')
elif (row1 - row2 == 2 or row1 - row2 == -2) and (col1 - col2 == 1 or col1 - col2 == -1):
    print('YES')
else:
    print('NO')


# Задача «Шоколадка»
n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 or k % m == 0) and n*m > k:
    print('YES')
else:
    print('NO')


# Задача «Яша плавает в бассейне»
N = int(input())
M = int(input())
x = int(input())
y = int(input())

if N > M:
    N, M = M, N

if x == 0 or y == 0:
    print(0)

elif N/x > 2 and M/y > 2:
    if x > y:
        print(y)
    else:
        print(x)
elif N/x < 2 and M/y < 2:
    if N-x > M-y:
        print(M-y)
    else:
        print(N-x)
elif N/x < 2:
    if N-x > y:
        print(y)
    else:
        print(N-x)
else:
    if x > M-y:
        print(M-y)
    else:
        print(x)