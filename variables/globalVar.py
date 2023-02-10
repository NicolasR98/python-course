x = 10

def my_func(x):
    print(f'x is {x}')

    x = 200

    print(f'x changed to be {x}')

my_func(x)
print(f'global x is {x}')

def my_other_func():
    global x
    print(f'x is {x}')

    x = 200

    print(f'x changed to be {x}')

my_other_func()
print(f'global x is {x}')