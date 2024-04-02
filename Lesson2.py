x = 5
print (x == 5)
print (x > 3 and x < 8)

num = 5
print(type(x))
if num == 5:
    print('Five!')
elif num < 5:
    print('Less than five')
else:
    print('More than five')

message1 = 'hello'
message2 = 'hellohello'
#to check string length
if len(message2) > len(message1):
    print(message2)
else:
    print(message1)

# ASCII code comparison
sym1 = 'O'
sym2 = 'P'
print(sym1 < sym2)

i = 0
while i < 5:
    i = i + 1
    # to skip an iteration
    if i == 3:
        continue
    print(i)
# to stop the loop use BREAK

i = 5
while i > 0:
    print(i, 'Hello')
    i = i - 1
print('Go!')

# when using for loop, no conditions are needed
# for iterating N times RANGE function can be used

for i in range(10):
    print(i)

# start, stop, step
for i in range(1, 11, 1):
    print(i)

word = 'hello'
for symbol in word:
    print(f'{word.index(symbol)} - {symbol}')

# to get distinct indices for all letters in the word (even repeating)
word = 'hello'
for index, symbol in enumerate(word):
    print(f'{index} - {symbol}')

# to get boolean value
# False: none, 0, 0.0, '', [], {}, SET()
print(bool(None))

arr = ''
if arr:
    print('Not empty')
else:
    print('Empty')

# functions - DEF
def sum(x, y):
    return x + y
print(sum(5, 8))