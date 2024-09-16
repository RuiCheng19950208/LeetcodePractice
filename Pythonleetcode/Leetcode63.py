class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp=[[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                elif j==0 and i==0:
                    dp[i][j]=1
                else:
                    if i>0:
                        dp[i][j]+=dp[i-1][j]
                    if j>0:
                        dp[i][j]+=dp[i][j-1]
        return dp[-1][-1]

print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().uniquePathsWithObstacles([[1,0,0]]))