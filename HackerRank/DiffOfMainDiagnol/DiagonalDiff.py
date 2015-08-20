
def main():

    matrixSize =int(input())
    intput_matrix = ""
    for i in range(1,matrixSize+1):
        value = input()
        if(i==matrixSize):
            intput_matrix = intput_matrix+value
        else:
            intput_matrix = intput_matrix+value+'\n'

    matrix = create_matrix(matrixSize,intput_matrix)

    left_diagonal = left_diagonal_sum(matrix,matrixSize)
    right_diagonal = right_diagonal_sum(matrix,matrixSize)

    # print("lft:" + str(left_diagonal))
    # print("rt:" + str(right_diagonal))

    diff = left_diagonal-right_diagonal

    print(abs(diff))


def left_diagonal_sum(matrix,matrix_size):

    sum = 0
    for i in range(0,matrix_size):
        sum = sum+int(matrix[i][i])

    return sum


def right_diagonal_sum(matrix,matrix_size):

    sum = 0
    col = 0
    for i in range(matrix_size-1,-1,-1):
        sum = sum+int(matrix[i][col])
        col=col+1

    return sum

#creates matrix based on input
def create_matrix(matrixSize,input_matrix):

    matrix = [ [ 0 for i in range(matrixSize) ] for j in range(matrixSize) ]

    row_count=0
    for row in input_matrix.split('\n'):
        column_count=0
        for element in row.split():
            matrix[row_count][column_count] = element
            column_count=column_count+1

        row_count=row_count+1

    return matrix


if __name__ == "__main__": main()
