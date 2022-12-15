import csv
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
    winner = None

    def __init__(self, *, log_writer: bool):
        self.is_log_writer = log_writer

    def define_winner(self):
        '''
        Defines attribute res of Game class object; defines the winner attribute
        '''
        if (self.human.figure, self.ai.figure) in rules.items():
            self.res = 'Congrats, You won!'
            self.winner = 'Human'
        elif (self.ai.figure, self.human.figure) in rules.items():
            self.res = 'Congrats to AI, he won!'
            self.winner = 'AI'
        elif self.human.figure == self.ai.figure:
            self.res = 'DRAW!'
            self.winner = 'DRAW!'
        else:
            self.res = 'Did you write your figure properly? Replay!'
            self.winner = "The game didn't happen"

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
        with open('game_res.csv', 'r') as filename:
            file = csv.DictReader(filename)
            rounds = []
            try:
                for col in file:
                    rounds.append(col['Round'])
                round_count = int(rounds[-1]) + 1
                write_header = False
            except:
                round_count = 1
                write_header = True
        with open('game_res.csv', 'a') as file:
            header = ['Round', 'Human', 'AI', 'Result']
            data = [round_count, self.human.figure.capitalize(), self.ai.figure.capitalize(), self.winner]
            writer = csv.writer(file)
            if write_header:
                writer.writerow(header)
            writer.writerow(data)

    def run(self):
        self.human = Human()
        self.ai = AI()
        self.human.get_figure()
        self.ai.get_figure()
        self.define_winner()
        self.text_msg()
        if self.is_log_writer:
            self.log_writer()
