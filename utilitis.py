import numpy as np
def convertMatrixToArray(matrix):
    array = []
    for vec in matrix:
        for i in vec:
            array.append(float(i))
    return np.array(array)

def convertMatrixToDic(matrix):
    m = n = 0
    dic = {}
    for vec in matrix:
        n = 0
        for i in vec:
            dic[(m,n)] = i
            n += 1
        m += 1
    return dic


    