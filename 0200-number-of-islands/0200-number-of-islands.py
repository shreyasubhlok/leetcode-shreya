class Solution:
    #time is o(m*n), m rows and n cols
    #space is o(m*n) worst case,n case that the grid map is filled with lands where DFS goes by m*n deep
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty or has no columns
        if not grid or not grid[0]:
            return 0
        
        row=len(grid)
        col=len(grid[0])
        res=0
        
        for i in range(row):
            for j in range(col):
                # If the cell contains '1', it indicates the start of a new island
                if grid[i][j]=="1": 
                    res+=1
                    self.dfs(i,j,grid) # Perform DFS to mark all connected land cells as visited
                    
        return res
    
    def dfs(self,r,c,grid):
        # Check boundaries and if the cell is water or already visited
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!="1":
            return
        
        grid[r][c]="0"   #  # Mark the cell as visited by setting it to '0' ..imp
        
        # Recursively visit all adjacent cells (up, down, left, right)
        self.dfs(r+1,c,grid)
        self.dfs(r-1,c,grid)
        self.dfs(r,c+1,grid)
        self.dfs(r,c-1,grid)