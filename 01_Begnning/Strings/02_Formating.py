username = input('Enter the user name: ')
age = input('Укажите возраст :')

# username = 'Vika'
# Форматирование строк:

# 1. С помощью оператора f
formatted_string_1 = f'Welcome {username}!'

# 2. С помощью метода .format()
common_text = 'Welcome {}!'
formatted_string_2 = common_text.format(username)

# 3. С помощью оператора %
formatted_string_3 = 'Welcome %s!' % username

# 4. Конкатенация
concatenated_string = 'Welcome ' + username + '!'









# if formatted_string_1 == formatted_string_2 == formatted_string_3 == concatenated_string:
#     print('\nВсе строки равны:')
#     print(formatted_string_1)
#     print(formatted_string_2)
#     print(formatted_string_3)
#     print(concatenated_string)
# else:
#     print(False)


# if username == 'Dima':
#     print('Hello, admin!')
# elif username == 'Vika':
#     print('Hello, user!')
# else:
#     print('Go away!')

















# Оператор %
some_values = [5.8654564, 12.993, 99595621.21, 777]

for value in some_values:
    print()
    print('%f' % value)
    print('%.2f' % value)
