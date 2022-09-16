import colorama
from random import randint, choice
# from tkinter import *


PLAY_OPTIONS = ['rock', 'paper', 'scissors']


def one_round(player_move: str, computer_move: str) -> None:
    if player_move == computer_move:
        print(f'Tie!, {computer_move=}, {player_move=}')
    elif computer_move == 'rock':
        if player_move == 'scissors':
            print(f'Player lose! {computer_move=}, {player_move=}')
        else:
            print(f'Player win! {computer_move=}, {player_move=}')
    elif computer_move == 'scissors':
        if player_move == 'paper':
            print(f'Player lose! {computer_move=}, {player_move=}')
        else:
            print(f'Player win! {computer_move=}, {player_move=}')
    elif computer_move == 'paper':
        if player_move == 'rock':
            print(f'Player lose! {computer_move=}, {player_move=}')
        else:
            print(f'Player win! {computer_move=}, {player_move=}')

def validate(move: str) -> bool:
    if move not in PLAY_OPTIONS:
        print(f'Player input {move} is not valid, please enter again!')
        return False
    return True

## TODO: Input control | rock -> r, 1
## TODO: OOP design
## TODO: GUI with TKINTER or pyqt5
# brew install python-tk

def clear_screen() -> None:
    print(colorama.ansi.clear_screen(), end='')

def main():
    # computer_move = PLAY_OPTIONS[randint(0,2)]
    computer_move = choice(PLAY_OPTIONS)

    player = False

    while player == False:
        player_move = (input('Rock, Paper, Scissors?\n')).lower()
        while not validate(player_move):
            player_move = (input('Rock, Paper, Scissors?\n')).lower()
        player = True
        one_round(player_move, computer_move)
    
        play_again = input('Play again? (y/n): ')
        player = 'n'.__eq__(play_again.lower())

if __name__ == "__main__":
    try:
        colorama.init()
        clear_screen()
        main()
    finally:
        colorama.deinit()

