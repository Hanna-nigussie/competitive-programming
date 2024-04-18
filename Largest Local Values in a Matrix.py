
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        largestLocal = []
        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                submatrix_max = max(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[i][j-1],   grid[i][j],   grid[i][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
                )
                row.append(submatrix_max)
            largestLocal.append(row)
        
        return largestLocal