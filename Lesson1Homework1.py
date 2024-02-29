# Задание 1: Напишите программу, которая на входе получает 2 числа, производит с ними арифметическую операцию(на ваше усмотрение),
# и выводит “Результат = {результат}”.

# number1 = int(input('Enter one number '))
# number2 = int(input('Enter another number '))
#
# print('Result is ' + str(number1 * number2))

# Задание 2: Напишите программу, чтобы вывести:
# ** ** ** ** *
# *           *
# *           *
# ** ** ** ** *

ast = '*'
print(ast + ast + ast + ast + '\n' + ast + ' ' + ' ' + ast + '\n' + ast + ' ' + ' ' + ast + '\n' + ast + ast + ast + ast)
print('*********\n*       *\n*       *\n*********')

# Задание 3: Напишите программу для нахождения цифр четырёхзначного числа. Число вводится при помощи методa input()
# Input: 3498
# Output:
# Тысячи - 3
# Сотни - 4
# Десятки - 9
# Единицы - 8
#
# bigNum = int(input('Enter a 4 digit number - '))
# thousand = bigNum // 1000
# hundred = (bigNum - thousand*1000) //100
# decimals = (bigNum - thousand*1000 - hundred*100) // 10
# singles = (bigNum - thousand*1000 - hundred*100 - decimals*10) // 1
#
# print(f' Thousands - {thousand} \n Hundreds - {hundred} \n Decimals - {decimals} \n Singles - {singles}')

number = int(input('Please enter 4-digit number: '))
thousand = number//1000
hundred = number%1000//100
ten = number%100//10
one = number%10
print(f'Тысячи - {thousand}\nСотни - {hundred}\nДесятки - {ten}\nЕдиницы — {one}')

# Задание 4: Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы  (a+b)2 и сумму квадратов a2+b2 этих чисел.
# Input:
# 3
# 2
# Output:
# Квадрат суммы 3 и 2 равен 25
# Сумма квадратов 3 и 2 равна 13

num1 = int(input('Enter the first number - '))
num2 = int(input('Enter the second number - '))
squareSum = (num1 + num2)**2
sumSquares = (num1 ** 2) + (num2 ** 2)
print(f'Square sum = {squareSum}')
print(f'Sum of squares = {sumSquares}')



