using System.Numerics;

public class Solution62 {
    public int UniquePaths(int m, int n) 
    {
        int[,] dp = new int[m,n];
        for (var i = 0; i < m; i++)
        {
            for (var j = 0; j < n; j++)
            {
                if (i==0 || j==0)
                {
                    dp[i,j] = 1;
                }
                else
                {
                    dp[i,j] = dp[i-1,j]+dp[i,j-1];
                }
            }
            
        }
        return dp[m-1,n-1];
        
    }
}