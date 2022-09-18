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

def test_one_round(capsys):
    computer = Action.Rock
    player = Action.Paper
    one_round(player, computer)
    # assert (one_round(player, computer) == 'Player lose! Computer: Rock, Player: Paper')
    captured = capsys.readouterr()
    assert (captured.out == 'Player win! Computer: Rock, Player: Paper')