from tkinter import N
import pytest
import mock
import builtins
from rps import Action, get_computer_move, get_player_move, one_round

def test_get_computer_move():
    action = get_computer_move()
    assert (action in range(3))

def test_get_player_move():
    with mock.patch.object(builtins, 'input', lambda _: '0'):
        assert get_player_move() == Action.Rock
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert get_player_move() == Action.Paper
    with mock.patch.object(builtins, 'input', lambda _: '2'):
        assert get_player_move() == Action.Scissors


actions_win = [(Action.Rock, Action.Paper), (Action.Paper, Action.Scissors)]

@pytest.mark.parametrize("computer, player", actions_win)
def test_one_round_win(capsys, computer, player):
    one_round(player, computer)
    captured = capsys.readouterr()
    assert (captured.out == f'Player win! Computer: {computer.name}, Player: {player.name}\n')

actions_lose = [(Action.Rock, Action.Scissors), (Action.Paper, Action.Rock)]

@pytest.mark.parametrize("computer, player", actions_lose)
def test_one_round_lose(capsys, computer, player):
    one_round(player, computer)
    captured = capsys.readouterr()
    assert (captured.out == f'Player lose! Computer: {computer.name}, Player: {player.name}\n')

actions_tie = [(Action.Rock, Action.Rock), (Action.Paper, Action.Paper)]

@pytest.mark.parametrize("computer, player", actions_tie)
def test_one_round_win(capsys, computer, player):
    one_round(player, computer)
    captured = capsys.readouterr()
    assert (captured.out == f'Tie! Computer: {computer.name}, Player: {player.name}\n')
