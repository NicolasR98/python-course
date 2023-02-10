"""MAP"""

def square(num): 
    return num ** 2

my_list = [1,2,3,4,5,6]

# If we want to get a list from a map we need to enclose in list()
my_mapped_list = list(map(square, my_list))

print(my_mapped_list)

def splicer(string):
    if len(string) % 2 == 0:
        return 'EVEN'
    else:
        return string[0]

my_name_list = ['Sally', 'Eve', 'Andy']

print(list(map(splicer, my_name_list)))

print(list(map(lambda name: name[::-1], my_name_list)))


"""FILTER"""

def check_even(num): 
    return num % 2 == 0

my_num_list = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(check_even, my_num_list)))

"""LAMBDA FUNCTIONS"""
square_lambda = lambda num: num ** 2

print(list(map(square_lambda, my_num_list)))