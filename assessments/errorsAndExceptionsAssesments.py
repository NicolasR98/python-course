"""
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
"""

def problem_1():
    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print("Can't use operand pow on 'str'")

"""
Problem 2
Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
"""

def problem_2():
    try:
        x = 5
        y = 0
        z = x/y
    except ZeroDivisionError:
        print("You can't divide by zero, fool")

"""
Problem 3
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, 
else block to account for incorrect inputs.
"""

def problem_3():
    while True:
        try:
            input_num = int(input('Input an integer: '))
        except ValueError:
            print('You have to introduce a number!')
        except EOFError:
            print('\nBye...')
            break
        else:
            print(f'Thank you, your number squared is: {input_num ** 2}')
            break

# problem_1()
# problem_2()
# problem_3()
