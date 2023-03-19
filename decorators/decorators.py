# Decorator example
def make_pretty_func(func):
    def inner():
        print('Making it prettier')
        func()
    return inner
def my_func():
    print('I am a func')
    
my_decorated_func = make_pretty_func(my_func)
my_decorated_func()

# Decorator with @
@make_pretty_func
def my_func():
    print('I am a func 2')

my_func()