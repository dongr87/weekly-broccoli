from distutils.log import error
from multiprocessing.sharedctypes import Value
import colorama
from random import randint
from enum import IntEnum
import logging

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def one_round(player_move: Action, computer_move: Action) -> None:
    victories = {
        Action.Rock: [Action.Scissors],  # Rock beats scissors
        Action.Paper: [Action.Rock],  # Paper beats rock
        Action.Scissors: [Action.Paper]  # Scissors beats paper
    }
    defeats = victories[player_move]

    if player_move == computer_move:
        print(f'Tie! Computer: {computer_move.name}, Player: {player_move.name}')
    elif computer_move in defeats:
        print(f'Player win! Computer: {computer_move.name}, Player: {player_move.name}')
    else:
        print(f'Player lose! Computer: {computer_move.name}, Player: {player_move.name}')


def get_player_move() -> Action:
    user_input = input('Enter a choice (Rock[0], Paper[1], Scissors[2]): \n')
    try:
        move = int(user_input)
    except:
        logging.error(f'Value error')
        print(f'Player input {user_input} is not valid, please enter again!')

    return Action(move)

def get_computer_move() -> Action:
    choice = randint(0, len(Action) - 1)
    return Action(choice)

## TODO: GUI with TKINTER or pyqt5
# brew install python-tk

def clear_screen() -> None:
    print(colorama.ansi.clear_screen(), end='')

def main():
    again = True

    while True:
        try:
            player_move = get_player_move()
        except ValueError as e:
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        computer_move = get_computer_move()
        one_round(player_move, computer_move)
    
        play_again = input('Play again? (y/n): ')
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    try:
        colorama.init()
        clear_screen()
        main()
    finally:
        colorama.deinit()
