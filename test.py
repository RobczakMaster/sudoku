# tests for sudoku

#test for verification functions

import unittest
import sudoku

rows_ok_bad_cols = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

bad_rows_cols_ok = [
  [1, 1, 9, 4, 6, 1, 0, 0, 0],
  [2, 2, 8, 1, 5, 2, 1, 1, 0],
  [3, 3, 7, 2, 4, 3, 2, 2, 0],
  [0, 4, 6, 3, 3, 4, 3, 3, 1],
  [0, 5, 5, 5, 2, 5, 4, 4, 2],
  [4, 6, 4, 6, 1, 9, 5, 0, 3],
  [5, 7, 3, 7, 7, 8, 6, 5, 4],
  [6, 8, 2, 8, 8, 7, 7, 6, 5],
  [7, 9, 1, 9, 9, 6, 8, 8, 6],
]

empty = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

bad_square = [
  [1, 2, 3, 0, 0, 0, 0, 0, 0],
  [4, 5, 6, 0, 0, 0, 0, 0, 0],
  [7, 8, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

squares_ok = [
  [1, 2, 3, 1, 2, 3, 1, 2, 3],
  [4, 5, 6, 4, 5, 6, 4, 5, 6],
  [7, 8, 9, 7, 8, 9, 7, 8, 9],
  [1, 2, 3, 1, 2, 3, 1, 2, 3],
  [4, 5, 6, 4, 5, 6, 4, 5, 6],
  [7, 8, 9, 7, 8, 9, 7, 8, 9],
  [1, 2, 3, 1, 2, 3, 1, 2, 3],
  [4, 5, 6, 4, 5, 6, 4, 5, 6],
  [7, 8, 9, 7, 8, 9, 7, 8, 9],
]

class BoardProperTest(unittest.TestCase):
  def test_rows_ok(self):
    self.assertTrue(sudoku.rows_proper(rows_ok_bad_cols))
    
  def test_bad_column(self):
    self.assertFalse(sudoku.columns_proper(rows_ok_bad_cols))
        
  def test_cols_ok(self):
    self.assertTrue(sudoku.columns_proper(bad_rows_cols_ok))
  
  def test_bad_rows(self):
    self.assertFalse(sudoku.rows_proper(bad_rows_cols_ok))
    
  def test_empty_isproper(self):
    self.assertTrue(sudoku.is_proper(empty))
    
  def test_bad_squares(self):
    self.assertFalse(sudoku.square_proper(bad_square))
    
  def test_squares_ok(self):
    self.assertTrue(sudoku.square_proper(squares_ok))
    

if __name__ == "__main__":
  unittest.main()
