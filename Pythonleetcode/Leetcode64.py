# class Solution(object):
#     def minPathSum(self, grid):
#         m = len(grid)
#         n = len(grid[0])
#         for i in range(1, n):
#             grid[0][i] += grid[0][i - 1]
#         for i in range(1, m):
#             grid[i][0] += grid[i - 1][0]
#         for i in range(1, m):
#             for j in range(1, n):
#                 grid[i][j] += (grid[i][j - 1] if grid[i][j - 1] < grid[i - 1][j] else grid[i - 1][j])
#         return grid[m - 1][n - 1]


class Solution(object):
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i>0 and j==0:
                    grid[i][j]+=grid[i-1][j]
                if i==0 and j>0:
                    grid[i][j] += grid[i][j-1]
                if i>0 and j>0:
                    grid[i][j]+=min(grid[i-1][j], grid[i][j-1])


        return grid[-1][-1]



print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))