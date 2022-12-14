from random import choice
from abc import ABC, abstractmethod


rules = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}


class Player(ABC):
    figure = None

    @abstractmethod
    def get_figure(self):
        pass


class Human(Player):

    def get_figure(self):
        self.figure = input("What's your figure? (Rock/Paper/Scissors): ").lower()


class AI(Player):

    def get_figure(self):
        self.figure = choice(list(rules)).lower()


class Game:
    human = None
    ai = None
    res = None
    is_log_writer = None

    def __init__(self, *, log_writer: bool):
        self.is_log_writer = log_writer

    def define_winner(self):
        '''
        Method defines attribute res of Game class object
        '''
        if (self.human.figure, self.ai.figure) in rules.items():
            self.res = 'Congrats, You won!'
        elif (self.ai.figure, self.human.figure) in rules.items():
            self.res = 'Congrats to AI, he won!'
        elif self.human.figure == self.ai.figure:
            self.res = 'DRAW!'
        else:
            self.res = 'Did you write your figure properly? Replay!'

    def text_msg(self):
        '''
        Method prints full statistics of the game
        '''
        if self.human.figure in rules:
            print(f'Your choice is: {self.human.figure.capitalize()}')
            print(f'AI choice is: {self.ai.figure.capitalize()}')
            print(f'\033[1;32m{self.res}')
        else:
            print(f'\033[1;31m{self.res}')

    def log_writer(self):
        '''
        Method logs full statistics of the game. When creating the object of class Game you should turn it on or off:
        Game(log_writer=True/False)
        '''
        with open('game_results.txt', 'r') as file:
            empty_lines = 0
            for line in file:
                if not line.strip():
                    empty_lines += 1
            game_count = empty_lines + 1

        with open('game_results.txt', 'a') as file:
            file.write(f'ROUND {game_count}\n')
            file.write(f'Player choice is: {self.human.figure.capitalize()}\n')
            file.write(f'AI choice is: {self.ai.figure.capitalize()}\n')
            file.write(f'{self.res}\n\n')

    def run(self):
        self.human = Human()
        self.ai = AI()
        self.human.get_figure()
        self.ai.get_figure()
        self.define_winner()
        self.text_msg()
        if self.is_log_writer:
            self.log_writer()
