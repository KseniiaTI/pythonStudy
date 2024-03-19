# Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
print(f'Task #1 {my_list[0:3]}')
print(f'Task #1 {my_list[2]}')

# Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
list_2 = []
list_3 = []
for x in list_1:
    if isinstance(x, str):
        list_2.append(x)
    else:
        list_3.append(x)
# print (list_2, list_3)
sum = 0
aWords = []

for y in list_3:
    sum += y
print(f'Task #2.1 {sum}')
for i in list_2:
    if "a" in i:
        aWords.append(i)
print(f'Task #2.2 {aWords}')

# Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
list_4 =  ['cat', 'dog', 'horse', 'cow']
print(f'Task #3 {tuple(list_4)}')

# Напишите программу, которая определяет, какая семья больше.
# 1) Программа имеет два input() - например, family_1, family_2.
# 2) Членов семьи нужно перечислить через запятую. Ожидаемый результат - программа выводит
# семью с бОльшим составом.Если состав одинаковый, print("Equal')

# fam_1 = input('How many family members are there in family #1?')
# fam_2 = input('How many family members are there in family #2?')
# allMembers = []
# i = 1
# x = max(int(fam_2), int(fam_1))
# if (int(fam_1) == int(fam_2)):
#     print('Equal')
# else:
#     while i <= x:
#         allMembers.append((i))
#         i = i + 1
#     print(f'Task #4 {allMembers}')

#  printing dictionaries
my_dict = {
    "title": "Один за всех",
    "director": "Сам",
    "year": 2007,
    "budget": 100,
    "main_actor": "Hugo",
    "slogan": "И все за одного"
}
print(f'Task #5 {my_dict.keys()}')
print(f'Task #5 {my_dict.values()}')
print(f'Task #5 {my_dict.items()}')

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
sum_dict = 0
for key in my_dictionary:
    sum_dict += my_dictionary[key]
print(f'Task #6 {sum_dict}')

my_list = [1, 2, 3, 4, 5, 3, 2, 1]
newSet = set(my_list)
print(f'Task #7 {list(newSet)}')

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(f'Task #8 {set1.issubset(set2)}')
print(f'Task #8 {set2.issubset(set1)}')
print(f'Task #8 {set1.intersection(set2)}')
print(f'Task #8 {set1.difference(set2)}')