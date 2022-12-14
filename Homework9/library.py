from random import choice
from functools import wraps
import time


rules = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}


def get_player_figure():
    '''
    func gets a figure chosen by human and returns the figure
    '''
    global player_figure
    player_figure = input("What's your figure? (Rock/Paper/Scissors): ").lower()
    return player_figure


def get_ai_figure():
    '''
    func gets a figure chosen by AI and returns the figure
    '''
    global ai_figure
    ai_figure = choice(list(rules)).lower()
    return ai_figure


def define_winner():
    '''
    func defines the winner and returns game results
    '''
    global text_message
    if (player_figure, ai_figure) in rules.items():
        text_message = 'Congrats, You won!'
    elif (ai_figure, player_figure) in rules.items():
        text_message = 'Congrats to AI, he won!'
    elif player_figure == ai_figure:
        text_message = 'DRAW!'
    else:
        text_message = 'Did you write your figure properly? Replay!'
    return text_message


def text_msg():
    '''
    func prints the result
    '''
    if player_figure in rules:
        print(f'Your choice is: {player_figure.capitalize()}')
        print(f'AI choice is: {ai_figure.capitalize()}')
        print(f'\033[1;32m{text_message}')
    else:
        print(f'\033[1;31m{text_message}')


def log_writer():
    '''
    func writes logs for rounds of game
    '''
    with open('game_results.txt', 'r') as file:
        empty_lines = 0
        for line in file:
            if not line.strip():
                empty_lines += 1
        game_count = empty_lines + 1

    with open('game_results.txt', 'a') as file:
        file.write(f'ROUND {game_count}\n')
        file.write(f'Player choice is: {player_figure.capitalize()}\n')
        file.write(f'AI choice is: {ai_figure.capitalize()}\n')
        file.write(f'{text_message}\n\n')


def game():
    '''
    func is made to compose the game
    '''
    get_player_figure()
    get_ai_figure()
    define_winner()
    text_msg()
    log_writer()


def time_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('\033[1;30mThe game lasted', round((end - start), 2), 'Seconds')
        return res
    return wrapper
