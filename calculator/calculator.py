from copy import deepcopy


class Calculator:
    def __init__(self):
        pass

    def __is_square(self, matrix):
        for row in matrix:
            if len(matrix) != len(row):
                return False
        return True

    def __create_empty_matrix(self, rows, cols):
        empty_matrix = []
        while len(empty_matrix) < rows:
            empty_matrix.append([])
            while len(empty_matrix[-1]) < cols:
                empty_matrix[-1].append(0)

        return empty_matrix

    def round(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = round(matrix[i][j])
        return matrix

    def __del_row(self, matrix, row):
        clone = deepcopy(matrix)
        del clone[row]
        return clone

    def __del_column(self, matrix, col):
        # removing the the element with index "col" of from every row
        # use of List comprehension
        return [row[:col] + row[col + 1:] for row in matrix]

    def __del_row_col(self, matrix, row, col):
        reduced_matrix = self.__del_row(self.__del_column(matrix, col), row)
        return reduced_matrix

    def calculate_determinant(self, matrix):
        if not self.__is_square(matrix):
            raise ArithmeticError('The matrix should be square')
        rows = len(matrix)
        if rows == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
        else:
            result = 0
            for i in range(rows):
                # find cofactor for each element of the first row and store the sum in result
                c = (-1) ** (1 + (i + 1)) * matrix[0][i] * self.calculate_determinant(self.__del_row_col(matrix, 0, i))
                result = result + c
            return result

    @staticmethod
    def multiply(A, B):
        # a variable to store the final multiplication result (a 2d array)
        result = []
        # if the passed argument if a scalar (float,int) perform scalar multiplication
        if isinstance(B, (int, float)):
            # use of list comprehension to perform the multiplication
            result = [[element * B for element in row] for row in
                      A.mMatrix]

        # if the passed argument is another Matrix object
        elif isinstance(B, Matrix):
            M1 = A.mMatrix
            M2 = B.mMatrix
            # if the the condition for matrix multiplication applies (columns of M1 = rows of M2)
            if len(M1[0]) == len(M2):
                for i in range(len(M1)):
                    result.append([])
                    for j in range(len(M2[0])):
                        row = M1[i]
                        # retrieving column j from matrix M2
                        column = Matrix.get_column(M2, j)
                        # perform dot products of the ith row of M1 and jth column of M2 and append result
                        result[i].append(Matrix.__dot_product(row, column))
            # if multiplication condition does not apply set result to None
            else:
                result = None
        # if passed argument is not supported set result to None
        else:
            result = None

        if result is not None:
            # if result is not None create a Matrix Object and return it
            return Matrix(result)
        else:
            return None
        

    def transpose(self, matrix):
        pass

    def subtract(self, matrix_a, matrix_b):
        rows_a = len(matrix_a)
        cols_a = len(matrix_a[0])
        rows_b = len(matrix_b)
        cols_b = len(matrix_b[0])

        if rows_a != rows_b or cols_a != cols_b:
            raise ArithmeticError('Matrices are NOT the same size.')

        matrix = self.__create_empty_matrix(rows_a, cols_a)
        for i in range(rows_a):
            for j in range(cols_a):
                matrix[i][j] = matrix_a[i][j] - matrix_b[i][j]

        return matrix

    def row_reduction(self, matrix):
        if not matrix:
            raise ArithmeticError('Matrices are NOT provided')
        lead = 0
        row_count = len(matrix)
        column_count = len(matrix[0])
        for r in range(row_count):
            if lead >= column_count:
                return
            i = r
            while matrix[i][lead] == 0:
                i += 1
                if i == row_count:
                    i = r
                    lead += 1
                    if column_count == lead:
                        return
            matrix[i], matrix[r] = matrix[r], matrix[i]
            lv = matrix[r][lead]
            matrix[r] = [mrx / lv for mrx in matrix[r]]
            for i in range(row_count):
                if i != r:
                    lv = matrix[i][lead]
                    if lv != 0:
                        matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
            lead += 1
