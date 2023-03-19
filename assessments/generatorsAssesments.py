import random

# Create a generator that generates the squares of numbers up to some number N.
def gen_squares(n: int):
    for i in range(n):
        yield i ** 2
        
print(*gen_squares(10))

# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
def rand_num(low: int, high: int, qty: int):
    for i in range(qty):
        yield random.randint(low, high)

print(*rand_num(1,10,12))

# Use the iter() function to convert the string below into an iterator:

s = 'Hello world'
next(s)

s_iter = iter(s)
print(next(s_iter))

# Generator comprehension
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)