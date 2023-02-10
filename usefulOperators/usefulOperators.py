from random import shuffle

"""Range"""
for num in range(0,11,2):
    print(num)

my_list_from_range = list(range(11))

print(my_list_from_range)

"""Enums"""
word = 'hello'

for index,letter in enumerate(word):
    print(f'index: {index} | letter {letter}')

"""Zip"""
list_1 = ['a','b','c','d','e',]
list_2 = [1,2,3,4]
list_3 = [100,200]

for item in zip(list_1,list_2,list_3):
    print(item)

"""Shuffle"""
ordered_list = [1,2,3,4,5,6,7,8,9,10]
shuffle(ordered_list)
print(ordered_list)