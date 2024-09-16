class Solution(object):
    def surfaceArea(self, grid):
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans=ans+grid[i][j]*4+2*(grid[i][j]>0)
        for i in range(len(grid)-1):
            for j in range(len(grid[0])-1):
                ans=ans-((min(grid[i][j],grid[i+1][j])+min(grid[i][j],grid[i][j+1]))*2)

        for i in range(len(grid)-1):
            ans=ans-(2*min(grid[i][len(grid[0])-1],grid[i+1][len(grid[0])-1]))


        for i in range(len(grid[0])-1):
            ans = ans - (2 * min(grid[len(grid) - 1][i], grid[len(grid) - 1][i+1]))
        return ans


print(Solution().surfaceArea([[2]]))
print(Solution().surfaceArea([[1,2],[3,4]]))
print(Solution().surfaceArea([[1,0],[0,2]]))
print(Solution().surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))




