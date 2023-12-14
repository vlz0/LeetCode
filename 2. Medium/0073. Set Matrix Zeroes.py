class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for k in range(col):
                        if matrix[i][k] == 0:
                            matrix[i][k] = None
                        else:
                            matrix[i][k] = 0
                    break
        
        for i in range(col):
            for j in range(row):
                if matrix[j][i] == None:
                    for k in range(row):
                        matrix[k][i] = 0
                    break
