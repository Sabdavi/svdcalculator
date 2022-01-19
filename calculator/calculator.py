from copy import deepcopy


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def __is_square(matrix):
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
    
    @staticmethod
    def get_column(matrix, col):
        return [row[col] for row in matrix]

    @staticmethod
    def __dot_product(v1, v2):
        size = len(v1)
        result = 0
        for i in range(size):
            result = result + (v1[i] * v2[i])
        return result

    @staticmethod
    def __del_row(matrix, row):
        clone = deepcopy(matrix)
        del clone[row]
        return clone

    @staticmethod
    def __del_column(matrix, col):
        # removing the the element with index "col" of from every row
        # use of List comprehension
        return [row[:col] + row[col + 1:] for row in matrix]

    @staticmethod
    def __del_row_col(matrix, row, col):
        reduced_matrix = Calculator.__del_row(Calculator.__del_column(matrix, col), row)
        return reduced_matrix

    @staticmethod
    def calculate_determinant(matrix):
        if not Calculator.__is_square(matrix):
            raise ArithmeticError('The matrix should be square')
        rows = len(matrix)
        if rows == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
        else:
            result = 0
            for i in range(rows):
                # find cofactor for each element of the first row and store the sum in result
                c = (-1) ** (1 + (i + 1)) * matrix[0][i] * Calculator.calculate_determinant(Calculator.__del_row_col(matrix, 0, i))
                result = result + c
            return result

    @staticmethod
    def multiply(matrix1, matrix2):
        # a variable to store the final multiplication result (a 2d array)
        result = []
        # if the passed argument if a scalar (float,int) perform scalar multiplication
        if isinstance(matrix2, (int, float)):
            # use of list comprehension to perform the multiplication
            result = [[element * matrix2 for element in row] for row in
                      matrix1.mMatrix]

        # if the passed argument is another Matrix object
        elif isinstance(matrix2, list):
            # if the the condition for matrix multiplication applies (columns of matrix1 = rows of matrix2)
            if len(matrix1[0]) == len(matrix2):
                for i in range(len(matrix1)):
                    result.append([])
                    for j in range(len(matrix2[0])):
                        row = matrix1[i]
                        # retrieving column j from matrix matrix2
                        column = Calculator.get_column(matrix2, j)
                        # perform dot products of the ith row of matrix1 and jth column of matrix2 and append result
                        result[i].append(Calculator.__dot_product(row, column))
                return result
            # if multiplication condition does not apply throw an exception
            else:
                raise ArithmeticError("col(a) is not equal to row(b)")

    def transpose(self, matrix):
        """
        Transpose of a matrix. Each elements [i,j] of the transposed matrix is just the [j,i] elements of the old matrix
        :return:
        """
        rows, cols = self.dimension()
        new_matrix = [[0 for _ in range(rows)] for __ in range(cols)]  # create a new matrix with columns as row and vice versa
        for i in range(rows):
            for j in range(cols):  # interchange the elements, put the 1st element of each of the lists in the 1st list, and so on and so forth
                new_matrix[j][i] = self._matrix[i][j]
        return new_matrix

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
