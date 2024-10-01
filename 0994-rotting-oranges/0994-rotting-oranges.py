class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        freshOranges=0
        q=deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    freshOranges=freshOranges+1
                if grid[r][c]==2:
                    q.append([r,c])
                    
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while len(q)!=0 and freshOranges>0:
            for i in range(len(q)):
                temp=q.popleft()
                row=temp[0]
                col=temp[1]
                for r,c in directions:
                    newRow=row+r
                    newCol=col+c
                    if newRow<0 or newRow>=len(grid) or newCol<0 or newCol>=len(grid[0]) or grid[newRow][newCol]!=1:
                        continue
                    grid[newRow][newCol]=2
                    q.append([newRow,newCol])
                    freshOranges=freshOranges-1
            time=time+1
            
        if freshOranges==0:
            return time
        else:
            return -1