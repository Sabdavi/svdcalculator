
from calculator import root_calculator




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






