from random import randint

PLAY_OPTIONS = ['rock', 'paper', 'scissors']


def play(player_move: str, computer_move: str) -> None:
    if player_move == computer_move:
        print('Tie!, {computer_move=}, {player_move=}')
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

computer_move = PLAY_OPTIONS[randint(0,2)]

player = False

while player == False:
    player_move = (input('Rock, Paper, Scissors?\n')).lower()
    while not validate(player_move):
        player_move = (input('Rock, Paper, Scissors?\n')).lower()
    player = True
    play(player_move, computer_move)



# print(f'{computer_move=}')
# print(f'{player_move=}')