from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def get_player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input('Please choose a number between 0 and 2\n')
    
    return int(guess)

def check_if_match(my_list, user_guess):
    if my_list[user_guess] == 'O':
        print(f'You won! | Selected {user_guess} | {my_list}')
    else:
        print(f'You Lose! | Selected {user_guess} | {my_list}')


def start_game():
    initial_list = shuffle_list(['','O',''])
    user_guess = get_player_guess()
    
    check_if_match(initial_list, user_guess)

start_game()