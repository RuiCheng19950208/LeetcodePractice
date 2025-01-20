public class Solution221 {
    public int MaximalSquare(char[][] matrix) 
    {
        int row = matrix.Length;
        int col = matrix[0].Length;
        List<List<int>> dp = new List<List<int>>();
        for(int i=0;i<row;i++)
        {
            List<int> temp = new List<int>();
            for(int j=0;j<col;j++)
            {
                temp.Add(0);
            }
            dp.Add(temp);
        }
        int ans = 0;
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(matrix[i][j]=='1')
                {
                    if(i>0 && j>0)
                    {
                        
                        dp[i][j]=new List<int> {dp[i-1][j-1],dp[i][j-1],dp[i-1][j]}.Min()+1;
                    }
                    else{dp[i][j]=1;}
                    ans=Math.Max(ans,dp[i][j]);
                }
            }
        }
        return ans*ans;
    }
}