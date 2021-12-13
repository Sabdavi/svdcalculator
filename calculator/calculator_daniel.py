###################################
########## Calculator Class
###################################
class Calculator:
    def __init__(self):
        pass

    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def svd(self):
        pass



###################################
########## Matrix Class
###################################
class Matrix:

    # constructor
    def __init__(self, lst:list):
        """
        Constructor requiring a list. This list contains sublist as row and columns
        :param lst:
        """
        self._matrix = lst

    def dimension(self):
        """
        Get the matrix dimension
        :return: tuple (rows, columns)
        """
        rows = len(self._matrix) # get the number of number of sublist
        cols = len(self._matrix[0]) # get the number of elements of the first sub list
        return rows,cols

    def transpose(self):
        """
        Transpose of a matrix. Each elements [i,j] of the transposed matrix is just the [j,i] elements of the old matrix
        :return:
        """
        rows,cols = self.dimension()
        new_matrix = [[0 for _ in range(rows)] for __ in range(cols)] # create a new matrix with columns as row and vice versa

        for i in range(rows):
            for j in range(cols): # interchange the elements, put the 1st element of each of the lists in the 1st list, and so on and so forth
                new_matrix[j][i] = self._matrix[i][j]
        return new_matrix

    def __str__(self):
        return "{}".format([x for x in self._matrix])





# Examples
# Creating a Matrix instance
Mp = Matrix([[1,3,5],[6,7,8],[0,2,4]])

# printing out the dimension of the matrix
print(Mp.dimension())
# testing the __str__ method to display the class
print(Mp)
# testing the transpose method
print(Mp.transpose())



if __name__ == '__main__':
    calc = Calculator()
