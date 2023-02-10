def get_five_percent_of_sum(*args):
    return sum(args) * 0.5

print(get_five_percent_of_sum(20,30,40,50))

def say_fruit(**kwargs):
    if 'fruit' in kwargs:
        print('I found my fruit {}'.format(kwargs['fruit']))
    else: print('Nevermind')

say_fruit(fruit = 'apple')


def ask_for_food(*args, **kwargs):
    print('I would like {qty} {food}'.format(qty = args[0], food = kwargs['food']))

ask_for_food(5, food = 'nuggets')