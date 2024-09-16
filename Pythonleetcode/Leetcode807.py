class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        m1=[]
        m2=[]
        for i in grid:
            m2.append(max(i))

        for j in range(len(grid[0])):
            a=[]
            for i in range(len(grid)):
                a.append(grid[i][j])
            m1.append(max(a))

        a=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                a=a+min(m1[j],m2[i])-grid[i][j]
                grid[i][j]=min(m1[j],m2[i])
        return a








print(Solution().maxIncreaseKeepingSkyline([[3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]))