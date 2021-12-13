class SaeidCalc:
    def __init__(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def create_empty_matrix(self, rows, cols):
        empty_matrix = []
        while len(empty_matrix) < rows:
            empty_matrix.append([])
            while len(empty_matrix[-1]) < cols:
                empty_matrix[-1].append(0)

        return empty_matrix

    def subtract(self):
        rows_a = len(self.matrix_a)
        cols_a = len(self.matrix_a[0])
        rows_b = len(self.matrix_b)
        cols_b = len(self.matrix_b[0])

        if rows_a != rows_b or cols_a != cols_b:
            raise ArithmeticError('Matrices are NOT the same size.')

        matrix = self.create_empty_matrix(rows_a, cols_a)
        for i in range(rows_a):
            for j in range(cols_a):
                matrix[i][j] = self.matrix_a[i][j] - self.matrix_b[i][j]

        return matrix

    def row_reduction(self):
        pass


if __name__ == '__main__':
    matrixA = [[1, 5], [4, 5]]
    matrixB = [[2, 15], [14, 25]]
    calc = SaeidCalc(matrixA, matrixB)
    print(calc.subtract())

