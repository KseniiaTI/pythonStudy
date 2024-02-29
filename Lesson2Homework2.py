# Задание 1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

def hp(x):
    if x <=0:
        return 'False'
    else:
        return 'True'

print(f'Task 1 - {hp(0.0000001)}')

# Задание 2
# Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

def even(x):
    if x % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(f'Task 2 - {even(3)}')

# Задание 3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)

def year(x):
    if x % 100 == 0 and x % 400 != 0:
        return 'Not a leap year'
    elif x % 4 == 0 or x % 400 == 0:
        return 'Leap year'
    else:
        return 'Not a leap year'

print(f'Task 3 - {year(2004)}')

# Задание 4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью input()

# text = input('Enter a word ')
# number = int(input('Enter a random number '))
# while number > 0:
#     number = number - 1
#     print(f'Task 4 - {number} - {text}')
#
# # with for loop
# text = input('Enter a word ')
# number = int(input('Enter a random number '))
# for i in range(number):
#     print(f'Task 4 - {text}')

# Задание 5
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное арифметическое действие
# и печатает результат в формате: {num1} {operator) {num2} = {result}

num1 = int(input('Enter a number '))
num2 = int(input('Enter another number '))
op = input('Enter an operator such as +, -, /, *, %, ** ')
result = 0

if num2 == 0 and op == '/':
    print('Error')
elif op == '+':
    result = num1 + num2
    print(f'{num1} {op} {num2} = {result}')
elif op == '-':
    result = num1 - num2
    print(f'{num1} {op} {num2} = {result}')
elif op == '/':
    result = num1 / num2
    print(f'{num1} {op} {num2} = {result}')
elif op == '*':
    result = num1 * num2
    print(f'{num1} {op} {num2} = {result}')
elif op == '%':
    result = num1 % num2
    print(f'{num1} {op} {num2} = {result}')
elif op == '**':
    result = num1 ** num2
    print(f'{num1} {op} {num2} = {result}')

