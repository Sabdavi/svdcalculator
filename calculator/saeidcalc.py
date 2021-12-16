class SaeidCalc:
    def __init__(self):
        pass

    def create_empty_matrix(self, rows, cols):
        empty_matrix = []
        while len(empty_matrix) < rows:
            empty_matrix.append([])
            while len(empty_matrix[-1]) < cols:
                empty_matrix[-1].append(0)

        return empty_matrix

    def subtract(self, matrix_a, matrix_b):
        rows_a = len(matrix_a)
        cols_a = len(matrix_a[0])
        rows_b = len(matrix_b)
        cols_b = len(matrix_b[0])

        if rows_a != rows_b or cols_a != cols_b:
            raise ArithmeticError('Matrices are NOT the same size.')

        matrix = self.create_empty_matrix(rows_a, cols_a)
        for i in range(rows_a):
            for j in range(cols_a):
                matrix[i][j] = self.matrix_a[i][j] - self.matrix_b[i][j]

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
            matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
            for i in range(row_count):
                if i != r:
                    lv = matrix[i][lead]
                    if lv != 0:
                        matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
            lead += 1
        return self.__round(matrix)

    def __round(self, matrix):
        for i in range(len(matrixC)):
            for j in range(len(matrixC[0])):
                matrixC[i][j] = round(matrixC[i][j])
        return matrix


if __name__ == '__main__':
    calc = SaeidCalc()

    matrixC = [[0, -7, -4, 2],
               [2, 4, 6, 12],
               [3, 1, -1, -2]]

    reduction = calc.row_reduction(matrixC)

    print(reduction)

