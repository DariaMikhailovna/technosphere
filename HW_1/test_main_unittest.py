import unittest
from HW_1.main import Board


class BoardTestCase(unittest.TestCase):
    def setUp(self):
        board = Board()
        board.grid = [['0', '0', '0'],
                      ['0', '0', '0'],
                      ['0', '0', '0']]
        self.full_board = board
        self.empty_board = Board()
        self.set_for_insert = [
            (1, 2, 'X'),
            (2, 2, '0'),
            (1, 1, 'X'),
            (0, 1, '0'),
            (2, 0, 'X'),
        ]
        self.set_for_column = [
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
        self.set_for_row = [
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
        self.set_for_diagonal = [
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

    def test_is_empty(self):
        for i in range(3):
            for j in range(3):
                self.assertTrue(self.empty_board.is_empty(i, j))
        for i in range(3):
            for j in range(3):
                self.assertFalse(self.full_board.is_empty(i, j))

    def test_insert(self):
        for i in range(len(self.set_for_insert)):
            self.assertEqual(self.empty_board.grid[self.set_for_insert[i][0]][self.set_for_insert[i][1]], '.')
            self.empty_board.insert(self.set_for_insert[i][0], self.set_for_insert[i][1], self.set_for_insert[i][2])
            self.assertEqual(self.empty_board.grid[self.set_for_insert[i][0]][self.set_for_insert[i][1]],
                             self.set_for_insert[i][2])

    def test_is_full(self):
        self.assertFalse(self.empty_board.is_full())
        self.assertTrue(self.full_board.is_full())
        self.full_board.insert(0, 0, '.')
        self.assertFalse(self.full_board.is_full())

    def test_check_column(self):
        for i in range(len(self.set_for_column)):
            self.empty_board.grid = self.set_for_column[i][0]
            self.assertEqual(self.empty_board.check_column(self.set_for_column[i][2], self.set_for_column[i][1]),
                             self.set_for_column[i][3])

    def test_check_row(self):
        for i in range(len(self.set_for_row)):
            self.empty_board.grid = self.set_for_row[i][0]
            self.assertEqual(self.empty_board.check_row(self.set_for_row[i][2], self.set_for_row[i][1]),
                             self.set_for_row[i][3])

    def test_check_diagonals(self):
        for i in range(len(self.set_for_row)):
            self.empty_board.grid = self.set_for_diagonal[i][0]
            self.assertEqual(self.empty_board.check_diagonals(self.set_for_diagonal[i][1]), self.set_for_diagonal[i][2])
