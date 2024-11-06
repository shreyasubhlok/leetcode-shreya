class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        maxarea = 0

        def dfstraversal(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            currArea=1
            currArea += dfstraversal(r + 1, c)
            currArea += dfstraversal(r - 1, c)
            currArea += dfstraversal(r, c + 1)
            currArea += dfstraversal(r, c - 1)
            return currArea


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    currArea = dfstraversal(i, j)
                    maxarea = max(maxarea, currArea)

        return maxarea
