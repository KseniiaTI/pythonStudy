import my_calc as calc

# Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
from math import sqrt
def square(a):
    return(f'Task 1: Perimeter - {a * 4} Square - {a * a} Diagonal - {round(sqrt(a ** 2 * 2), 2)}')
print(square(2))

# Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# в формате аргумент: значение.
def objects(**kwargs):
    for k, v in kwargs.items():
        print(f'Task 2: {k}: {v}')
objects(name= "John", last_name= "Smith", age= 35, position= "web developer")

#  Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#  положительные числа
my_list = [20, -3, 15, 2, -1, -21]
positive = list(filter(lambda x: x>0, my_list))
print(f'Task 3: {positive}')

# Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
from functools import reduce
muptiply = reduce(lambda x, y: x * y, my_list)
print(f'Task 4: {muptiply}')

# Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Task 5: Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper

# Example usage
@measure_execution_time
def calculate_multiply(numbers):
    tot = 1
    for x in numbers:
        tot *= x
    return tot

# Call the decorated function
result = calculate_multiply([1, 2, 3, 4, 5])
print("Task 5: Result:", result)

# use imported file
print(f'Task 6: {calc.sum(2, 3)}')
print(f'Task 6: {calc.subt(2, 3)}')
print(f'Task 6: {calc.mult(2, 3)}')
print(f'Task 6: {calc.div(2, 0)}')
print(f'Task 6: {calc.sq(2, 3)}')
