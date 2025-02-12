public class Solution63 {
    public int UniquePathsWithObstacles(int[][] obstacleGrid) 
    {
        int m = obstacleGrid.Length;
        int n = obstacleGrid[0].Length;
        int[,] dp = new int[m,n];
        if (obstacleGrid[0][0]==0)
        {
            dp[0,0] = 1;
        }
        for (var i = 1; i < m; i++)
        {
            if (obstacleGrid[i][0]==0)
            {
                dp[i,0] = dp[i-1,0];
            }
        }
        for (var j = 1; j < n; j++)
        {
            if (obstacleGrid[0][j]==0)
            {
                dp[0,j] = dp[0,j-1];
            }
        }
        for (var i = 1; i < m; i++)
        {
            for (var j = 1; j < n; j++)
            {
                if (obstacleGrid[i][j]==0)
                {
                    dp[i,j] = dp[i-1,j]+dp[i,j-1];
                }
            }
        }
        return dp[m-1,n-1];
    }
}