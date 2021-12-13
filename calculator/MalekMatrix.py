from copy import deepcopy


class Matrix:
    mMatrix = []

    def __init__(self, matrix):
        self.mMatrix = matrix

    # -----------------------Helper Methods -------------------------------------------------------

    # function to check if the matrix is an NxN square matrix
    @staticmethod
    def __is_square(matrix):
        for row in matrix:
            if len(matrix) != len(row):
                return False
        return True

    # helper function to remove a row from a matrix without altering the original matrix
    @staticmethod
    def del_row(matrix, row):
        clone = deepcopy(matrix)
        del clone[row]
        return clone

    # helper function to remove a column from a matrix without altering the original matrix
    @staticmethod
    def del_column(matrix, col):
        # removing the the element with index "col" of from every row
        # use of List comprehension
        return [row[:col] + row[col + 1:] for row in matrix]

    @staticmethod
    def get_column(matrix, col):
        return [row[col] for row in matrix]

    @staticmethod
    def dot_product(v1, v2):
        size = len(v1)
        result = 0
        for i in range(size):
            result = result + (v1[i] * v2[i])
        return result

    # helper method to remove a specific row and a column from a matrix
    # returning a modified copy without altering the original matrix
    @staticmethod
    def del_row_col(matrix, row, col):
        reduced_matrix = Matrix.del_row(Matrix.del_column(matrix, col), row)
        return reduced_matrix

    # private static recursive method to find the determinant
    @staticmethod
    def __determinant(matrix):
        # if Matrix is not square the determinant can't be calculated
        if not Matrix.__is_square(matrix):
            return None
        # at this point we know the Matrix is square so number of rows equals number of columns
        rows = len(matrix)
        # if Matrix is 2x2 simply calculate the determinant
        if rows == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])

        # if matrix is NxN do expansion through the first row and find determinants for smaller matrices recursively
        else:
            result = 0
            for i in range(rows):
                # find cofactor for each element of the first row and store the sum in result
                c = (-1) ** (1 + (i + 1)) * matrix[0][i] * Matrix.__determinant(Matrix.del_row_col(matrix, 0, i))
                result = result + c
            return result

    # ---------------------- Main Methods -------------------------------------------

    # the main method to find the determinant
    def determinant(self):
        # calling private method __determinant() to calculate the determinant recursively
        d = Matrix.__determinant(self.mMatrix)
        Matrix.dot_product(d, d)
        return d

    # multiply method takes another Matrix Object and returns a new Matrix object which is the result of the
    # multiplication if the wrong argument is passed to multiply() or multiplication is not possible it None is
    # returned for now
    def multiply(self, product):
        # a variable to store the final multiplication result (a 2d array)
        result = []
        # if the passed argument if a scalar (float,int) perform scalar multiplication
        if isinstance(product, (int, float)):
            # use of list comprehension to perform the multiplication
            result = [[element * product for element in row] for row in
                      self.mMatrix]

        # if the passed argument is another Matrix object
        elif isinstance(product, Matrix):
            A = self.mMatrix
            B = product.mMatrix
            # if the the condition for matrix multiplication applies (rows of A = columns of B)
            if len(A[0]) == len(B):
                for i in range(len(A)):
                    result.append([])
                    for j in range(len(B)):
                        row = A[i]
                        # retrieving column j from matrix B
                        column = Matrix.get_column(B, j)
                        # perform dot products of the ith row of A and jth column of B and append result
                        result[i].append(Matrix.dot_product(row, column))
            # if multiplication condition does not apply set result to None
            else:
                result = None
        # if passed argument is not supported set result to None
        else:
            result = None

        if result is not None:
            # if result is not None return create a Matrix Object and return it
            return Matrix(result)
        else:
            return None

    def __str__(self):
        # like done in class
        result = []
        for row in self.mMatrix:
            for element in row:
                result.append(str(element))
                result.append(" ")
            result.append("\n")
        return "".join(result)
