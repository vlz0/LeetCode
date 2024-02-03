class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        plana = []
        nueva = []

        for row in mat:
            for num in row:
                plana.append(num)
                
        if r * c != len(plana):
            return mat
        else:
            for row_index in range(r):
                nueva.append(plana[row_index * c : row_index * c + c])
            return nueva
