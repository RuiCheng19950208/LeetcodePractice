class Solution:
    def islandPerimeter(self, grid):
        sum=0
        minus=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==1:
                    sum=sum+1
                    if i>0:
                        if grid[i-1][j]==1:
                            minus=minus+1
                    if i<len(grid)-1:
                        if grid[i+1][j]==1:
                            minus=minus+1
                    if j>0:
                        if grid[i][j-1]==1:
                            minus=minus+1
                    if j<len(grid[0])-1:
                        if grid[i][j+1]==1:
                            minus=minus+1
        return 4*sum-minus



print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))