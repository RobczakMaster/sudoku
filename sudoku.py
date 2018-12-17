#my first programme in python3

def is_proper(sudoku):
  """
  This function checks if all numbers in each row, column and subsquare are unique.
  """
  return rows_proper(sudoku) and columns_proper(sudoku) and square_proper(sudoku)

def rows_proper(sudoku):
  for row in sudoku:
    for i, element in enumerate(row): # for each element with index i in a row
      if not element:                 # if element = 0 do not compare with other elements
        continue
      for next_el in row[i+1:]:       # for next element to the end of a row
        if element == next_el:
          return False
  return True

def rows_proper2(sudoku):
  nrows = len(sudoku)
  ncols = len(sudoku[0])
  for row_id in range(nrows):
    for col_id in range(ncols):
      element = sudoku[row_id][col_id]
      if not element:
        continue
      for j in range(col_id + 1, ncols):
        next_el = sudoku[row_id][j]
        if element == next_el:
          return False
  return True

def columns_proper(sudoku):
  nrows = len(sudoku)                   # number of rows (elements of sudoku)
  ncols = len(sudoku[0])                # numner of columns = number of elements in first row in sudoku
  for col_id in range(ncols):
    for i in range(nrows):
      element = sudoku[i][col_id]
      if not element:
        continue
      for j in range(i+1, nrows):      #
        next_el = sudoku[j][col_id]    # 
        if element == next_el:
          return False
  return True

def square_proper(sudoku):  # asumption - dim 9x9
  for sqrow in range(3):          # "duży" wiersz (składa się z 3 zwykłych wierszy sudoku)
    for sqcol in range(3):        # "duża" kolumna (z 3 kolumn sudoku)
      for row_id in range(3):     # mały wiersz w dużym wierszu
        for col_id in range(3):   # mała kolumna w dużej kolumnie
          i = sqrow*3 + row_id    # wiersz sudoku zapisany z użyciem dużego i małego wiersza
          j = sqcol*3 + col_id    # analogicznie
          element = sudoku[i][j] # współrzędne elementu
 # współrzędne następnego elementu next_el, z którym porównuję element
          for nrow_id in range(3):
            for ncol_id in range(3):
              m = sqrow*3 + nrow_id
              n = sqcol*3 + ncol_id
              next_el = sudoku[m][n]
              if m==i and n==j:
                continue
              if not element:
                continue
              if element == next_el:          
                return False  
  return True