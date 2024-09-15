from typing import List

class Solution:

    def numIslands(self, grid: List[List[int]]) -> int:
        # Check if the grid is empty
        if not grid or not grid[0]:
            return 0

        row = len(grid)
        col = len(grid[0])
        res = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(i, j, grid)

        return res

    def dfs(self, r: int, c: int, grid: List[List[int]]) -> None:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        self.dfs(r + 1, c, grid)
        self.dfs(r - 1, c, grid)
        self.dfs(r, c + 1, grid)
        self.dfs(r, c - 1, grid)
