def my_func():
    print('Hello from myModule.py')

# When executing this script, __name__ will be assigned with '__main__'

if __name__ == '__main__':
    # This block of code is executed only when the the module is being run directly
    print('This module is being run directly')
    my_func()