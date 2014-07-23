import itertools

def has_sequence(array, n):
    """Finds a sequence of n equal values with consecutive indices in an array
    Returns true if the array contains such a sequence
    """

    return any([True for k, g in itertools.groupby(array) if len(list(g)) >= n])

def checkio(matrix):
    #check the horizontals
    for idx in range(len(matrix[0])):
        if has_sequence(matrix[idx], 4):
            return True

    #transpose the matrix and then check again for horizontals
    t_matrix = zip(*matrix)
    for idx in range(len(t_matrix[0])):
        if has_sequence(t_matrix[idx],4):
            return True

    # check the NW-SE diagonals
    for idx in range(-len(matrix[0])+1, 0):
        diag = [row[i+idx] for i,row in enumerate(matrix) if 0 < i+idx+1 < len(row)]
        if len(diag) >= 4 and has_sequence(diag,4):
            return True

    for idx in range(0, len(matrix[0])):
        diag = [row[i+idx] for i,row in enumerate(matrix) if 0 <= i+idx < len(row)]
        if len(diag) >= 4 and has_sequence(diag,4):
            return True

    # check the NE-SW diagonals
    for idx in range(0,len(matrix[0])):
        diag = [row[-i-(len(matrix[0])-idx)] for i, row in enumerate(matrix) if i in range(0, idx+1)]
        if len(diag) >= 4 and has_sequence(diag,4):
            return True

    for idx in range(0, len(matrix[0])-1):
        diag = [row[-i+idx] for i, row in enumerate(matrix) if i in range(idx+1, len(matrix[0]))]
        if len(diag) >= 4 and has_sequence(diag,4):
            return True

    return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
         [1, 2, 1, 1],
         [1, 1, 4, 1],
         [1, 3, 1, 6],
         [1, 7, 2, 5]
     ]) == True, "Vertical"
    assert checkio([
         [7, 1, 4, 1],
         [1, 2, 5, 2],
         [3, 4, 1, 3],
         [1, 1, 8, 1]
     ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"


