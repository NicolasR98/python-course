def greet(name='User'):
    print(f'Hello {name}')

def check_if_even(number):
    return number % 2 == 0

def get_list_of_events(num_list):
    return [num for num in num_list if check_if_even(num)]

my_list = get_list_of_events([1,2,3,4,5,6,7,8,9,10])
print(my_list)

"""Tuple unpacking function"""
work_hours = [('Abby', 100), ('Bobby', 300), ('Jonhy', 500)]

def get_employee_stats(work_hours):
    max_current_hours = 0
    employee_of_the_month = ''

    for employee,hours in work_hours:
        if hours > max_current_hours:
            employee_of_the_month = employee
            max_current_hours = hours

    return (employee_of_the_month, max_current_hours)

name,hours = get_employee_stats(work_hours)
print(name, hours)