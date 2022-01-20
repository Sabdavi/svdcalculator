from copy import deepcopy
from calculator import root_calculator

class Calculator:
    def __init__():
        pass

    @staticmethod
    def __is_square(matrix):
        for row in matrix:
            if len(matrix) != len(row):
                return False
        return True

    def __create_empty_matrix(rows, cols):
        empty_matrix = []
        while len(empty_matrix) < rows:
            empty_matrix.append([])
            while len(empty_matrix[-1]) < cols:
                empty_matrix[-1].append(0)

        return empty_matrix

    def round(matrix):
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

    def transpose(matrix):
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
    
    
    def __add__(other):
        #Creating a new matrix where the result of addition will be stored
        new_matrix = []

        # Checking if the dimensions of two matrices are the same
        if len(self.new_matrix) != len(other.new_matrix) or len(self.new_matrix[0]) != len(other.new_matrix[0]):
          raise ArithmeticError('Matrices are not the same size!')
        # Using for-loop to add up the elements of two matrices
        for i in range(len(self.new_matrix)):
            new_matrix.append([])
            for j in range(len(self.new_matrix[0])):
                new_matrix[i].append(self.new_matrix[i][j] + other.new_matrix[i][j])

        return new_matrix
    

    def subtract(matrix_a, matrix_b):
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

    def row_reduction(matrix):
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

    def matrix_dimensions(m):
      """
      Following function returns dimensions of any given matrix m
      @param m: matrix (list of lists) with float values.
      @return: a list of values showing matrix dimensions
      """
      return [len(m),len(m[0])]


    def identity_m(dims):
        """
        Return an identity matrix of any given dimensions.
        :param dims: A list of values.
        :return: A list of lists of values containing the identity matrix.
        """
        m = [[0 for k in range(dims[1])] for j in range(dims[0])]
        for j in range(dims[0]):
            m[j][j] = 1
        return m


    def multiplying_lists(l1,l2):
      """
      Using FOIL (First Outside, Inside Last) method to multiply two lists. 
      The Lists are treated as factors.
      l1 and l2 are lists of float values.
      returns the result of multiplication which is also a list containing float values
      """
      res = [0 for i in range(len(l1)+len(l2)-1)]
      for j in range(len(l1)):
        for k in range(len(l2)):
          res[j+k] += l1[j] * l2[k]
      return res


    def adding_lists(l1,l2, subtract=1):

      """
      Following function calculates the addition of two lists.
      parameter subtract, if set to -1, does subtraction instead of addition.
      the function returns the result of addition as a list of float values.
      """
      return [i+(subtract*j) for i,j in zip(l1,l2)]

    def det_eq(m,exclude=[1,0]):
      """
      Given function returns determinant equation in terms of x variable.
      index of the elements in the list represents the power of x variable.
      E.g. [a,b,c] corresponds to a + bx + cx^2
      parameters:
      m - matrix presented as a list of lists with float values.
      exclude - values of rows and columns of matrices that are excluded during calculation. for 2x2 matrix [1,0] are excluded by default.
      returns:
      list of respective float values of determinant equation.
      """
      dims = matrix_dimensions(m)
      if dims == [2,2]:
        temp = adding_lists(multiplying_lists(m[0][0],m[1][1]),multiplying_lists(m[0][1],m[1][0]),subtract=-1)
        return multiplying_lists(temp,exclude)
      else:
        exclude=[]
        new_m=[]
        exclude_r = 0
        for exclude_col in range(dims[1]):
          temp=[]
          exclude.append(m[exclude_r][exclude_col])
          for row in range(1,dims[0]):
            temp_row =[]
            for col in range(dims[1]):
              if (row!= exclude_r) & (col != exclude_col):
                temp_row.append(m[row][col])
            temp.append(temp_row)
          new_m.append(temp)
        det_equations = [det_eq(new_m[j],exclude[j]) for j in range(len(new_m))]

        final_det_eq = [sum(el) for el in zip(*det_equations)]

        return final_det_eq

    def charact_eq(m):
      """
      The given function gives the characeristic equation of a given matrix m.
      parameters:
      m : matrix presented as a list of lists with float values.
      returns:
      list of lists with float values corresponding to characteristic equation.
      """
      dims = matrix_dimensions(m)

      return [[[x,-y] for x,y in zip(i,j)] for i,j in zip(m,identity_m(dims))]


    def eigenvalues_m(m):
      """
      The given function gives eigenvalues of matrix m in an array of float values.
      parameter:
      m - matrix presented as a list of lists with float values.
      returns: array of float values with corresponding eigenvalues of matrix m
      """
      final_det_eq = det_eq(charact_eq(m))
      return root_calculator.RootCalculator.solve(final_det_eq[::-1])
