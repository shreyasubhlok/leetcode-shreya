class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        row=len(grid)
        col=len(grid[0])
        res=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    res+=1
                    self.dfs(i,j,grid)
                    
        return res
    
    def dfs(self,r,c,grid):
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!="1":
            return
        
        grid[r][c]="0"   #mark them visited so that you dont get into infinited recursive call
        self.dfs(r+1,c,grid)
        self.dfs(r-1,c,grid)
        self.dfs(r,c+1,grid)
        self.dfs(r,c-1,grid)