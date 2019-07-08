def multiply(m1, m2):
    m1_column = len(m1[0])
    m2_row = len(m2)
    if (m1_column == m2_row):
        newMatrix = []
        k = 0
        while (k < len(m1)):
            rowArr = []
            h = 0
            while (h < len(m2[0])):
                result = 0
                i = 0
                while (i < len(m1[0])):
                    result += m1[k][i] * m2[i][h]
                    i += 1
                rowArr.append(result)
                h += 1
            newMatrix.append(rowArr)
            k += 1
        newMatrix.append("Multiplication")
        return newMatrix
    else:
        return "Matrix_1 column must equal Matrix_2 row"

def makeMatrix(number):
    matrix = []
    row = int(input("\nMatrix_" + str(number) + " Rows: "))
    for i in range(1, row + 1):
        rowArr = input("Row " + str(i) + ": ").split(" ")
        for j in range(0, len(rowArr)):
            rowArr[j] = int(rowArr[j])
        matrix.append(rowArr)
    return matrix

def showMatrix(matrix):
    result = matrix.pop()
    print(f"\n----------- Result of {result} --------------")
    if (type(matrix) == str):
        print("\n" + matrix)
    else:
        for row in matrix:
            print("\t", row)

def add(m1, m2):
    if (checkDimension(m1, m2)):
        newMatrix = []
        for i in range(0, len(m1)):
            rowArr = []
            for j in range(0, len(m1)):
                rowArr.append(m1[i][j] + m2[i][j])
            newMatrix.append(rowArr)
        newMatrix.append("Addition")
        return newMatrix
    else:
        return "{}x{} and {}x{} addition is not applicable".format(len(m1), len(m1[0]), len(m2), len(m2[0]))

def subtract(m1, m2):
    if(checkDimension(m1, m2)):
        newMatrix = []
        for i in range(0, len(m1)):
            rowArr = []
            for j in range(0, len(m1)):
                rowArr.append(m1[i][j] - m2[i][j])
            newMatrix.append(rowArr)
        newMatrix.append("Subtraction")
        return newMatrix
    else:
        return "{}x{} and {}x{} subtraction is not applicable".format(len(m1), len(m1[0]), len(m2), len(m2[0]))

def checkDimension(m1, m2):
    m1_row = len(m1)
    m1_column = len(m1[0])
    m2_row = len(m2)
    m2_column = len(m2[0])
    if (m1_row == m2_row and m1_column == m2_column):
        return True
    else:
        return False

matrix_1 = makeMatrix(1)
matrix_2 = makeMatrix(2)


showMatrix(add(matrix_1, matrix_2))
showMatrix(subtract(matrix_1, matrix_2))
showMatrix(multiply(matrix_1, matrix_2))