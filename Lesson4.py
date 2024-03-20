# functions
def sum_it(a, b, c=5):
    return a + b + c
print(sum_it(5, 4))

def hello(name, lname, age):
    return f'Hello, my name is {name} {lname}. I am {age}.'

print(hello('Julia', 'Bird', 70))
print(hello(lname ='Bird', age = 70, name = 'Julia'))

def pattern(length, char1='/', char2='*'):
    return (char1 + char2) * length + char1

print(pattern(9))

min_value = min(5, 8, 25, 1, 0)
print(min_value)

l = [1, 5, 8, 12, 15]

from functools import reduce
res1 = reduce(lambda x, y: x + y, l)
print(res1)

evens = list(filter(lambda x: x%2 == 0, l))
print(evens)

my_list = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
new_list = list(filter( lambda item: isinstance(item, str) and 'a' in item, my_list))
print(new_list)

# decorator function
def decorator_function(func):
    def wrapper(*arg):
        print('Wrapper function')
        print(f'Wrapped function {func.__name__}')
        print(f'Executing wrapper function')
        print(func(*arg))
        print('Exiting wrapper function')
    return wrapper()

@decorator_function
def my_wrapper(item):
    return f'{item} is wrapped'

my_wrapper('Candy')