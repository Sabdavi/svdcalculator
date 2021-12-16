from calculator.saeidcalc import SaeidCalc


def test_matrix_subtract():
    calc = SaeidCalc()
    matrix_a = [[1, 2, 3], [2, 4, 5]]
    matrix_b = [[1, 2, 3], [2, 4, 5]]
    result = [[0, 0, 0], [0, 0, 0]]

    assert result == calc.subtract(matrix_a, matrix_b)


def test_matrix_reduce():
    calc = SaeidCalc()
    matrix = [[0, -7, -4, 2],
              [2, 4, 6, 12],
              [3, 1, -1, -2]]
    reduce = [[1, 0, 0, 1],
              [0, 1, 0, -2],
              [0, 0, 1, 3]]

    calc.row_reduction(matrix)
    assert reduce == calc.round(matrix)


def test_matrix_reduce1():
    calc = SaeidCalc()
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    reduce = [[1, 0, -1, -2],
              [0, 1, 2, 3],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    calc.row_reduction(matrix)
    assert reduce == calc.round(matrix)
