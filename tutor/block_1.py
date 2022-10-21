# Задача «Сумма трёх чисел»
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)


# Задача «Площадь прямоугольного треугольника»
b = int(input())
h = int(input())
print(b*h*1/2)


# Задача «Дележ яблок»
n = int(input())
k = int(input())
print(k // n)
print(k % n)


# Задача «Электронные часы»
t = int(input())
print(t//60%24, t%60)


# Задача «Hello, Harry!»
name = input()
print('Hello, ' + name + '!')


# Задача «Следующее и предыдущее»
num = int(input())
print('The next number for the number ' + str(num) + ' is ' + str(num+1))
print('The previous number for the number ' + str(num) + ' is ' + str(num-1))


# Задача «Парты»
a = int(input())
b = int(input())
c = int(input())
print((a//2) + (a%2) + (b//2) + (b%2) + (c//2) + (c%2))


# Задача «Шнурки»
a = int(input())
b = int(input())
l = int(input())
n = int(input())
print(l*2 + ((a+b)*(n-1))*2 + a)
