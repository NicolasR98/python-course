"""Append way (old)"""
my_string = 'Helloo'
my_list = []

for letter in my_string:
    my_list.append(letter)

print(my_list)

my_nested_list = []

for x in [2,4,6]:
    for y in [100,200,300]:
        my_nested_list.append(x*y)

print(my_nested_list)

"""List comprehension (new)"""
my_list = [letter for letter in my_string]

print(my_list)

my_num_list = [x for x in range(0,11)]

print(my_num_list)

my_sqr_num_list = [x**2 for x in range(0,11)]

print(my_sqr_num_list)

my_even_num_list = [x for x in range(0,11) if x%2 == 0]

print(my_even_num_list)

celcius = [0,10,15,22,34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celcius]

print(fahrenheit)

my_nested_list = [x*y for x in [2,4,6] for y in [100,200,300]]

print(my_nested_list)



