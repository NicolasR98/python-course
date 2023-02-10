"""For loops"""

my_iterable = [1,2,3,4,5,6,7,8,9,10]

for num in my_iterable:
    if num % 2 == 0:
        print(f'Is even! {num}')
    else:
        print(f'Is odd! {num}')

my_tuple_list = [(1,2), (3,4), (5,6)]

for a,b in my_tuple_list:
    print(f'This is {a} and this is {b}')

my_dict = {'k1': 1, 'k2': 2, 'k3': 3}

for key,value in my_dict.items():
    print(f'{key}: {value}')

for num in my_iterable:
    pass # This basically pass each loop and does nothing

my_string = 'Nicolas'

for letter in my_string:
    if letter == 'a':
        continue    # Goes to the top of the closest loop
    print(letter)

for letter in my_string:
    if letter == 'a':
        break    # Breaks and end the loop
    print(letter)

"""While loops"""
bar = 0

while bar < 5:
    print(f'The current value is {bar}')
    bar += 1
else:
    print(f'BAR IS NOT LESS THAN 5')