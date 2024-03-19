# ## lists
# my_list = [1, 2, 3]
# print(type(my_list))
#
# sentence = 'What a wonderful life'
# my_list2 = sentence.split(' ')
# print(my_list2)
#
# my_list3 = list(sentence)
# print(my_list3)

numbers = [1, 2, 3, 4, 5, 6]

# for num in numbers:
#     print(num**2)
#
# # indices in lists
#                     probe
# index               01234
# negative index     -54321
#
# print(numbers[0])
# print(numbers[-1])
#
# Methods:
# .append() - add an element at the end of the list
# .insert() - add an element to a certain place of the list
# .index() - get index of an element in the list (first element if there are repetitions)
# .clear() - clear the list
# .remove() - remove an element from the list
# .reverse() - reverse the list
# .sort() - sorts the list (min to max) by modifying the original list
# sorted(list) - not a method (built-in function), sorts a list by creating a new one and not modifying the original
# .count() - count the number of repeated elements in the list
# .extend() - adds all the items of the specified iterable, such as list, tuple, dictionary, or string , to the end of a list
# sum() - sum the elements in the list
# min() - get the smallest element
# max() - get the largest element
#
# numbers[0] = 10
# print(numbers)
#
# numbers2 = [15, 20, 35]
# numbers.append(numbers2)
# print(numbers)
#
# numbers.extend(numbers2)
# print(numbers)
#
# print(sorted(numbers2))
#
# # to print the first 4 elements
# print(numbers[0: 4])
#
# List comprehension
# num2 = []
# for i in numbers:
#     if i % 2 == 1:
#         num2.append(i*i)
# print(num2)
#
# num3 = [x * x for x in numbers if x % 2 == 1]
# print(num3)

# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

my_tuple = (1, 'apple', None, 2.5)
print(my_tuple)
print(type(my_tuple ))

my_tuple2 = 1, 2, 3, 4
print(my_tuple2)

# print(tuple(numbers))

# Methods:
# .index() - get index of an element in the tuple (first element if there are repetitions)
# .count() - count the number of repeated elements in the tuple
# sum() - sum the elements in the tuple
# min() - get the smallest element
# max() - get the largest element
# len() - shows number of elemens in tuple

num10 = 10
my_tuple.count()

# to show
