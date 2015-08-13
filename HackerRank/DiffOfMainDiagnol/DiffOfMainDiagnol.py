### WORK IN PROGRESS

def main():

    matrixSize =int(input())
    matrix = [matrixSize][matrixSize]
    for i in range(0,matrixSize):
        row = list(input())
        if(len(row)!= matrixSize):
            print("Invalid row entries")
            break;
        matrix = create_matrix_row(i,row)

def create_matrix_row(row_number,matrix,row):
    for i in range(0,len(row)):
        matrix[row_number][i] = row[i]
    return matrix



if __name__ == '__main__':
   main()