class Solution(object):
    def projectionArea(self, grid):
        def top(grid):
            ans=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]!=0:
                        ans=ans+1
            return ans


        def left(grid):
            ans = 0
            newgrid=[]
            for i in range(len(grid[0])):
                for j in range(len(grid)):
                    newgrid.append(grid[j][i])
                ans=ans+max(newgrid)
                newgrid=[]
            return ans

        def front(grid):
            ans = 0
            for i in range(len(grid)):
                ans = ans + max(grid[i])
            return ans
        # print(top(grid),left(grid),front(grid))

        return top(grid)+left(grid)+front(grid)



print(Solution().projectionArea([[1,2],[3,4]]))
print(Solution().projectionArea([[1,0],[0,2]]))
print(Solution().projectionArea([[2,2,2],[2,1,2],[2,2,2]]))