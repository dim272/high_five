# Срезы строк

numbers = '123456789'
# indexes  012345678

x = numbers[0] # 1
y = numbers[0:9:2]  # 1 по 9 с шагом 2 '13579'
y1 = numbers[2:6]   # "3456"
y2 = numbers[:3]   # "123"

# numbers.index('1') == 0
# numbers.index('3') == 2
# numbers.index('9') == 8

# numbers[0] == '1'
# numbers[2] == '3'
# numbers[8] == '9'


for num in numbers:
    if num != '5':
        print(f'num = {num} ~~ index = {numbers.index(num)}')


# строка[индекс] - получение символа по его индексу
# строка[с какого индекса : по какой индекс(не включая его) : шаг] - получение среза строки


# numbers[5]       == '6'
# numbers[0:9:2]   == '13579'
# numbers[5:6]     == '6'
# numbers[::2]     == '13579'
# numbers[5:]      == '6789'
# numbers[:5]      == '12345'
# numbers[::-1]    == '987654321'
# numbers[:3:-1]   == '98765'


# print('numbers[5] =',       numbers[5])         # '6'
# print('numbers[0:9:2]) =',  numbers[0:9:2])     # '13579'
# print('numbers[5:6]) =',    numbers[5:6])       # '6'
# print('numbers[::2]) =',    numbers[::2])       # '13579'
# print('numbers[5:]) =',     numbers[5:])        # '6789'
# print('numbers[:5]) =',     numbers[:5])        # '12345'
# print('numbers[::-1] =',    numbers[::-1])      # '987654321'
# print('numbers[:3:-1] =',   numbers[:3:-1])     # '98765'


