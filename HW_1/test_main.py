import pytest
from HW_1.main import Board


@pytest.fixture()
def get_empty_board():
    return Board()


@pytest.fixture()
def get_full_board():
    board = Board()
    board.grid = [['0', '0', '0'],
                  ['0', '0', '0'],
                  ['0', '0', '0']]
    return board


def test_is_empty(get_empty_board, get_full_board):
    for i in range(3):
        for j in range(3):
            assert get_empty_board.is_empty(i, j) is True
    for i in range(3):
        for j in range(3):
            assert get_full_board.is_empty(i, j) is False


@pytest.mark.parametrize(
    ('row', 'column', 'key'), [
        (1, 2, 'X'),
        (2, 2, '0'),
        (1, 1, 'X'),
        (0, 1, '0'),
        (2, 0, 'X'),
    ]
)
def test_insert(row, column, key, get_empty_board):
    assert get_empty_board.grid[row][column] == '.'
    get_empty_board.insert(row, column, key)
    assert get_empty_board.grid[row][column] == key


def test_is_full(get_full_board, get_empty_board):
    assert get_empty_board.is_full() is False
    assert get_full_board.is_full() is True
    get_full_board.insert(0, 0, '.')
    assert get_full_board.is_full() is False


@pytest.mark.parametrize(
    ('grid', 'key', 'column', 'expected'), [
        ([['X', '.', '.'],
         ['X', '.', '.'],
         ['X', '.', 'X']], 'X', 0, True),
        ([['X', 'X', '.'],
         ['.', 'X', '.'],
         ['.', '0', '.']], 'X', 1, False),
        ([['0', '.', '.'],
         ['.', 'X', '.'],
         ['.', '.', '0']], '0', 2, False),
        ([['0', '.', '0'],
         ['.', '.', '0'],
         ['0', '.', '0']], '0', 2, True),
        ([['.', '0', '0'],
         ['.', '0', '.'],
         ['0', '0', '.']], 'X', 1, False),
    ]
)
def test_check_column(grid, key, column, expected, get_empty_board):
    get_empty_board.grid = grid
    assert get_empty_board.check_column(column, key) == expected


@pytest.mark.parametrize(
    ('grid', 'key', 'row', 'expected'), [
        ([['X', '.', '.'],
         ['.', 'X', '.'],
         ['.', '.', 'X']], 'X', 0, False),
        ([['X', '.', '.'],
         ['0', 'X', '0'],
         ['.', '.', 'X']], '0', 1, False),
        ([['0', '.', '.'],
         ['.', 'X', '.'],
         ['0', '0', '0']], '0', 2, True),
        ([['0', '0', '0'],
         ['.', '.', '.'],
         ['0', '.', '.']], '0', 0, True),
        ([['X', 'X', 'X'],
         ['.', '0', '.'],
         ['0', '0', '0']], 'X', 2, False),
        ([['0', '.', 'X'],
          ['.', '0', '.'],
          ['0', '.', '.']], '0', 0, False),
    ]
)
def test_check_row(grid, key, row, expected, get_empty_board):
    get_empty_board.grid = grid
    assert get_empty_board.check_row(row, key) == expected


@pytest.mark.parametrize(
    ('grid', 'key', 'expected'), [
        ([['X', '.', '.'],
         ['.', 'X', '.'],
         ['.', '.', 'X']], 'X', True),
        ([['X', '.', '.'],
         ['.', 'X', '.'],
         ['.', '.', 'X']], '0', False),
        ([['0', '.', '.'],
         ['.', 'X', '.'],
         ['.', '.', '0']], '0', False),
        ([['.', '.', '0'],
         ['.', '0', '.'],
         ['0', '.', '.']], '0', True),
        ([['.', '.', '0'],
         ['.', '0', '.'],
         ['0', '.', '.']], 'X', False),
        ([['.', '.', 'X'],
          ['.', '0', '.'],
          ['0', '.', '.']], '0', False),
    ]
)
def test_check_diagonals(grid, key, expected, get_empty_board):
    get_empty_board.grid = grid
    assert get_empty_board.check_diagonals(key) == expected

