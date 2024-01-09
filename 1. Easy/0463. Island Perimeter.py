class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        perimetro = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimetro += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimetro -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimetro -= 2

        return perimetro
